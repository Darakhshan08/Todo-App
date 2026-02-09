# API Documentation - Todo Application

**Version**: 1.0.0
**Base URL**: `http://localhost:8000`
**Authentication**: JWT Bearer Token

---

## Authentication Endpoints

### POST /api/auth/signup

Register a new user account.

**Request Body**:
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "SecurePassword123!"
}
```

**Response** (201 Created):
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": "user-uuid",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

**Error Responses**:
- `400 Bad Request`: Invalid input data
- `409 Conflict`: Email already registered

---

### POST /api/auth/login

Authenticate and receive JWT token.

**Request Body**:
```json
{
  "email": "user@example.com",
  "password": "SecurePassword123!"
}
```

**Response** (200 OK):
```json
{
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "user": {
    "id": "user-uuid",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid credentials
- `404 Not Found`: User not found

---

### POST /api/auth/logout

Logout current user (client-side token removal).

**Headers**:
```
Authorization: Bearer <token>
```

**Response** (200 OK):
```json
{
  "status": "logged out"
}
```

---

## Task Management Endpoints

All task endpoints require JWT authentication via `Authorization: Bearer <token>` header.

### GET /api/{user_id}/tasks

Retrieve all tasks for authenticated user with filtering and sorting.

**Path Parameters**:
- `user_id` (string): User ID (must match authenticated user)

**Query Parameters**:
- `status` (string, optional): Filter by status - `all`, `pending`, `completed` (default: `all`)
- `priority` (string, optional): Filter by priority - `high`, `medium`, `low`
- `tag` (string, optional): Filter by tag (e.g., `work`, `home`)
- `search` (string, optional): Search keyword in title or description
- `sort` (string, optional): Sort by - `created`, `updated`, `title`, `priority` (default: `created`)
- `skip` (number, optional): Pagination offset (default: 0)
- `limit` (number, optional): Max results per page (default: 100, max: 1000)

**Example Request**:
```
GET /api/user-123/tasks?status=pending&priority=high&sort=priority
```

**Response** (200 OK):
```json
[
  {
    "id": 1,
    "user_id": "user-123",
    "title": "Complete project documentation",
    "description": "Write API docs and setup guide",
    "completed": false,
    "priority": "high",
    "tags": ["work", "documentation"],
    "created_at": "2026-02-08T10:00:00Z",
    "updated_at": "2026-02-08T10:00:00Z"
  }
]
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing token
- `403 Forbidden`: user_id doesn't match authenticated user

---

### POST /api/{user_id}/tasks

Create a new task.

**Path Parameters**:
- `user_id` (string): User ID (must match authenticated user)

**Request Body**:
```json
{
  "title": "Complete project documentation",
  "description": "Write API docs and setup guide",
  "priority": "high",
  "tags": ["work", "documentation"]
}
```

**Field Constraints**:
- `title` (required): 1-200 characters
- `description` (optional): Max 1000 characters
- `priority` (optional): `high`, `medium`, or `low` (default: `medium`)
- `tags` (optional): Array of strings

**Response** (201 Created):
```json
{
  "id": 1,
  "user_id": "user-123",
  "title": "Complete project documentation",
  "description": "Write API docs and setup guide",
  "completed": false,
  "priority": "high",
  "tags": ["work", "documentation"],
  "created_at": "2026-02-08T10:00:00Z",
  "updated_at": "2026-02-08T10:00:00Z"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid input (title too long, etc.)
- `401 Unauthorized`: Invalid or missing token
- `403 Forbidden`: user_id doesn't match authenticated user

---

### PUT /api/{user_id}/tasks/{id}

Update an existing task.

**Path Parameters**:
- `user_id` (string): User ID (must match authenticated user)
- `id` (number): Task ID

**Request Body** (all fields optional):
```json
{
  "title": "Updated task title",
  "description": "Updated description",
  "completed": true,
  "priority": "medium",
  "tags": ["work", "updated"]
}
```

**Response** (200 OK):
```json
{
  "id": 1,
  "user_id": "user-123",
  "title": "Updated task title",
  "description": "Updated description",
  "completed": true,
  "priority": "medium",
  "tags": ["work", "updated"],
  "created_at": "2026-02-08T10:00:00Z",
  "updated_at": "2026-02-08T11:30:00Z"
}
```

**Error Responses**:
- `400 Bad Request`: Invalid input
- `401 Unauthorized`: Invalid or missing token
- `403 Forbidden`: user_id doesn't match authenticated user
- `404 Not Found`: Task not found

---

### DELETE /api/{user_id}/tasks/{id}

Delete a task.

**Path Parameters**:
- `user_id` (string): User ID (must match authenticated user)
- `id` (number): Task ID

**Response** (200 OK):
```json
{
  "status": "deleted",
  "task_id": 1
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing token
- `403 Forbidden`: user_id doesn't match authenticated user
- `404 Not Found`: Task not found

---

### PATCH /api/{user_id}/tasks/{id}/complete

Toggle task completion status.

**Path Parameters**:
- `user_id` (string): User ID (must match authenticated user)
- `id` (number): Task ID

**Response** (200 OK):
```json
{
  "task_id": 1,
  "completed": true,
  "title": "Complete project documentation"
}
```

**Error Responses**:
- `401 Unauthorized`: Invalid or missing token
- `403 Forbidden`: user_id doesn't match authenticated user
- `404 Not Found`: Task not found

---

## Error Response Format

All error responses follow this structure:

```json
{
  "detail": "Error message describing what went wrong"
}
```

**Common HTTP Status Codes**:
- `200 OK`: Request successful
- `201 Created`: Resource created successfully
- `400 Bad Request`: Invalid input data
- `401 Unauthorized`: Authentication required or token invalid
- `403 Forbidden`: User not authorized for this resource
- `404 Not Found`: Resource not found
- `409 Conflict`: Resource already exists
- `422 Unprocessable Entity`: Validation error
- `500 Internal Server Error`: Server error

---

## Rate Limiting

**Limits**:
- Authentication endpoints: 5 requests per minute
- Task endpoints: 60 requests per minute per user

**Response Headers**:
```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1675862400
```

When rate limit exceeded, returns `429 Too Many Requests`:
```json
{
  "detail": "Rate limit exceeded. Try again in 30 seconds."
}
```

---

## Authentication Flow

1. **Sign Up**: POST `/api/auth/signup` → Receive JWT token
2. **Login**: POST `/api/auth/login` → Receive JWT token
3. **Use API**: Include `Authorization: Bearer <token>` in all task requests
4. **Logout**: POST `/api/auth/logout` + Clear token from client storage

**Token Storage** (Frontend):
```javascript
// Store token
localStorage.setItem('auth_token', token);

// Retrieve token for API calls
const token = localStorage.getItem('auth_token');
fetch('/api/user-123/tasks', {
  headers: {
    'Authorization': `Bearer ${token}`
  }
});
```

---

## Interactive API Documentation

Visit `http://localhost:8000/docs` for interactive Swagger UI documentation where you can:
- Explore all endpoints
- Test API calls directly
- View request/response schemas
- Try authentication flows

---

**Last Updated**: 2026-02-08
**Status**: Production Ready
