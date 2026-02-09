/**
 * Task List Component - Display tasks with status indicators
 * Task: T031 [US2] Create task list component with status indicators
 * Task: T033 [US2] Add task filtering by status (pending/completed)
 * Task: T055 [US6] Update task list component to display priority indicators and tags
 */
"use client";

import { useState } from "react";

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

interface TaskListProps {
  tasks: Task[];
  loading?: boolean;
  onToggleComplete?: (taskId: number) => void;
  onUpdate?: (taskId: number) => void;
  onDelete?: (taskId: number) => void;
}

export default function TaskList({
  tasks,
  loading = false,
  onToggleComplete,
  onUpdate,
  onDelete,
}: TaskListProps) {
  if (loading) {
    return (
      <div className="flex justify-center py-8">
        <div className="h-8 w-8 animate-spin rounded-full border-4 border-blue-600 border-t-transparent" />
      </div>
    );
  }

  return (
    <div className="space-y-4">
      <h2 className="text-xl font-semibold text-gray-900">
        Tasks ({tasks.length})
      </h2>

      {/* Task List */}
      {tasks.length === 0 ? (
        <div className="rounded-lg border border-gray-200 bg-white p-8 text-center">
          <p className="text-gray-500">
            No tasks found. Try adjusting your filters or create a new task!
          </p>
        </div>
      ) : (
        <div className="space-y-3">
          {tasks.map((task) => (
            <div
              key={task.id}
              className="group rounded-lg border border-gray-200 bg-white p-4 transition-all hover:border-gray-300 hover:shadow-sm"
            >
              <div className="flex items-start gap-3">
                {/* Completion Checkbox */}
                {onToggleComplete && (
                  <button
                    onClick={() => onToggleComplete(task.id)}
                    className="mt-1 flex-shrink-0"
                    aria-label={task.completed ? "Mark as incomplete" : "Mark as complete"}
                  >
                    <div
                      className={`flex h-5 w-5 items-center justify-center rounded border-2 ${
                        task.completed
                          ? "border-green-600 bg-green-600"
                          : "border-gray-300 hover:border-gray-400"
                      }`}
                    >
                      {task.completed && (
                        <svg
                          className="h-3 w-3 text-white"
                          fill="none"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path d="M5 13l4 4L19 7" />
                        </svg>
                      )}
                    </div>
                  </button>
                )}

                {/* Task Content */}
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2">
                    <h3
                      className={`font-medium ${
                        task.completed
                          ? "text-gray-400 line-through"
                          : "text-gray-900"
                      }`}
                    >
                      {task.title}
                    </h3>
                    {/* Priority Badge */}
                    <span
                      className={`rounded px-2 py-0.5 text-xs font-semibold ${
                        task.priority === "high"
                          ? "bg-red-100 text-red-800"
                          : task.priority === "medium"
                          ? "bg-yellow-100 text-yellow-800"
                          : "bg-green-100 text-green-800"
                      }`}
                    >
                      {task.priority.toUpperCase()}
                    </span>
                  </div>
                  {task.description && (
                    <p
                      className={`mt-1 text-sm ${
                        task.completed ? "text-gray-400" : "text-gray-600"
                      }`}
                    >
                      {task.description}
                    </p>
                  )}
                  {/* Tags */}
                  {task.tags && task.tags.length > 0 && (
                    <div className="mt-2 flex flex-wrap gap-1">
                      {task.tags.map((tag, index) => (
                        <span
                          key={index}
                          className="inline-block rounded-full bg-blue-100 px-2 py-0.5 text-xs text-blue-800"
                        >
                          #{tag}
                        </span>
                      ))}
                    </div>
                  )}
                  {/* Due Date and Recurring */}
                  <div className="mt-2 flex flex-wrap items-center gap-3 text-xs">
                    {task.due_date && (
                      <span className="flex items-center gap-1 text-orange-600">
                        <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
                        </svg>
                        Due: {new Date(task.due_date).toLocaleString()}
                      </span>
                    )}
                    {task.recurring && task.recurring !== "none" && (
                      <span className="flex items-center gap-1 text-purple-600">
                        <svg className="h-4 w-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15" />
                        </svg>
                        Recurring: {task.recurring}
                      </span>
                    )}
                  </div>
                  <div className="mt-2 flex items-center gap-4 text-xs text-gray-400">
                    <span>
                      Created: {new Date(task.created_at).toLocaleDateString()}
                    </span>
                    {task.updated_at !== task.created_at && (
                      <span>
                        Updated: {new Date(task.updated_at).toLocaleDateString()}
                      </span>
                    )}
                  </div>
                </div>

                {/* Status Badge */}
                <div className="flex flex-col items-end gap-2">
                  <span
                    className={`rounded-full px-3 py-1 text-xs font-medium ${
                      task.completed
                        ? "bg-green-100 text-green-800"
                        : "bg-yellow-100 text-yellow-800"
                    }`}
                  >
                    {task.completed ? "Completed" : "Pending"}
                  </span>

                  {/* Action Buttons */}
                  <div className="flex gap-2 opacity-0 transition-opacity group-hover:opacity-100">
                    {onUpdate && (
                      <button
                        onClick={() => onUpdate(task.id)}
                        className="rounded-md p-1 text-gray-400 hover:bg-gray-100 hover:text-blue-600"
                        aria-label="Edit task"
                      >
                        <svg
                          className="h-4 w-4"
                          fill="none"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
                        </svg>
                      </button>
                    )}
                    {onDelete && (
                      <button
                        onClick={() => onDelete(task.id)}
                        className="rounded-md p-1 text-gray-400 hover:bg-red-50 hover:text-red-600"
                        aria-label="Delete task"
                      >
                        <svg
                          className="h-4 w-4"
                          fill="none"
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth="2"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                      </button>
                    )}
                  </div>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
