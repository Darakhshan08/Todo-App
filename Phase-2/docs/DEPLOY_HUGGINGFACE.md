# Deployment Guide - Hugging Face Spaces

**Target Platform**: Hugging Face Spaces
**App Type**: Full-Stack Todo Application
**Deployment Strategy**: Backend on HF Spaces (Docker), Frontend on Vercel or HF Static

---

## Overview

Hugging Face Spaces supports deploying applications using:
- **Docker containers** (for FastAPI backend) ✅ Recommended
- **Static sites** (for Next.js frontend) ✅ Alternative
- **Gradio/Streamlit** (not applicable for this app)

**Recommended Architecture**:
```
Frontend (Vercel) → Backend (HF Spaces) → Database (Neon)
```

**Alternative Architecture**:
```
Frontend (HF Static) → Backend (HF Spaces) → Database (Neon)
```

---

## Part 1: Backend Deployment to Hugging Face Spaces

### 1.1 Create Dockerfile for Backend

Create `Phase-2/backend/Dockerfile`:

```dockerfile
FROM python:3.13-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port (Hugging Face uses 7860 by default)
EXPOSE 7860

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:7860/health')"

# Run application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
```

### 1.2 Create README.md for Hugging Face

Create `Phase-2/backend/README.md`:

```markdown
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

FastAPI backend for a modern full-stack Todo application with user authentication and task management.

## Features

- 🔐 JWT Authentication
- 📝 Full CRUD operations for tasks
- 🏷️ Priority levels and tags
- 🔍 Search and filter functionality
- 📊 RESTful API design
- 🗃️ PostgreSQL database integration

## API Documentation

Once deployed, visit `/docs` for interactive Swagger UI documentation.

## Endpoints

- `POST /api/auth/signup` - User registration
- `POST /api/auth/login` - User authentication
- `GET /api/{user_id}/tasks` - List tasks (with filters)
- `POST /api/{user_id}/tasks` - Create task
- `PUT /api/{user_id}/tasks/{id}` - Update task
- `DELETE /api/{user_id}/tasks/{id}` - Delete task
- `PATCH /api/{user_id}/tasks/{id}/complete` - Toggle completion

## Environment Variables

Required environment variables (set in Hugging Face Space settings):

- `DATABASE_URL` - PostgreSQL connection string (from Neon)
- `BETTER_AUTH_SECRET` - JWT signing secret
- `SECRET_KEY` - Additional auth secret
- `BACKEND_CORS_ORIGINS` - Allowed frontend origins (comma-separated)

## Tech Stack

- FastAPI 0.115.0
- SQLModel 0.0.22
- Neon PostgreSQL
- JWT Authentication
- Async/await operations
```

### 1.3 Create .dockerignore

Create `Phase-2/backend/.dockerignore`:

```
.venv/
__pycache__/
*.pyc
*.pyo
*.pyd
.Python
*.so
.env
.env.local
.git/
.gitignore
*.md
.vscode/
.idea/
*.log
tests/
.pytest_cache/
```

### 1.4 Deploy Backend to Hugging Face

**Method 1: Web Interface (Recommended)**

1. Go to https://huggingface.co/spaces
2. Click "Create new Space"
3. Configure:
   - **Space name**: `todo-app-backend`
   - **License**: MIT
   - **SDK**: Docker
   - **Hardware**: CPU basic (free)

4. After creation:
   - Upload `Dockerfile`
   - Upload `requirements.txt`
   - Upload all `.py` files from `src/`
   - Upload `main.py`
   - Upload `README.md`

5. Go to Settings → Environment Variables:
   ```
   DATABASE_URL=postgresql+asyncpg://user:pass@host/db?sslmode=require
   BETTER_AUTH_SECRET=your-secret-here
   SECRET_KEY=your-jwt-secret-here
   BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
   ```

6. Space will auto-deploy on file upload

**Method 2: Git Push**

```bash
# Navigate to backend
cd Phase-2/backend

# Initialize git (if not already)
git init

# Add Hugging Face remote
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/todo-app-backend

# Add files
git add Dockerfile requirements.txt main.py src/ README.md

# Commit
git commit -m "Initial backend deployment"

# Push to Hugging Face
git push hf main
```

### 1.5 Verify Backend Deployment

