/**
 * API Client for Frontend-Backend Communication
 * Handles JWT token injection and error handling
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

/**
 * Get JWT token from localStorage
 */
function getAuthToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("auth_token");
}

/**
 * Generic API request function with JWT token injection
 */
async function apiRequest<T>(
  endpoint: string,
  options: RequestInit = {}
): Promise<T> {
  const token = getAuthToken();

  const headers: HeadersInit = {
    "Content-Type": "application/json",
    ...(options.headers || {}),
  };

  if (token) {
    headers["Authorization"] = `Bearer ${token}`;
  }

  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    ...options,
    headers,
    credentials: 'include', // Required for CORS with credentials
  });

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: "An error occurred" }));
    throw new Error(error.detail || `HTTP ${response.status}`);
  }

  return response.json();
}

/**
 * API client methods
 */
export const api = {
  // Task operations
  getTasks: (
    userId: string,
    params?: {
      status?: string;
      priority?: string;
      tag?: string;
      search?: string;
      sort?: string;
    }
  ) => {
    const queryParams = new URLSearchParams();
    if (params?.status) queryParams.set("status", params.status);
    if (params?.priority) queryParams.set("priority", params.priority);
    if (params?.tag) queryParams.set("tag", params.tag);
    if (params?.search) queryParams.set("search", params.search);
    if (params?.sort) queryParams.set("sort", params.sort);

    const queryString = queryParams.toString();
    return apiRequest<any>(`/api/${userId}/tasks${queryString ? `?${queryString}` : ""}`);
  },

  createTask: (
    userId: string,
    data: {
      title: string;
      description?: string;
      priority?: string;
      tags?: string[];
      due_date?: string;
      recurring?: string;
    }
  ) => {
    return apiRequest<any>(`/api/${userId}/tasks`, {
      method: "POST",
      body: JSON.stringify(data),
    });
  },

  getTask: (userId: string, taskId: number) => {
    return apiRequest<any>(`/api/${userId}/tasks/${taskId}`);
  },

  updateTask: (
    userId: string,
    taskId: number,
    data: {
      title?: string;
      description?: string;
      priority?: string;
      tags?: string[];
      due_date?: string;
      recurring?: string;
    }
  ) => {
    return apiRequest<any>(`/api/${userId}/tasks/${taskId}`, {
      method: "PUT",
      body: JSON.stringify(data),
    });
  },

  deleteTask: (userId: string, taskId: number) => {
    return apiRequest<any>(`/api/${userId}/tasks/${taskId}`, {
      method: "DELETE",
    });
  },

  toggleTaskComplete: (userId: string, taskId: number) => {
    return apiRequest<any>(`/api/${userId}/tasks/${taskId}/complete`, {
      method: "PATCH",
    });
  },
};
