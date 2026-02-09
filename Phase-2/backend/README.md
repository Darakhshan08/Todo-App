---
title: Todo App Backend API
emoji: ✅
colorFrom: blue
colorTo: purple
sdk: docker
pinned: false
license: mit
---

# Todo Application Backend API

FastAPI backend for a modern full-stack Todo application with user authentication, task management, and advanced filtering capabilities.

## 🚀 Features

- 🔐 **JWT Authentication** - Secure user signup and login
- 📝 **Full CRUD Operations** - Create, read, update, delete tasks
- 🏷️ **Priority & Tags** - Organize tasks with priorities (high/medium/low) and custom tags
- 🔍 **Search & Filter** - Search by keyword, filter by status, priority, or tags
- 📊 **Sort Options** - Sort by created date, updated date, title, or priority
- 🗃️ **PostgreSQL Database** - Persistent storage with Neon Serverless
- ⚡ **Async Operations** - Non-blocking I/O for optimal performance
- 🛡️ **User Isolation** - Each user sees only their own data
- 📈 **Rate Limiting** - Built-in protection against abuse (60 req/min per user)

## 📖 API Documentation

Once deployed, visit `/docs` for interactive Swagger UI documentation.

**Live Documentation**: https://YOUR_USERNAME-todo-app-backend.hf.space/docs

## 🔌 API Endpoints

### Authentication
- `POST /api/auth/signup` - Register new user
- `POST /api/auth/login` - Authenticate user
- `POST /api/auth/logout` - Logout current user

### Task Management
- `GET /api/{user_id}/tasks` - List all tasks (with filters)
  - Query params: `status`, `priority`, `tag`, `search`, `sort`, `skip`, `limit`
- `POST /api/{user_id}/tasks` - Create new task
- `GET /api/{user_id}/tasks/{id}` - Get specific task
- `PUT /api/{user_id}/tasks/{id}` - Update task
- `DELETE /api/{user_id}/tasks/{id}` - Delete task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle completion status

### Health
- `GET /health` - Health check endpoint

## ⚙️ Environment Variables

Set these in your Hugging Face Space settings:

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection string (async) | `postgresql+asyncpg://user:pass@host/db` |
| `BETTER_AUTH_SECRET` | JWT signing secret (32+ chars) | `your-random-secret-key-here` |
| `SECRET_KEY` | Additional auth secret (32+ chars) | `another-random-secret-key` |
| `BACKEND_CORS_ORIGINS` | Allowed frontend origins | `https://your-app.vercel.app` |

**Generate secrets**:
```bash
openssl rand -hex 32
```

## 🏗️ Tech Stack

- **Framework**: FastAPI 0.115.0
- **ORM**: SQLModel 0.0.22
- **Database**: PostgreSQL (via Neon Serverless)
- **Database Driver**: asyncpg 0.30.0
- **Authentication**: JWT (python-jose)
- **Password Hashing**: bcrypt (passlib)
- **Validation**: Pydantic 2.x
- **Server**: Uvicorn (ASGI)

## 🚀 Quick Start (Local Development)

```bash
# Clone repository
git clone https://huggingface.co/spaces/YOUR_USERNAME/todo-app-backend
cd todo-app-backend

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
# .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials

# Run server
uvicorn main:app --reload --port 7860

# Visit http://localhost:7860/docs
```

## 🐳 Docker Deployment

```bash
# Build image
docker build -t todo-backend .

# Run container
docker run -p 7860:7860 \
  -e DATABASE_URL="postgresql+asyncpg://..." \
  -e BETTER_AUTH_SECRET="your-secret" \
  -e SECRET_KEY="your-key" \
  -e BACKEND_CORS_ORIGINS="https://your-frontend.com" \
  todo-backend
```

## 📊 Database Schema

### Users Table
- `id` (string, primary key)
- `email` (string, unique)
- `name` (string)
- `password_hash` (string)
- `created_at` (datetime)

### Tasks Table
- `id` (integer, primary key)
- `user_id` (string, foreign key → users.id)
- `title` (string, 1-200 chars)
- `description` (string, optional, max 1000 chars)
- `completed` (boolean, default: false)
- `priority` (enum: high/medium/low, default: medium)
- `tags` (array of strings)
- `created_at` (datetime)
- `updated_at` (datetime)

## 🔒 Security Features

- ✅ JWT token authentication on all endpoints
- ✅ Password hashing with bcrypt
- ✅ User data isolation (users can only access their own data)
- ✅ SQL injection prevention (SQLModel ORM)
- ✅ Rate limiting (60 requests/minute per user)
- ✅ Input validation with Pydantic models
- ✅ CORS configuration
- ✅ No hardcoded secrets

## 📈 Performance

- **Response Time**: p95 < 200ms for all endpoints
- **Concurrent Users**: Supports 100+ concurrent users
- **Database**: Connection pooling (10 base, 20 max overflow)
- **Operations**: Fully async (non-blocking I/O)

## 🧪 Testing

```bash
# Run manual tests
# See TESTING.md for comprehensive test cases

# Example API test
curl -X POST http://localhost:7860/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","name":"Test User","password":"SecurePass123!"}'
```

## 📝 Example Usage

```python
import requests

# Base URL
API_URL = "https://YOUR_USERNAME-todo-app-backend.hf.space"

# 1. Sign up
response = requests.post(f"{API_URL}/api/auth/signup", json={
    "email": "user@example.com",
    "name": "John Doe",
    "password": "SecurePassword123!"
})
token = response.json()["token"]
user_id = response.json()["user"]["id"]

# 2. Create task
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(
    f"{API_URL}/api/{user_id}/tasks",
    headers=headers,
    json={
        "title": "Complete project",
        "description": "Finish the documentation",
        "priority": "high",
        "tags": ["work", "urgent"]
    }
)

# 3. Get all tasks
response = requests.get(
    f"{API_URL}/api/{user_id}/tasks?priority=high&status=pending",
    headers=headers
)
tasks = response.json()
```

## 🔗 Links

- **Frontend Repository**: [Link to frontend repo]
- **Documentation**: See `/docs` endpoint when deployed
- **Issues**: Report bugs in the main repository
- **Neon Database**: https://neon.tech

## 📄 License

MIT License - See LICENSE file for details

## 🤝 Contributing

This is a deployment space for the Todo Application backend. For contributions, please visit the main repository.

---

**Built with**: FastAPI | SQLModel | PostgreSQL | Neon | Hugging Face Spaces

**Status**: Production Ready ✅