1. Wait for Space to build (2-3 minutes)
2. Visit: `https://YOUR_USERNAME-todo-app-backend.hf.space/health`
3. Expected response:
   ```json
   {
     "status": "healthy",
     "service": "Todo Application API",
     "version": "1.0.0"
   }
   ```

4. Visit API docs: `https://YOUR_USERNAME-todo-app-backend.hf.space/docs`

---

## Part 2: Frontend Deployment Options

### Option A: Keep Frontend on Vercel (Recommended)

**Pros**:
- Optimized for Next.js
- Automatic edge deployment
- Better performance
- Free tier generous

**Setup**:
1. Deploy frontend to Vercel (see `DEPLOYMENT.md`)
2. Update `.env.production`:
   ```
   NEXT_PUBLIC_API_URL=https://YOUR_USERNAME-todo-app-backend.hf.space
   ```
3. Redeploy frontend

### Option B: Deploy Frontend to Hugging Face (Static Export)

**Note**: Next.js App Router requires static export configuration.

1. Update `Phase-2/frontend/next.config.js`:
   ```javascript
   /** @type {import('next').NextConfig} */
   const nextConfig = {
     output: 'export',
     images: {
       unoptimized: true
     },
     trailingSlash: true,
   }

   module.exports = nextConfig
   ```

2. Build static export:
   ```bash
   cd Phase-2/frontend
   npm run build
   # Creates 'out/' directory with static files
   ```

3. Create Hugging Face Space for frontend:
   - SDK: Static
   - Upload all files from `out/` directory

4. **Limitation**: Static export doesn't support:
   - Server-side rendering (SSR)
   - API routes
   - Image optimization
   - Incremental Static Regeneration (ISR)

**Recommendation**: Use Vercel for frontend, Hugging Face for backend only.

---

## Part 3: Environment Variables Management

### Backend Variables (Hugging Face Space Settings)

```bash
# Database (Neon PostgreSQL)
DATABASE_URL=postgresql+asyncpg://user:password@ep-xxx.neon.tech/neondb?sslmode=require

# Authentication Secrets
BETTER_AUTH_SECRET=<generate with: openssl rand -hex 32>
SECRET_KEY=<generate with: openssl rand -hex 32>

# CORS (allow frontend)
BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app,https://your-hf-frontend.hf.space
```

### Frontend Variables (.env.production)

```bash
# Backend API URL (Hugging Face Space URL)
NEXT_PUBLIC_API_URL=https://YOUR_USERNAME-todo-app-backend.hf.space

# Same secret as backend
BETTER_AUTH_SECRET=<same-as-backend-secret>
```

---

## Part 4: Post-Deployment Configuration

### 4.1 Update CORS Settings

After frontend deployment, update backend CORS:

1. Go to Hugging Face Space Settings
2. Update `BACKEND_CORS_ORIGINS`:
   ```
   https://your-actual-frontend.vercel.app
   ```
3. Space will automatically redeploy

### 4.2 Test Full Flow

1. Visit frontend URL
2. Sign up with test account
3. Create a task
4. Verify task appears
5. Test all CRUD operations
6. Check Network tab for API calls

---

## Part 5: Hugging Face Spaces Limitations

### Resource Limits (Free Tier)

- **CPU**: 2 vCPU
- **RAM**: 16 GB
- **Storage**: 50 GB
- **Sleep**: Inactive spaces sleep after 48 hours
- **Build time**: 1 hour max

### Sleep Behavior

Free Spaces sleep after 48 hours of inactivity:
- First request after sleep takes 30-60 seconds
- Solution: Upgrade to persistent hardware ($0.60/month)

### Database

Hugging Face doesn't provide databases:
- **Must use external database** (Neon, Supabase, etc.)
- Already configured for Neon PostgreSQL ✅

---

## Part 6: Monitoring and Logs

### View Logs

**Web Interface**:
1. Go to your Space
2. Click "Logs" tab
3. See real-time application logs

**API**:
```bash
# View Space logs
curl -H "Authorization: Bearer $HF_TOKEN" \
  https://huggingface.co/api/spaces/YOUR_USERNAME/todo-app-backend/logs
```

### Health Monitoring

