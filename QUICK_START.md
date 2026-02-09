# Quick Start Guide - Phase 2 Todo Application

## ✅ Setup Status

### Frontend (Next.js)
- ✅ Dependencies installed
- ✅ `.env.local` configured
- ✅ Package issue resolved (`better-auth` correctly configured)

### Backend (FastAPI)
- ✅ Virtual environment created
- ✅ All Python dependencies installed
- ✅ `.env` file exists (configure database URL before running)

---

## 🚀 Running the Application

### 1. Start Backend (FastAPI)

```bash
# Navigate to backend directory
cd Phase-2/backend

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On Linux/Mac:
source .venv/bin/activate

# Configure .env file first (edit DATABASE_URL and SECRET_KEY)
# Then run the server
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

**Backend will run on:** `http://localhost:8000`
- API Docs: `http://localhost:8000/docs`
- Health Check: `http://localhost:8000/health`

### 2. Start Frontend (Next.js)

```bash
# Open a NEW terminal
# Navigate to frontend directory
cd Phase-2/frontend

# Run development server
npm run dev
```

**Frontend will run on:** `http://localhost:3000`

---

## 📝 Important Configuration

### Backend (.env)
Before running the backend, update these values in `Phase-2/backend/.env`:

```env
# Change this to a secure random key
SECRET_KEY=your-secure-random-key-here

# Configure your Neon PostgreSQL database URL
DATABASE_URL=postgresql+asyncpg://user:password@your-neon-db-url/tododb
```

To generate a secure SECRET_KEY:
```bash
openssl rand -hex 32
```

### Frontend (.env.local)
Already configured ✅
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## 🧪 Testing the Setup

### 1. Test Backend
```bash
curl http://localhost:8000/health
```
Expected response:
```json
{
  "status": "healthy",
  "service": "Todo Application API",
  "version": "1.0.0"
}
```

### 2. Test Frontend
Open browser: `http://localhost:3000`

---

## 📦 Dependencies Summary

### Frontend
- Next.js 15.1.5
- React 19.0.0
- better-auth 1.1.2 (for authentication)
- Tailwind CSS 3.4.1
- TypeScript 5

### Backend
- FastAPI 0.115.0
- Uvicorn 0.32.0
- SQLModel 0.0.22 (ORM)
- AsyncPG 0.30.0 (PostgreSQL driver)
- Python-Jose 3.3.0 (JWT tokens)
- Passlib 1.7.4 (Password hashing)

---

## 🔧 Troubleshooting

### Issue: Frontend can't connect to backend
- Ensure backend is running on `http://localhost:8000`
- Check `.env.local` has correct `NEXT_PUBLIC_API_URL`

### Issue: Database connection error
- Update `DATABASE_URL` in `Phase-2/backend/.env`
- Ensure Neon PostgreSQL database is accessible
- Run migrations: `alembic upgrade head`

### Issue: Authentication errors
- Ensure `SECRET_KEY` is set in backend `.env`
- Match `BETTER_AUTH_SECRET` between frontend and backend if using Better Auth

---

## 📚 Next Steps

1. Configure Neon PostgreSQL database
2. Run database migrations
3. Test authentication flow
4. Start building features!

---

## 🐛 Known Issues - RESOLVED

### ✅ Package Issue (FIXED)
**Problem:** `@better-auth/react` package doesn't exist
**Solution:** Using correct import from `better-auth` package
**Status:** ✅ Resolved - Dependencies installed correctly

---

Generated: 2026-02-08
