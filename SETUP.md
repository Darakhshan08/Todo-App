# Setup Instructions - Todo Application Phase 2

## Prerequisites

- Python 3.13+
- Node.js 18+
- UV (Python package manager)
- Git

## Backend Setup (Python Virtual Environment)

### 1. Navigate to Backend Directory

```bash
cd Phase-2/backend
```

### 2. Create Virtual Environment with UV

```bash
# Create virtual environment
uv venv

# This creates a .venv directory
```

### 3. Activate Virtual Environment

**Windows:**
```bash
.venv\Scripts\activate
```

**Linux/Mac:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies (Inside Virtual Environment)

```bash
# Make sure your prompt shows (.venv) indicating virtual environment is active
uv pip install -r requirements.txt
```

### 5. Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env

# Edit .env file with your configuration:
# - DATABASE_URL (Neon PostgreSQL connection string)
# - BETTER_AUTH_SECRET (shared secret with frontend)
# - BACKEND_CORS_ORIGINS (frontend URL)
```

### 6. Run Backend Server (Inside Virtual Environment)

```bash
# Make sure (.venv) is active
uvicorn main:app --reload
```

Backend will be available at: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Frontend Setup (Node.js)

### 1. Navigate to Frontend Directory

```bash
cd Phase-2/frontend
```

### 2. Install Dependencies (Local node_modules)

```bash
# This installs dependencies in node_modules/ directory (NOT globally)
npm install
```

### 3. Configure Environment Variables

```bash
# Copy example env file
cp .env.example .env.local

# Edit .env.local with your configuration:
# - NEXT_PUBLIC_API_URL=http://localhost:8000
# - BETTER_AUTH_SECRET (same as backend)
```

### 4. Run Frontend Server

```bash
npm run dev
```

Frontend will be available at: http://localhost:3000

## Verification

### Check Backend (in virtual environment)

```bash
# Terminal 1 - Make sure (.venv) is active
cd Phase-2/backend
.venv\Scripts\activate  # Windows
# OR
source .venv/bin/activate  # Linux/Mac

# Verify Python packages are installed in virtual environment
which python  # Should point to .venv/bin/python
pip list  # Should show fastapi, sqlmodel, etc.

# Run server
uvicorn main:app --reload
```

### Check Frontend (local node_modules)

```bash
# Terminal 2
cd Phase-2/frontend

# Verify node_modules exists locally
ls -la node_modules/  # Should show installed packages

# Run dev server
npm run dev
```

## Important Notes

### ✅ DO:
- ✅ Always activate virtual environment before working with backend
- ✅ Install Python packages using `uv pip install` (NOT `pip install` globally)
- ✅ Install npm packages using `npm install` (automatically installs in local node_modules)
- ✅ Keep virtual environment (.venv) and node_modules in .gitignore

### ❌ DON'T:
- ❌ Don't install Python packages globally without virtual environment
- ❌ Don't use `npm install -g` for project dependencies
- ❌ Don't commit .venv/ or node_modules/ to git

## Deactivate Virtual Environment

When you're done working:

```bash
# Deactivate Python virtual environment
deactivate
```

## Troubleshooting

### Backend Issues

**Problem**: "Module not found" error
**Solution**:
```bash
# Activate virtual environment first
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac

# Reinstall dependencies
uv pip install -r requirements.txt
```

**Problem**: "uvicorn not found"
**Solution**: Make sure virtual environment is active and uvicorn is installed
```bash
.venv\Scripts\activate
uv pip install uvicorn
```

### Frontend Issues

**Problem**: "Module not found" in Next.js
**Solution**:
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install
```

**Problem**: "clsx" or "tailwind-merge" not found
**Solution**: Install the new dependencies
```bash
npm install clsx tailwind-merge
```

## Directory Structure After Setup

```
Phase-2/
├── backend/
│   ├── .venv/                    # ✅ Virtual environment (local, not in git)
│   ├── src/
│   ├── requirements.txt
│   ├── .env                      # ✅ Your local config (not in git)
│   └── main.py
├── frontend/
│   ├── node_modules/             # ✅ Local packages (not in git)
│   ├── src/
│   ├── package.json
│   └── .env.local                # ✅ Your local config (not in git)
└── docker-compose.yml
```

## Quick Start Commands

```bash
# Terminal 1 - Backend
cd Phase-2/backend
.venv\Scripts\activate  # Activate venv first!
uvicorn main:app --reload

# Terminal 2 - Frontend
cd Phase-2/frontend
npm run dev

# Visit: http://localhost:3000
```

## Database Setup (Neon PostgreSQL)

1. Create account at https://neon.tech
2. Create a new project
3. Copy the connection string
4. Add to `Phase-2/backend/.env`:
   ```
   DATABASE_URL=postgresql+asyncpg://[user]:[password]@[host]/[database]
   ```

## Testing the Setup

1. Backend health check: http://localhost:8000/health
2. Frontend: http://localhost:3000
3. Sign up for an account
4. Create a task
5. Verify task appears in list

---

**Last Updated**: 2026-02-08
**Status**: Ready for Development
