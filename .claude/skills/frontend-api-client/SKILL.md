---
name: frontend-api-client
description: Create API client utility for backend communication. Builds type-safe API client with async functions, JWT token injection, error handling, and base URL configuration. Use when setting up API communication in frontend applications.
---

# Frontend API Client

This skill helps you create robust, type-safe API client utilities for communicating with backend services in frontend applications.

## Overview

A well-structured API client provides:
- **Type Safety**: TypeScript interfaces for requests and responses
- **Centralized Configuration**: Base URL, timeouts, headers
- **Authentication**: Automatic JWT token injection
- **Error Handling**: Standardized error responses
- **Interceptors**: Request/response transformation
- **Retry Logic**: Automatic retries for failed requests

## Prerequisites

- TypeScript project
- Node.js and npm/pnpm/yarn
- Backend API to communicate with

## Approach 1: Using Axios (Recommended for Complex Apps)

Axios is a popular HTTP client with built-in interceptor support, automatic JSON transformation, and comprehensive error handling.

### Installation

```bash
npm install axios
# or
pnpm add axios
# or
yarn add axios
```

### Basic API Client Setup

Create `lib/api/client.ts`:

```typescript
import axios, { AxiosInstance, AxiosError, AxiosRequestConfig } from 'axios'

// API Configuration
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000/api'
const API_TIMEOUT = 10000 // 10 seconds

// Create Axios instance with base configuration
const apiClient: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
})

export default apiClient
```

### Adding JWT Authentication Interceptor

Add request interceptor to inject JWT tokens:

```typescript
import axios, { AxiosInstance, AxiosError, InternalAxiosRequestConfig } from 'axios'

const apiClient: AxiosInstance = axios.create({
  baseURL: API_BASE_URL,
  timeout: API_TIMEOUT,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request Interceptor - Add JWT token to every request
apiClient.interceptors.request.use(
  (config: InternalAxiosRequestConfig) => {
    // Get token from localStorage, cookies, or your auth state
    const token = localStorage.getItem('authToken')

    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }

    return config
  },
  (error: AxiosError) => {
    return Promise.reject(error)
  }
)

export default apiClient
```

### Error Handling Interceptor

Add response interceptor to handle errors globally:

```typescript
import { toast } from 'sonner' // or your notification library

// Response Interceptor - Handle errors globally
apiClient.interceptors.response.use(
  (response) => {
    // Return successful responses as-is
    return response
  },
  async (error: AxiosError) => {
    // Handle different error types
    if (error.response) {
      // Server responded with error status code
      const status = error.response.status
      const data = error.response.data as any

      switch (status) {
        case 401:
          // Unauthorized - redirect to login
          toast.error('Session expired. Please login again.')
          // Clear auth state
          localStorage.removeItem('authToken')
          // Redirect to login
          window.location.href = '/login'
          break

        case 403:
          // Forbidden
          toast.error('You do not have permission to perform this action.')
          break

        case 404:
          // Not found
          toast.error('Resource not found.')
          break

        case 500:
          // Server error
          toast.error('Server error. Please try again later.')
          break

        default:
          // Other errors
          toast.error(data?.message || 'An error occurred.')
      }
    } else if (error.request) {
      // Request was made but no response received (network error)
      toast.error('Network error. Please check your connection.')
    } else {
      // Error setting up the request
      toast.error('Request failed. Please try again.')
    }

    return Promise.reject(error)
  }
)
```

### Token Refresh Pattern

Handle 401 errors by refreshing tokens:

```typescript
let isRefreshing = false
let failedQueue: Array<{
  resolve: (value?: unknown) => void
  reject: (reason?: any) => void
}> = []

const processQueue = (error: any = null) => {
  failedQueue.forEach((promise) => {
    if (error) {
      promise.reject(error)
    } else {
      promise.resolve()
    }
  })
  failedQueue = []
}

apiClient.interceptors.response.use(
  (response) => response,
  async (error: AxiosError) => {
    const originalRequest = error.config as InternalAxiosRequestConfig & {
      _retry?: boolean
    }

    if (error.response?.status === 401 && !originalRequest._retry) {
      if (isRefreshing) {
        // Queue requests while refreshing
        return new Promise((resolve, reject) => {
          failedQueue.push({ resolve, reject })
        })
          .then(() => {
            return apiClient(originalRequest)
          })
          .catch((err) => {
            return Promise.reject(err)
          })
      }

      originalRequest._retry = true
      isRefreshing = true

      try {
        // Call refresh token endpoint
        const refreshToken = localStorage.getItem('refreshToken')
        const response = await axios.post(`${API_BASE_URL}/auth/refresh`, {
          refreshToken,
        })

        const { token } = response.data

        // Update token
        localStorage.setItem('authToken', token)

        // Update header
        originalRequest.headers.Authorization = `Bearer ${token}`

        // Process queued requests
        processQueue()

        // Retry original request
        return apiClient(originalRequest)
      } catch (refreshError) {
        // Refresh failed - logout user
        processQueue(refreshError)
        localStorage.removeItem('authToken')
        localStorage.removeItem('refreshToken')
        window.location.href = '/login'
        return Promise.reject(refreshError)
      } finally {
        isRefreshing = false
      }
    }

    return Promise.reject(error)
  }
)
```

### Type-Safe API Methods

Create type-safe methods for your API endpoints:

```typescript
// lib/api/types.ts
export interface User {
  id: string
  name: string
  email: string
  role: string
}

export interface LoginRequest {
  email: string
  password: string
}

export interface LoginResponse {
  token: string
  refreshToken: string
  user: User
}

export interface ApiResponse<T> {
  data: T
  message: string
  success: boolean
}

export interface ApiError {
  message: string
  errors?: Record<string, string[]>
}
```

```typescript
// lib/api/auth.ts
import apiClient from './client'
import { LoginRequest, LoginResponse, ApiResponse } from './types'

export const authApi = {
  // Login
  async login(credentials: LoginRequest): Promise<LoginResponse> {
    const response = await apiClient.post<ApiResponse<LoginResponse>>(
      '/auth/login',
      credentials
    )
    return response.data.data
  },

  // Logout
  async logout(): Promise<void> {
    await apiClient.post('/auth/logout')
  },

  // Get current user
  async getCurrentUser(): Promise<User> {
    const response = await apiClient.get<ApiResponse<User>>('/auth/me')
    return response.data.data
  },

  // Refresh token
  async refreshToken(refreshToken: string): Promise<{ token: string }> {
    const response = await apiClient.post<ApiResponse<{ token: string }>>(
      '/auth/refresh',
      { refreshToken }
    )
    return response.data.data
  },
}
```

```typescript
// lib/api/users.ts
import apiClient from './client'
import { User, ApiResponse } from './types'

export const usersApi = {
  // Get all users
  async getAll(): Promise<User[]> {
    const response = await apiClient.get<ApiResponse<User[]>>('/users')
    return response.data.data
  },

  // Get user by ID
  async getById(id: string): Promise<User> {
    const response = await apiClient.get<ApiResponse<User>>(`/users/${id}`)
    return response.data.data
  },

  // Create user
  async create(userData: Omit<User, 'id'>): Promise<User> {
    const response = await apiClient.post<ApiResponse<User>>(
      '/users',
      userData
    )
    return response.data.data
  },

  // Update user
  async update(id: string, userData: Partial<User>): Promise<User> {
    const response = await apiClient.put<ApiResponse<User>>(
      `/users/${id}`,
      userData
    )
    return response.data.data
  },

  // Delete user
  async delete(id: string): Promise<void> {
    await apiClient.delete(`/users/${id}`)
  },
}
```

### Complete Example

```typescript
// lib/api/index.ts
export { default as apiClient } from './client'
export * from './auth'
export * from './users'
export * from './types'
```

Usage in a component:

```typescript
'use client'

import { useState } from 'react'
import { authApi, usersApi, User } from '@/lib/api'

export function LoginForm() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [loading, setLoading] = useState(false)

  const handleLogin = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)

    try {
      const response = await authApi.login({ email, password })

      // Store tokens
      localStorage.setItem('authToken', response.token)
      localStorage.setItem('refreshToken', response.refreshToken)

      // Redirect or update state
      console.log('Logged in:', response.user)
    } catch (error) {
      // Error already handled by interceptor
      console.error('Login failed:', error)
    } finally {
      setLoading(false)
    }
  }

  return (
    <form onSubmit={handleLogin}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
        required
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Password"
        required
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Logging in...' : 'Login'}
      </button>
    </form>
  )
}
```