Set up external monitoring:
```bash
# UptimeRobot configuration
URL: https://YOUR_USERNAME-todo-app-backend.hf.space/health
Method: GET
Interval: 5 minutes
Expected: {"status":"healthy"}
```

---

## Part 7: Custom Domain (Optional)

Hugging Face Spaces support custom domains:

1. Go to Space Settings → Domain
2. Add custom domain: `api.yourdomain.com`
3. Configure DNS:
   ```
   CNAME api.yourdomain.com → YOUR_USERNAME-todo-app-backend.hf.space
   ```
4. Wait for DNS propagation (up to 24 hours)

---

## Part 8: Troubleshooting

### Issue: Space Keeps Rebuilding

**Cause**: Docker build failures
**Solution**:
```bash
# Test Dockerfile locally
cd Phase-2/backend
docker build -t todo-backend .
docker run -p 7860:7860 --env-file .env todo-backend
```

### Issue: 500 Internal Server Error

**Cause**: Missing environment variables
**Solution**:
1. Check Space Settings → Environment Variables
2. Verify all required variables are set
3. Check logs for specific error

### Issue: CORS Errors

**Cause**: Frontend URL not in CORS origins
**Solution**:
```bash
# Update BACKEND_CORS_ORIGINS to include exact frontend URL
BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
# No trailing slash, exact match required
```

### Issue: Database Connection Failed

**Cause**: Invalid DATABASE_URL or network issues
**Solution**:
1. Verify Neon database is active
2. Check connection string format:
   ```
   postgresql+asyncpg://user:pass@host/db?sslmode=require
   ```
3. Ensure Neon allows connections from Hugging Face IPs (usually allowed)

---

## Part 9: Cost Comparison

| Platform | Backend | Frontend | Database | Total/Month |
|----------|---------|----------|----------|-------------|
| **HF + Vercel + Neon** | Free | Free | Free | $0 |
| **HF Persistent** | $0.60 | Free | Free | $0.60 |
| **Railway + Vercel + Neon** | $5 | Free | Free | $5 |
| **Render + Vercel + Neon** | $7 | Free | Free | $7 |

**Recommendation**: Start with free tier, upgrade to persistent if sleep is an issue.

---

## Part 10: Deployment Checklist

### Backend Deployment
- [ ] Create Dockerfile
- [ ] Create README.md with frontmatter
- [ ] Create .dockerignore
- [ ] Set up Neon PostgreSQL database
- [ ] Create Hugging Face Space (Docker SDK)
- [ ] Upload backend files
- [ ] Set environment variables in HF Space settings
- [ ] Wait for build to complete
- [ ] Test /health endpoint
- [ ] Test /docs endpoint
- [ ] Verify database connection

### Frontend Deployment
- [ ] Deploy to Vercel (recommended)
- [ ] OR create static export for HF
- [ ] Update NEXT_PUBLIC_API_URL
- [ ] Test frontend-backend connection
- [ ] Update backend CORS with actual frontend URL

### Post-Deployment
- [ ] Test user signup
- [ ] Test user login
- [ ] Test task CRUD operations
- [ ] Test search and filter
- [ ] Verify user isolation
- [ ] Set up monitoring (optional)
- [ ] Configure custom domain (optional)

---

## Quick Deploy Commands

```bash
# 1. Prepare backend for HF
cd Phase-2/backend
cat > Dockerfile << 'EOF'
FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 7860
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]
EOF

# 2. Create .dockerignore
cat > .dockerignore << 'EOF'
.venv/
__pycache__/
*.pyc
.env
.git/
EOF

# 3. Test locally with Docker
docker build -t todo-backend .
docker run -p 7860:7860 --env-file .env todo-backend

# 4. Push to Hugging Face (after creating Space)
git init
git remote add hf https://huggingface.co/spaces/YOUR_USERNAME/todo-app-backend
git add .
git commit -m "Deploy backend to Hugging Face"
git push hf main
```

---

## Resources

- **Hugging Face Spaces**: https://huggingface.co/docs/hub/spaces
- **Docker Spaces Guide**: https://huggingface.co/docs/hub/spaces-sdks-docker
- **Spaces Config**: https://huggingface.co/docs/hub/spaces-config-reference
- **Neon PostgreSQL**: https://neon.tech/docs

---

**Last Updated**: 2026-02-08
**Status**: Ready for Deployment
