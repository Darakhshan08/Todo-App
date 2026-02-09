/**
 * Task Creation Form Component
 * Task: T025 [US1], T054 [US6] Create task creation form component with priority and tags
 */
"use client";

import { useState } from "react";

interface TaskFormProps {
  onSubmit: (data: {
    title: string;
    description?: string;
    priority?: "high" | "medium" | "low";
    tags?: string[];
    due_date?: string;
    recurring?: string;
  }) => Promise<void>;
  loading?: boolean;
}

export default function TaskForm({ onSubmit, loading = false }: TaskFormProps) {
  const [formData, setFormData] = useState({
    title: "",
    description: "",
    priority: "medium" as "high" | "medium" | "low",
    tagInput: "",
    tags: [] as string[],
    due_date: "",
    recurring: "none",
  });
  const [errors, setErrors] = useState<Record<string, string>>({});

  const validateForm = () => {
    const newErrors: Record<string, string> = {};

    if (!formData.title.trim()) {
      newErrors.title = "Title is required";
    } else if (formData.title.length > 200) {
      newErrors.title = "Title must be 200 characters or less";
    }

    if (formData.description && formData.description.length > 1000) {
      newErrors.description = "Description must be 1000 characters or less";
    }

    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();

    if (!validateForm()) return;

    try {
      const submitData: any = {
        title: formData.title.trim(),
        description: formData.description.trim() || undefined,
        priority: formData.priority,
        tags: formData.tags,
      };

      // Only include due_date if provided
      if (formData.due_date) {
        submitData.due_date = new Date(formData.due_date).toISOString();
      }

      // Only include recurring if not "none"
      if (formData.recurring && formData.recurring !== "none") {
        submitData.recurring = formData.recurring;
      }

      await onSubmit(submitData);

      // Reset form on success
      setFormData({
        title: "",
        description: "",
        priority: "medium",
        tagInput: "",
        tags: [],
        due_date: "",
        recurring: "none",
      });
      setErrors({});
    } catch (error) {
      setErrors({ submit: "Failed to create task" });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4 rounded-lg border bg-white p-6 shadow-sm">
      <h2 className="text-xl font-semibold text-gray-900">Create New Task</h2>

      {errors.submit && (
        <div className="rounded-md bg-red-50 p-4">
          <p className="text-sm text-red-800">{errors.submit}</p>
        </div>
      )}

      <div>
        <label htmlFor="title" className="block text-sm font-medium text-gray-700">
          Title <span className="text-red-500">*</span>
        </label>
        <input
          id="title"
          name="title"
          type="text"
          value={formData.title}
          onChange={(e) => setFormData({ ...formData, title: e.target.value })}
          className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
          placeholder="Enter task title"
          maxLength={200}
          disabled={loading}
        />
        {errors.title && <p className="mt-1 text-sm text-red-600">{errors.title}</p>}
        <p className="mt-1 text-xs text-gray-500">{formData.title.length}/200 characters</p>
      </div>

      <div>
        <label htmlFor="description" className="block text-sm font-medium text-gray-700">
          Description (optional)
        </label>
        <textarea
          id="description"
          name="description"
          value={formData.description}
          onChange={(e) => setFormData({ ...formData, description: e.target.value })}
          className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
          placeholder="Enter task description"
          rows={3}
          maxLength={1000}
          disabled={loading}
        />
        {errors.description && <p className="mt-1 text-sm text-red-600">{errors.description}</p>}
        <p className="mt-1 text-xs text-gray-500">{formData.description.length}/1000 characters</p>
      </div>

      <div>
        <label htmlFor="priority" className="block text-sm font-medium text-gray-700">
          Priority
        </label>
        <select
          id="priority"
          name="priority"
          value={formData.priority}
          onChange={(e) => setFormData({ ...formData, priority: e.target.value as "high" | "medium" | "low" })}
          className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
          disabled={loading}
        >
          <option value="high">High</option>
          <option value="medium">Medium</option>
          <option value="low">Low</option>
        </select>
      </div>

      <div>
        <label htmlFor="tags" className="block text-sm font-medium text-gray-700">
          Tags (optional)
        </label>
        <div className="mt-1 flex gap-2">
          <input
            id="tags"
            name="tags"
            type="text"
            value={formData.tagInput}
            onChange={(e) => setFormData({ ...formData, tagInput: e.target.value })}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                e.preventDefault();
                const tag = formData.tagInput.trim();
                if (tag && !formData.tags.includes(tag)) {
                  setFormData({
                    ...formData,
                    tags: [...formData.tags, tag],
                    tagInput: "",
                  });
                }
              }
            }}
            className="block flex-1 rounded-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
            placeholder="Add tag and press Enter (e.g., work, home)"
            disabled={loading}
          />
          <button
            type="button"
            onClick={() => {
              const tag = formData.tagInput.trim();
              if (tag && !formData.tags.includes(tag)) {
                setFormData({
                  ...formData,
                  tags: [...formData.tags, tag],
                  tagInput: "",
                });
              }
            }}
            className="rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50 disabled:opacity-50"
            disabled={loading}
          >
            Add
          </button>
        </div>
        {formData.tags.length > 0 && (
          <div className="mt-2 flex flex-wrap gap-2">
            {formData.tags.map((tag, index) => (
              <span
                key={index}
                className="inline-flex items-center gap-1 rounded-full bg-blue-100 px-3 py-1 text-sm text-blue-800"
              >
                {tag}
                <button
                  type="button"
                  onClick={() => {
                    setFormData({
                      ...formData,
                      tags: formData.tags.filter((_, i) => i !== index),
                    });
                  }}
                  className="hover:text-blue-600"
                  disabled={loading}
                >
                  ×
                </button>
              </span>
            ))}
          </div>
        )}
      </div>

      <div>
        <label htmlFor="due_date" className="block text-sm font-medium text-gray-700">
          Due Date (optional)
        </label>
        <input
          id="due_date"
          name="due_date"
          type="datetime-local"
          value={formData.due_date}
          onChange={(e) => setFormData({ ...formData, due_date: e.target.value })}
          className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
          disabled={loading}
        />
        <p className="mt-1 text-xs text-gray-500">Set a deadline for this task</p>
      </div>

      <div>
        <label htmlFor="recurring" className="block text-sm font-medium text-gray-700">
          Recurring (optional)
        </label>
        <select
          id="recurring"
          name="recurring"
          value={formData.recurring}
          onChange={(e) => setFormData({ ...formData, recurring: e.target.value })}
          className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
          disabled={loading}
        >
          <option value="none">None</option>
          <option value="daily">Daily</option>
          <option value="weekly">Weekly</option>
          <option value="monthly">Monthly</option>
          <option value="yearly">Yearly</option>
        </select>
        <p className="mt-1 text-xs text-gray-500">Auto-reschedule this task</p>
      </div>

      <button
        type="submit"
        disabled={loading}
        className="w-full rounded-md border border-transparent bg-blue-600 px-4 py-2 text-sm font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2 disabled:opacity-50"
      >
        {loading ? "Creating..." : "Create Task"}
      </button>
    </form>
  );
}
