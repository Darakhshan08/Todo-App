/**
 * Authentication Functions for FastAPI Backend
 * Handles JWT token authentication
 * Task: T027 [US1] JWT token handling and user context
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000";

interface SignUpData {
  email: string;
  password: string;
  name: string;
}

interface SignInData {
  email: string;
  password: string;
}

interface AuthResponse {
  token: string;
  user: {
    id: string;
    email: string;
    name: string;
  };
}

/**
 * Sign up a new user
 */
export async function signUp(data: SignUpData): Promise<AuthResponse> {
  const response = await fetch(`${API_BASE_URL}/api/auth/signup`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Signup failed");
  }

  const result = await response.json();

  // Store token in localStorage
  if (typeof window !== "undefined") {
    localStorage.setItem("auth_token", result.token);
    localStorage.setItem("user", JSON.stringify(result.user));
  }

  return result;
}

/**
 * Sign in an existing user
 */
export async function signIn(data: SignInData): Promise<AuthResponse> {
  const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!response.ok) {
    const error = await response.json();
    throw new Error(error.detail || "Login failed");
  }

  const result = await response.json();

  // Store token in localStorage
  if (typeof window !== "undefined") {
    localStorage.setItem("auth_token", result.token);
    localStorage.setItem("user", JSON.stringify(result.user));
  }

  return result;
}

/**
 * Sign out the current user
 */
export async function signOut(): Promise<void> {
  // Remove token from localStorage
  if (typeof window !== "undefined") {
    localStorage.removeItem("auth_token");
    localStorage.removeItem("user");
  }

  // Optional: Call backend logout endpoint
  try {
    const token = getAuthToken();
    if (token) {
      await fetch(`${API_BASE_URL}/api/auth/logout`, {
        method: "POST",
        headers: {
          Authorization: `Bearer ${token}`,
        },
      });
    }
  } catch (error) {
    console.error("Logout error:", error);
  }
}

/**
 * Get auth token from localStorage
 */
export function getAuthToken(): string | null {
  if (typeof window === "undefined") return null;
  return localStorage.getItem("auth_token");
}

/**
 * Get current user from localStorage
 */
export function getCurrentUser(): { id: string; email: string; name: string } | null {
  if (typeof window === "undefined") return null;
  const userStr = localStorage.getItem("user");
  return userStr ? JSON.parse(userStr) : null;
}

/**
 * Check if user is authenticated
 */
export function isAuthenticated(): boolean {
  return getAuthToken() !== null;
}
