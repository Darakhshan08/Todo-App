/**
 * Search and Filter Controls Component
 * Task: T059 [US7], T060 [US7] Create search and filter controls
 */
"use client";

import { useState, useEffect } from "react";

interface SearchFilterProps {
  onSearch: (keyword: string) => void;
  onFilterPriority: (priority: string | null) => void;
  onFilterTag: (tag: string | null) => void;
  onSort: (sortBy: string) => void;
  loading?: boolean;
}

export default function SearchFilter({
  onSearch,
  onFilterPriority,
  onFilterTag,
  onSort,
  loading = false,
}: SearchFilterProps) {
  const [searchKeyword, setSearchKeyword] = useState("");
  const [selectedPriority, setSelectedPriority] = useState<string | null>(null);
  const [selectedTag, setSelectedTag] = useState<string | null>(null);
  const [sortBy, setSortBy] = useState("created");

  // Debounced search
  useEffect(() => {
    const timer = setTimeout(() => {
      onSearch(searchKeyword);
    }, 300);

    return () => clearTimeout(timer);
  }, [searchKeyword, onSearch]);

  const handlePriorityChange = (priority: string) => {
    const newPriority = selectedPriority === priority ? null : priority;
    setSelectedPriority(newPriority);
    onFilterPriority(newPriority);
  };

  const handleTagChange = (tag: string) => {
    const newTag = selectedTag === tag ? null : tag;
    setSelectedTag(newTag);
    onFilterTag(newTag);
  };

  const handleSortChange = (newSortBy: string) => {
    setSortBy(newSortBy);
    onSort(newSortBy);
  };

  return (
    <div className="space-y-4 rounded-lg border bg-white p-4 shadow-sm">
      <h3 className="text-lg font-semibold text-gray-900">Search & Filter</h3>

      {/* Search Input */}
      <div>
        <label htmlFor="search" className="block text-sm font-medium text-gray-700">
          Search
        </label>
        <input
          id="search"
          type="text"
          value={searchKeyword}
          onChange={(e) => setSearchKeyword(e.target.value)}
          placeholder="Search tasks by title or description..."
          className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 placeholder-gray-400 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
          disabled={loading}
        />
      </div>

      {/* Priority Filter */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Priority
        </label>
        <div className="flex gap-2">
          {["high", "medium", "low"].map((priority) => (
            <button
              key={priority}
              onClick={() => handlePriorityChange(priority)}
              className={`rounded-md px-3 py-1 text-sm font-medium transition-colors ${
                selectedPriority === priority
                  ? priority === "high"
                    ? "bg-red-600 text-white"
                    : priority === "medium"
                    ? "bg-yellow-600 text-white"
                    : "bg-green-600 text-white"
                  : "bg-gray-100 text-gray-700 hover:bg-gray-200"
              }`}
              disabled={loading}
            >
              {priority.charAt(0).toUpperCase() + priority.slice(1)}
            </button>
          ))}
        </div>
      </div>

      {/* Tag Filter */}
      <div>
        <label className="block text-sm font-medium text-gray-700 mb-2">
          Quick Tags
        </label>
        <div className="flex flex-wrap gap-2">
          {["work", "home", "personal", "urgent"].map((tag) => (
            <button
              key={tag}
              onClick={() => handleTagChange(tag)}
              className={`rounded-full px-3 py-1 text-sm font-medium transition-colors ${
                selectedTag === tag
                  ? "bg-blue-600 text-white"
                  : "bg-blue-100 text-blue-800 hover:bg-blue-200"
              }`}
              disabled={loading}
            >
              #{tag}
            </button>
          ))}
        </div>
      </div>

      {/* Sort Controls */}
      <div>
        <label htmlFor="sort" className="block text-sm font-medium text-gray-700">
          Sort By
        </label>
        <select
          id="sort"
          value={sortBy}
          onChange={(e) => handleSortChange(e.target.value)}
          className="mt-1 block w-full rounded-md border border-gray-300 px-3 py-2 text-gray-900 focus:border-blue-500 focus:outline-none focus:ring-blue-500 sm:text-sm"
          disabled={loading}
        >
          <option value="created">Date Created (Newest)</option>
          <option value="updated">Date Updated (Newest)</option>
          <option value="title">Title (A-Z)</option>
          <option value="priority">Priority (High to Low)</option>
        </select>
      </div>

      {/* Active Filters Display */}
      {(searchKeyword || selectedPriority || selectedTag) && (
        <div className="border-t pt-3">
          <p className="text-xs font-medium text-gray-500 mb-2">Active Filters:</p>
          <div className="flex flex-wrap gap-2">
            {searchKeyword && (
              <span className="inline-flex items-center gap-1 rounded-full bg-gray-100 px-2 py-1 text-xs text-gray-700">
                Search: "{searchKeyword}"
                <button
                  onClick={() => setSearchKeyword("")}
                  className="hover:text-gray-900"
                  disabled={loading}
                >
                  ×
                </button>
              </span>
            )}
            {selectedPriority && (
              <span className="inline-flex items-center gap-1 rounded-full bg-gray-100 px-2 py-1 text-xs text-gray-700">
                Priority: {selectedPriority}
                <button
                  onClick={() => {
                    setSelectedPriority(null);
                    onFilterPriority(null);
                  }}
                  className="hover:text-gray-900"
                  disabled={loading}
                >
                  ×
                </button>
              </span>
            )}
            {selectedTag && (
              <span className="inline-flex items-center gap-1 rounded-full bg-gray-100 px-2 py-1 text-xs text-gray-700">
                Tag: #{selectedTag}
                <button
                  onClick={() => {
                    setSelectedTag(null);
                    onFilterTag(null);
                  }}
                  className="hover:text-gray-900"
                  disabled={loading}
                >
                  ×
                </button>
              </span>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
