# Quick Start Guide

## ⚡ Fast Setup (5 minutes)

### 1. Backend Setup

```bash
cd Phase-2/backend

# Create & activate virtual environment
uv venv
.venv\Scripts\activate          # Windows
# source .venv/bin/activate     # Linux/Mac

# Install dependencies IN VIRTUAL ENVIRONMENT
uv pip install -r requirements.txt

# Setup environment
cp .env.example .env
# Edit .env with your database URL

# Run server (with venv active)
uvicorn main:app --reload
```

**✅ Backend running on http://localhost:8000**

### 2. Frontend Setup

```bash
cd Phase-2/frontend

# Install dependencies in LOCAL node_modules
npm install

# Setup environment
cp .env.example .env.local

# Run server
npm run dev
```

**✅ Frontend running on http://localhost:3000**

## 🎯 Daily Development Workflow

### Start Working

```bash
# Terminal 1 - Backend
cd Phase-2/backend
.venv\Scripts\activate          # ⚠️ ALWAYS activate venv first!
uvicorn main:app --reload

# Terminal 2 - Frontend
cd Phase-2/frontend
npm run dev
```

### Stop Working

```bash
# Ctrl+C to stop servers
# Then deactivate virtual environment
deactivate
```

## ✅ Verify Setup

**Check virtual environment is active:**
```bash
# Your prompt should show (.venv)
# Example: (.venv) PS C:\...\backend>
```

**Check packages are in venv (not global):**
```bash
which python    # Should show: Phase-2/backend/.venv/Scripts/python
pip list        # Should show: fastapi, sqlmodel, etc.
```

## 🚨 Common Mistakes to Avoid

❌ **DON'T**: Run `pip install` without activating venv
❌ **DON'T**: Install packages globally
❌ **DON'T**: Use `npm install -g` for project dependencies

✅ **DO**: Always activate `.venv` before backend work
✅ **DO**: Install Python packages in virtual environment
✅ **DO**: Install npm packages locally (automatic with `npm install`)

## 📁 What Gets Created

```
Phase-2/
├── backend/
│   └── .venv/          ← Virtual environment (LOCAL, in .gitignore)
└── frontend/
    └── node_modules/   ← Node packages (LOCAL, in .gitignore)
```

## 🔧 Installation Commands Summary

| What | Where | Command |
|------|-------|---------|
| Python packages | backend/.venv | `uv pip install -r requirements.txt` |
| Node packages | frontend/node_modules | `npm install` |
| Backend server | backend | `uvicorn main:app --reload` |
| Frontend server | frontend | `npm run dev` |

---

**Remember**: Always activate virtual environment before backend work! 🎯
