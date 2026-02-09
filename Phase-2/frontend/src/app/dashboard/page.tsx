/**
 * Dashboard Page - Full Task Management
 * Tasks: T026, T028 [US1], T032, T034 [US2], T039, T040 [US3], T044, T045 [US4], T049, T050 [US5]
 */
"use client";

import { useEffect, useState } from "react";
import { useRouter } from "next/navigation";
import { useUser } from "@/contexts/UserContext";
import { api } from "@/lib/api";
import TaskForm from "@/components/TaskForm";
import TaskList from "@/components/TaskList";

interface Task {
  id: number;
  title: string;
  description?: string;
  completed: boolean;
  priority: string;
  tags: string[];
  due_date?: string;
  recurring?: string;
  created_at: string;
  updated_at: string;
}

export default function DashboardPage() {
  const router = useRouter();
  const { user, loading: userLoading, isLoggedIn, logout } = useUser();
  const [tasks, setTasks] = useState<Task[]>([]);
  const [loading, setLoading] = useState(true);
  const [creating, setCreating] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [editingTask, setEditingTask] = useState<Task | null>(null);

  // Filter, search, and sort state
  const [searchQuery, setSearchQuery] = useState("");
  const [statusFilter, setStatusFilter] = useState("all");
  const [priorityFilter, setPriorityFilter] = useState("all");
  const [sortBy, setSortBy] = useState("created");

  // Notification state
  const [notificationPermission, setNotificationPermission] = useState<NotificationPermission>("default");

  // Redirect to login if not authenticated
  useEffect(() => {
    if (!userLoading && !isLoggedIn) {
      router.push("/login");
    }
  }, [userLoading, isLoggedIn, router]);

  // Fetch tasks on mount and when filters change
  useEffect(() => {
    if (user) {
      fetchTasks();
    }
  }, [user, searchQuery, statusFilter, priorityFilter, sortBy]);

  // Check and update notification permission status
  useEffect(() => {
    if (typeof window !== "undefined" && "Notification" in window) {
      setNotificationPermission(Notification.permission);

      // Auto-request permission on first visit
      if (Notification.permission === "default") {
        Notification.requestPermission().then(permission => {
          setNotificationPermission(permission);
        });
      }
    }
  }, []);

  // Browser Notifications for Due Dates
  useEffect(() => {
    console.log("[Notification Debug] useEffect triggered");
    console.log("[Notification Debug] Window check:", typeof window !== "undefined");
    console.log("[Notification Debug] Notification API available:", typeof window !== "undefined" && "Notification" in window);
    console.log("[Notification Debug] Tasks count:", tasks?.length || 0);
    console.log("[Notification Debug] Permission:", typeof window !== "undefined" && "Notification" in window ? Notification.permission : "N/A");

    if (typeof window === "undefined" || !("Notification" in window)) {
      console.log("[Notification Debug] BLOCKED: Window or Notification API not available");
      return;
    }
    if (!tasks || tasks.length === 0) {
      console.log("[Notification Debug] BLOCKED: No tasks available");
      return;
    }
    if (Notification.permission !== "granted") {
      console.log("[Notification Debug] BLOCKED: Permission not granted, current permission:", Notification.permission);
      return;
    }

    console.log("[Notification Debug] ✅ All checks passed, setting up notification monitoring");

    // Function to check and show notifications
    const checkNotifications = () => {
      const now = new Date();
      const fifteenMinutesFromNow = new Date(now.getTime() + 15 * 60 * 1000);

      console.log("[Notification Debug] Check running at:", now.toLocaleTimeString());
      console.log("[Notification Debug] 15-minute window:", fifteenMinutesFromNow.toLocaleTimeString());
      console.log("[Notification Debug] Checking", tasks.length, "tasks");

      tasks.forEach((task) => {
        console.log(`[Notification Debug] Task "${task.title}":`, {
          id: task.id,
          completed: task.completed,
          has_due_date: !!task.due_date,
          due_date: task.due_date
        });

        // Skip completed tasks or tasks without due dates
        if (task.completed) {
          console.log(`[Notification Debug] ❌ Skipped "${task.title}": Task is completed`);
          return;
        }
        if (!task.due_date) {
          console.log(`[Notification Debug] ❌ Skipped "${task.title}": No due date`);
          return;
        }

        const dueDate = new Date(task.due_date);
        const minutesUntilDue = Math.round((dueDate.getTime() - now.getTime()) / 60000);

        console.log(`[Notification Debug] Task "${task.title}" due in ${minutesUntilDue} minutes`);
        console.log(`[Notification Debug] Due date: ${dueDate.toLocaleString()}`);
        console.log(`[Notification Debug] Is future: ${dueDate > now}`);
        console.log(`[Notification Debug] Within 15min window: ${dueDate <= fifteenMinutesFromNow}`);

        // Check if task is due within 15 minutes
        if (dueDate > now && dueDate <= fifteenMinutesFromNow) {
          console.log(`[Notification Debug] ✅ Task "${task.title}" qualifies for notification!`);

          // Create unique notification ID
          const notificationId = `task-${task.id}-${dueDate.getTime()}`;

          // Check if we've already shown this notification
          const shownNotifications = JSON.parse(
            localStorage.getItem("shownNotifications") || "[]"
          );

          console.log(`[Notification Debug] Notification ID: ${notificationId}`);
          console.log(`[Notification Debug] Already shown: ${shownNotifications.includes(notificationId)}`);
          console.log(`[Notification Debug] Shown notifications:`, shownNotifications);

          if (!shownNotifications.includes(notificationId)) {
            console.log(`[Notification] 🔔 SHOWING NOTIFICATION for task "${task.title}" due in ${minutesUntilDue} minutes`);

            try {
              // Show notification
              const notification = new Notification("⏰ Task Due Soon!", {
                body: `"${task.title}" is due in ${minutesUntilDue} minute${minutesUntilDue !== 1 ? 's' : ''}`,
                icon: "/favicon.ico",
                badge: "/favicon.ico",
                tag: notificationId,
                requireInteraction: false,
                silent: false,
              });

              console.log("[Notification] ✅ Notification object created successfully");

              // Mark as shown
              shownNotifications.push(notificationId);
              localStorage.setItem(
                "shownNotifications",
                JSON.stringify(shownNotifications)
              );

              console.log("[Notification] Notification marked as shown in localStorage");

              // Clear old notification IDs (keep only last 100)
              if (shownNotifications.length > 100) {
                localStorage.setItem(
                  "shownNotifications",
                  JSON.stringify(shownNotifications.slice(-100))
                );
              }

              // Auto-close notification after 10 seconds
              setTimeout(() => notification.close(), 10000);

              // Click handler to focus window
              notification.onclick = () => {
                window.focus();
                notification.close();
              };
            } catch (error) {
              console.error("[Notification] ❌ Error creating notification:", error);
            }
          } else {
            console.log(`[Notification Debug] ⏭️ Skipped "${task.title}": Already shown this notification`);
          }
        } else {
          console.log(`[Notification Debug] ❌ Task "${task.title}" doesn't qualify: Not in 15-minute window`);
        }
      });

      console.log("[Notification Debug] Check complete");
    };

    // Check immediately on mount/task change
    console.log("[Notification Debug] Running initial check...");
    checkNotifications();

    // Then check every minute
    console.log("[Notification Debug] Setting up 60-second interval");
    const notificationInterval = setInterval(checkNotifications, 60000);

    // Cleanup interval on unmount
    return () => {
      console.log("[Notification Debug] Cleaning up interval");
      clearInterval(notificationInterval);
    };
  }, [tasks]);

  const fetchTasks = async () => {
    if (!user) return;

    try {
      setLoading(true);
      setError(null);
      const params: any = {
        sort: sortBy,
      };

      if (statusFilter !== "all") {
        params.status = statusFilter;
      }
      if (priorityFilter !== "all") {
        params.priority = priorityFilter;
      }
      if (searchQuery.trim()) {
        params.search = searchQuery.trim();
      }

      const data = await api.getTasks(user.id, params);
      setTasks(data);
    } catch (err: any) {
      setError(err.message || "Failed to fetch tasks");
    } finally {
      setLoading(false);
    }
  };

  // T028 [US1] - Create Task
  const handleCreateTask = async (taskData: {
    title: string;
    description?: string;
    priority?: string;
    tags?: string[];
    due_date?: string;
    recurring?: string;
  }) => {
    if (!user) return;

    try {
      setCreating(true);
      setError(null);
      const newTask = await api.createTask(user.id, taskData);
      setTasks([newTask, ...tasks]);
    } catch (err: any) {
      setError(err.message || "Failed to create task");
      throw err;
    } finally {
      setCreating(false);
    }
  };

  // T049 [US5] - Toggle Task Completion
  const handleToggleComplete = async (taskId: number) => {
    if (!user) return;

    try {
      const result = await api.toggleTaskComplete(user.id, taskId);
      setTasks(tasks.map((task) =>
        task.id === taskId ? { ...task, completed: result.completed } : task
      ));
    } catch (err: any) {
      setError(err.message || "Failed to toggle task completion");
    }
  };

  // T039 [US3] - Update Task
  const handleUpdateTask = async (
    taskId: number,
    taskData: {
      title?: string;
      description?: string;
      priority?: string;
      tags?: string[];
      due_date?: string;
      recurring?: string;
    }
  ) => {
    if (!user) return;

    try {
      const updatedTask = await api.updateTask(user.id, taskId, taskData);
      setTasks(tasks.map((task) => (task.id === taskId ? updatedTask : task)));
      setEditingTask(null);
    } catch (err: any) {
      setError(err.message || "Failed to update task");
    }
  };

  // T044 [US4] - Delete Task
  const handleDeleteTask = async (taskId: number) => {
    if (!user) return;

    // T045 [US4] - Confirmation dialog
    if (!confirm("Are you sure you want to delete this task?")) {
      return;
    }

    try {
      await api.deleteTask(user.id, taskId);
      setTasks(tasks.filter((task) => task.id !== taskId));
    } catch (err: any) {
      setError(err.message || "Failed to delete task");
    }
  };

  const handleSignOut = async () => {
    await logout();
    router.push("/login");
  };

  const requestNotificationPermission = async () => {
    if (typeof window === "undefined" || !("Notification" in window)) {
      alert("Your browser doesn't support notifications.");
      return;
    }

    try {
      const permission = await Notification.requestPermission();
      setNotificationPermission(permission);

      if (permission === "granted") {
        // Show immediate test notification
        const testNotification = new Notification("✅ Notifications Enabled!", {
          body: "You'll now receive reminders for tasks due soon.",
          icon: "/favicon.ico",
        });

        setTimeout(() => testNotification.close(), 5000);
      } else if (permission === "denied") {
        alert("Notifications blocked. Please enable them in your browser settings.");
      }
    } catch (error) {
      console.error("Notification permission error:", error);
      alert("Failed to request notification permission. Please check your browser settings.");
    }
  };

  // Show loading state while checking authentication
  if (userLoading || !user) {
    return (
      <div className="flex min-h-screen items-center justify-center">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-blue-600 border-t-transparent" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="border-b bg-white shadow-sm">
        <div className="mx-auto max-w-7xl px-4 py-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <h1 className="text-2xl font-bold text-gray-900">My Tasks</h1>
            <div className="flex items-center gap-4">
              <span className="text-sm text-gray-600">Welcome, {user.name}!</span>
              {notificationPermission !== "granted" && (
                <button
                  onClick={requestNotificationPermission}
                  className="rounded-md border border-orange-300 bg-orange-50 px-4 py-2 text-sm font-medium text-orange-700 hover:bg-orange-100 transition-colors"
                  title="Enable notifications for task reminders"
                >
                  🔔 Enable Notifications
                </button>
              )}
              {notificationPermission === "granted" && (
                <span className="text-sm text-green-600 flex items-center gap-1">
                  ✅ Notifications On
                </span>
              )}
              <button
                onClick={handleSignOut}
                className="rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
              >
                Sign Out
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="mx-auto max-w-7xl px-4 py-8 sm:px-6 lg:px-8">
        {error && (
          <div className="mb-4 rounded-md bg-red-50 p-4">
            <div className="flex justify-between">
              <p className="text-sm text-red-800">{error}</p>
              <button
                onClick={() => setError(null)}
                className="text-red-600 hover:text-red-800"
              >
                ×
              </button>
            </div>
          </div>
        )}

        {/* Search, Filter, and Sort Controls */}
        <div className="mb-6 rounded-lg border bg-white p-4 shadow-sm">
          <div className="grid gap-4 md:grid-cols-4">
            {/* Search */}
            <div>
              <label htmlFor="search" className="block text-sm font-medium text-gray-700 mb-1">
                Search
              </label>
              <input
                id="search"
                type="text"
                value={searchQuery}
                onChange={(e) => setSearchQuery(e.target.value)}
                placeholder="Search tasks..."
                className="block w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500"
              />
            </div>

            {/* Status Filter */}
            <div>
              <label htmlFor="status" className="block text-sm font-medium text-gray-700 mb-1">
                Status
              </label>
              <select
                id="status"
                value={statusFilter}
                onChange={(e) => setStatusFilter(e.target.value)}
                className="block w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500"
              >
                <option value="all">All</option>
                <option value="pending">Pending</option>
                <option value="completed">Completed</option>
              </select>
            </div>

            {/* Priority Filter */}
            <div>
              <label htmlFor="priority" className="block text-sm font-medium text-gray-700 mb-1">
                Priority
              </label>
              <select
                id="priority"
                value={priorityFilter}
                onChange={(e) => setPriorityFilter(e.target.value)}
                className="block w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500"
              >
                <option value="all">All</option>
                <option value="high">High</option>
                <option value="medium">Medium</option>
                <option value="low">Low</option>
              </select>
            </div>

            {/* Sort */}
            <div>
              <label htmlFor="sort" className="block text-sm font-medium text-gray-700 mb-1">
                Sort By
              </label>
              <select
                id="sort"
                value={sortBy}
                onChange={(e) => setSortBy(e.target.value)}
                className="block w-full rounded-md border border-gray-300 px-3 py-2 text-sm focus:border-blue-500 focus:outline-none focus:ring-blue-500"
              >
                <option value="created">Created (Newest)</option>
                <option value="updated">Updated (Newest)</option>
                <option value="title">Title (A-Z)</option>
                <option value="priority">Priority (High to Low)</option>
              </select>
            </div>
          </div>
        </div>

        <div className="grid gap-8 lg:grid-cols-3">
          {/* Task Creation Form */}
          <div className="lg:col-span-1">
            <TaskForm onSubmit={handleCreateTask} loading={creating} />
          </div>

          {/* Task List - T032 [US2] */}
          <div className="lg:col-span-2">
            <div className="rounded-lg border bg-white p-6 shadow-sm">
              <TaskList
                tasks={tasks}
                loading={loading}
                onToggleComplete={handleToggleComplete}
                onUpdate={(taskId) => {
                  const task = tasks.find((t) => t.id === taskId);
                  if (task) setEditingTask(task);
                }}
                onDelete={handleDeleteTask}
              />
            </div>
          </div>
        </div>

        {/* Edit Modal - T037, T038 [US3] */}
        {editingTask && (
          <div className="fixed inset-0 z-50 flex items-center justify-center bg-black bg-opacity-50 p-4">
            <div className="w-full max-w-md max-h-[90vh] overflow-y-auto rounded-lg bg-white p-6 shadow-xl">
              <h2 className="mb-4 text-xl font-semibold">Edit Task</h2>
              <form
                onSubmit={(e) => {
                  e.preventDefault();
                  const formData = new FormData(e.currentTarget);

                  const tagInput = formData.get("tags") as string;
                  const tags = tagInput ? tagInput.split(",").map(t => t.trim()).filter(Boolean) : [];

                  const updateData: any = {
                    title: formData.get("title") as string,
                    description: formData.get("description") as string || undefined,
                    priority: formData.get("priority") as string,
                    tags,
                  };

                  const dueDateValue = formData.get("due_date") as string;
                  if (dueDateValue) {
                    updateData.due_date = new Date(dueDateValue).toISOString();
                  }

                  const recurringValue = formData.get("recurring") as string;
                  if (recurringValue && recurringValue !== "none") {
                    updateData.recurring = recurringValue;
                  } else {
                    updateData.recurring = null;
                  }

                  handleUpdateTask(editingTask.id, updateData);
                }}
                className="space-y-4"
              >
                <div>
                  <label htmlFor="edit-title" className="block text-sm font-medium text-gray-700">
                    Title
                  </label>
                  <input
                    id="edit-title"
                    name="title"
                    type="text"
                    defaultValue={editingTask.title}
                    className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                    required
                  />
                </div>
                <div>
                  <label htmlFor="edit-description" className="block text-sm font-medium text-gray-700">
                    Description
                  </label>
                  <textarea
                    id="edit-description"
                    name="description"
                    defaultValue={editingTask.description || ""}
                    className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                    rows={3}
                  />
                </div>
                <div>
                  <label htmlFor="edit-priority" className="block text-sm font-medium text-gray-700">
                    Priority
                  </label>
                  <select
                    id="edit-priority"
                    name="priority"
                    defaultValue={editingTask.priority}
                    className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                  >
                    <option value="high">High</option>
                    <option value="medium">Medium</option>
                    <option value="low">Low</option>
                  </select>
                </div>
                <div>
                  <label htmlFor="edit-tags" className="block text-sm font-medium text-gray-700">
                    Tags (comma-separated)
                  </label>
                  <input
                    id="edit-tags"
                    name="tags"
                    type="text"
                    defaultValue={editingTask.tags?.join(", ") || ""}
                    className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                    placeholder="work, urgent, home"
                  />
                </div>
                <div>
                  <label htmlFor="edit-due-date" className="block text-sm font-medium text-gray-700">
                    Due Date
                  </label>
                  <input
                    id="edit-due-date"
                    name="due_date"
                    type="datetime-local"
                    defaultValue={editingTask.due_date ? new Date(editingTask.due_date).toISOString().slice(0, 16) : ""}
                    className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                  />
                </div>
                <div>
                  <label htmlFor="edit-recurring" className="block text-sm font-medium text-gray-700">
                    Recurring
                  </label>
                  <select
                    id="edit-recurring"
                    name="recurring"
                    defaultValue={editingTask.recurring || "none"}
                    className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2"
                  >
                    <option value="none">None</option>
                    <option value="daily">Daily</option>
                    <option value="weekly">Weekly</option>
                    <option value="monthly">Monthly</option>
                    <option value="yearly">Yearly</option>
                  </select>
                </div>
                <div className="flex gap-2">
                  <button
                    type="submit"
                    className="flex-1 rounded-md bg-blue-600 px-4 py-2 text-white hover:bg-blue-700"
                  >
                    Save Changes
                  </button>
                  <button
                    type="button"
                    onClick={() => setEditingTask(null)}
                    className="flex-1 rounded-md border border-gray-300 bg-white px-4 py-2 text-gray-700 hover:bg-gray-50"
                  >
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}
      </main>
    </div>
  );
}