---

## Approach 2: Using Native Fetch API

For simpler applications or when you prefer native APIs, use the Fetch API with a custom wrapper.

### Installation

No installation needed! Fetch is built into modern browsers and Node.js 18+.

### Basic Fetch Wrapper

Create `lib/api/fetch-client.ts`:

```typescript
// API Configuration
const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000/api'
const API_TIMEOUT = 10000

// Custom error class
export class ApiError extends Error {
  constructor(
    public status: number,
    public statusText: string,
    public data: any
  ) {
    super(`HTTP ${status}: ${statusText}`)
    this.name = 'ApiError'
  }
}

// Request options
interface RequestOptions extends RequestInit {
  timeout?: number
}

// Fetch wrapper with timeout
async function fetchWithTimeout(
  url: string,
  options: RequestOptions = {}
): Promise<Response> {
  const { timeout = API_TIMEOUT, ...fetchOptions } = options

  const controller = new AbortController()
  const timeoutId = setTimeout(() => controller.abort(), timeout)

  try {
    const response = await fetch(url, {
      ...fetchOptions,
      signal: controller.signal,
    })
    clearTimeout(timeoutId)
    return response
  } catch (error) {
    clearTimeout(timeoutId)
    if (error instanceof Error && error.name === 'AbortError') {
      throw new Error('Request timeout')
    }
    throw error
  }
}

// Main API client
class FetchClient {
  private baseURL: string
  private defaultHeaders: HeadersInit

  constructor(baseURL: string) {
    this.baseURL = baseURL
    this.defaultHeaders = {
      'Content-Type': 'application/json',
    }
  }

  // Get auth token
  private getAuthToken(): string | null {
    return localStorage.getItem('authToken')
  }

  // Build headers
  private buildHeaders(customHeaders?: HeadersInit): HeadersInit {
    const token = this.getAuthToken()
    const headers = { ...this.defaultHeaders, ...customHeaders }

    if (token) {
      return {
        ...headers,
        Authorization: `Bearer ${token}`,
      }
    }

    return headers
  }

  // Handle response
  private async handleResponse<T>(response: Response): Promise<T> {
    if (!response.ok) {
      const data = await response.json().catch(() => ({}))
      throw new ApiError(response.status, response.statusText, data)
    }

    // Handle 204 No Content
    if (response.status === 204) {
      return {} as T
    }

    return response.json()
  }

  // GET request
  async get<T>(endpoint: string, options?: RequestOptions): Promise<T> {
    const url = `${this.baseURL}${endpoint}`
    const headers = this.buildHeaders(options?.headers)

    const response = await fetchWithTimeout(url, {
      ...options,
      method: 'GET',
      headers,
    })

    return this.handleResponse<T>(response)
  }

  // POST request
  async post<T>(
    endpoint: string,
    body?: any,
    options?: RequestOptions
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`
    const headers = this.buildHeaders(options?.headers)

    const response = await fetchWithTimeout(url, {
      ...options,
      method: 'POST',
      headers,
      body: JSON.stringify(body),
    })

    return this.handleResponse<T>(response)
  }

  // PUT request
  async put<T>(
    endpoint: string,
    body?: any,
    options?: RequestOptions
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`
    const headers = this.buildHeaders(options?.headers)

    const response = await fetchWithTimeout(url, {
      ...options,
      method: 'PUT',
      headers,
      body: JSON.stringify(body),
    })

    return this.handleResponse<T>(response)
  }

  // DELETE request
  async delete<T>(endpoint: string, options?: RequestOptions): Promise<T> {
    const url = `${this.baseURL}${endpoint}`
    const headers = this.buildHeaders(options?.headers)

    const response = await fetchWithTimeout(url, {
      ...options,
      method: 'DELETE',
      headers,
    })

    return this.handleResponse<T>(response)
  }

  // PATCH request
  async patch<T>(
    endpoint: string,
    body?: any,
    options?: RequestOptions
  ): Promise<T> {
    const url = `${this.baseURL}${endpoint}`
    const headers = this.buildHeaders(options?.headers)

    const response = await fetchWithTimeout(url, {
      ...options,
      method: 'PATCH',
      headers,
      body: JSON.stringify(body),
    })

    return this.handleResponse<T>(response)
  }
}

// Export singleton instance
export const apiClient = new FetchClient(API_BASE_URL)
```

### Error Handling with Fetch

```typescript
// lib/api/error-handler.ts
import { ApiError } from './fetch-client'
import { toast } from 'sonner'

export function handleApiError(error: unknown): void {
  if (error instanceof ApiError) {
    switch (error.status) {
      case 401:
        toast.error('Session expired. Please login again.')
        localStorage.removeItem('authToken')
        window.location.href = '/login'
        break

      case 403:
        toast.error('You do not have permission to perform this action.')
        break

      case 404:
        toast.error('Resource not found.')
        break

      case 422:
        // Validation errors
        const validationErrors = error.data?.errors
        if (validationErrors) {
          Object.values(validationErrors).forEach((messages: any) => {
            messages.forEach((msg: string) => toast.error(msg))
          })
        } else {
          toast.error(error.data?.message || 'Validation failed.')
        }
        break

      case 500:
        toast.error('Server error. Please try again later.')
        break

      default:
        toast.error(error.data?.message || 'An error occurred.')
    }
  } else if (error instanceof Error) {
    if (error.message === 'Request timeout') {
      toast.error('Request timeout. Please try again.')
    } else if (error.message === 'Failed to fetch') {
      toast.error('Network error. Please check your connection.')
    } else {
      toast.error(error.message)
    }
  } else {
    toast.error('An unexpected error occurred.')
  }
}
```

### Type-Safe API Methods with Fetch

```typescript
// lib/api/users.ts
import { apiClient } from './fetch-client'
import { handleApiError } from './error-handler'
import { User, ApiResponse } from './types'

export const usersApi = {
  async getAll(): Promise<User[]> {
    try {
      const response = await apiClient.get<ApiResponse<User[]>>('/users')
      return response.data
    } catch (error) {
      handleApiError(error)
      throw error
    }
  },

  async getById(id: string): Promise<User> {
    try {
      const response = await apiClient.get<ApiResponse<User>>(`/users/${id}`)
      return response.data
    } catch (error) {
      handleApiError(error)
      throw error
    }
  },

  async create(userData: Omit<User, 'id'>): Promise<User> {
    try {
      const response = await apiClient.post<ApiResponse<User>>(
        '/users',
        userData
      )
      return response.data
    } catch (error) {
      handleApiError(error)
      throw error
    }
  },

  async update(id: string, userData: Partial<User>): Promise<User> {
    try {
      const response = await apiClient.put<ApiResponse<User>>(
        `/users/${id}`,
        userData
      )
      return response.data
    } catch (error) {
      handleApiError(error)
      throw error
    }
  },

  async delete(id: string): Promise<void> {
    try {
      await apiClient.delete(`/users/${id}`)
    } catch (error) {
      handleApiError(error)
      throw error
    }
  },
}
```

---

## Approach 3: Using Modern Fetch Wrapper (ofetch)

For the best of both worlds, use `ofetch` - a modern fetch wrapper with interceptor support.

### Installation

```bash
npm install ofetch
# or
pnpm add ofetch
```

### Setup with ofetch

```typescript
// lib/api/client.ts
import { ofetch } from 'ofetch'

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:3000/api'

export const apiClient = ofetch.create({
  baseURL: API_BASE_URL,
  timeout: 10000,
  retry: 3,
  retryDelay: 1000,

  // Request interceptor
  async onRequest({ options }) {
    const token = localStorage.getItem('authToken')
    if (token) {
      options.headers = options.headers || {}
      options.headers.set('Authorization', `Bearer ${token}`)
    }
  },

  // Response interceptor
  async onResponse({ response }) {
    // Log successful responses
    console.log('Response:', response.status)
  },

  // Error interceptor
  async onResponseError({ response, options }) {
    if (response.status === 401) {
      // Try to refresh token
      try {
        const refreshToken = localStorage.getItem('refreshToken')
        const result = await ofetch('/auth/refresh', {
          method: 'POST',
          body: { refreshToken },
        })

        localStorage.setItem('authToken', result.token)

        // Retry original request
        return ofetch(response.url, options)
      } catch (error) {
        // Refresh failed - redirect to login
        localStorage.removeItem('authToken')
        window.location.href = '/login'
      }
    }
  },

  // Request error interceptor
  async onRequestError({ error }) {
    console.error('Request error:', error)
  },
})
```

---

## Best Practices

### 1. Environment Variables

Store API URLs in environment variables:

```env
# .env.local
NEXT_PUBLIC_API_URL=http://localhost:3000/api
```

### 2. Type Safety

Always define TypeScript interfaces for requests and responses:

```typescript
interface CreateUserRequest {
  name: string
  email: string
  password: string
}

interface CreateUserResponse {
  id: string
  name: string
  email: string
  createdAt: string
}
```

### 3. Error Boundaries

Wrap API calls in try-catch blocks or use error boundaries:

```typescript
try {
  const user = await usersApi.create(userData)
  toast.success('User created successfully')
} catch (error) {
  // Error already handled by interceptor
  console.error('Failed to create user:', error)
}
```

### 4. Loading States

Always manage loading states in UI:

```typescript
const [loading, setLoading] = useState(false)

const handleSubmit = async () => {
  setLoading(true)
  try {
    await apiCall()
  } finally {
    setLoading(false)
  }
}
```

### 5. Request Cancellation

Cancel requests when components unmount:

```typescript
useEffect(() => {
  const controller = new AbortController()

  fetchData({ signal: controller.signal })

  return () => {
    controller.abort()
  }
}, [])
```

### 6. Caching Strategy

Consider using React Query or SWR for data fetching with caching:

```typescript
import { useQuery } from '@tanstack/react-query'
import { usersApi } from '@/lib/api'

function UsersList() {
  const { data, isLoading, error } = useQuery({
    queryKey: ['users'],
    queryFn: () => usersApi.getAll(),
  })

  if (isLoading) return <div>Loading...</div>
  if (error) return <div>Error loading users</div>

  return (
    <ul>
      {data?.map((user) => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  )
}
```

---

## Testing API Clients

### Mock API Responses

```typescript
import { vi } from 'vitest'
import { apiClient } from '@/lib/api/client'

vi.mock('@/lib/api/client')

describe('Users API', () => {
  it('should fetch users', async () => {
    const mockUsers = [{ id: '1', name: 'John', email: 'john@example.com' }]

    vi.mocked(apiClient.get).mockResolvedValueOnce({ data: mockUsers })

    const users = await usersApi.getAll()

    expect(users).toEqual(mockUsers)
    expect(apiClient.get).toHaveBeenCalledWith('/users')
  })
})
```

---

## Common Patterns

### File Upload

```typescript
async uploadFile(file: File): Promise<{ url: string }> {
  const formData = new FormData()
  formData.append('file', file)

  const response = await apiClient.post<ApiResponse<{ url: string }>>(
    '/upload',
    formData,
    {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
    }
  )

  return response.data.data
}
```

### Query Parameters

```typescript
async searchUsers(query: string): Promise<User[]> {
  const response = await apiClient.get<ApiResponse<User[]>>('/users', {
    params: { q: query },
  })
  return response.data.data
}
```

### Pagination

```typescript
interface PaginatedResponse<T> {
  data: T[]
  meta: {
    page: number
    perPage: number
    total: number
    totalPages: number
  }
}

async getUsers(page: number = 1): Promise<PaginatedResponse<User>> {
  const response = await apiClient.get<PaginatedResponse<User>>('/users', {
    params: { page, perPage: 20 },
  })
  return response.data
}
```

---

## Troubleshooting

**Issue**: CORS errors
- Solution: Configure CORS on backend or use a proxy

**Issue**: Token not being sent
- Solution: Check localStorage key names and interceptor logic

**Issue**: Network errors
- Solution: Verify API URL and network connection

**Issue**: Type errors
- Solution: Ensure response types match backend API schema

---

## Resources

- Axios Documentation: https://axios-http.com
- Fetch API MDN: https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API
- ofetch Documentation: https://github.com/unjs/ofetch
- TypeScript Handbook: https://www.typescriptlang.org/docs
- React Query: https://tanstack.com/query
