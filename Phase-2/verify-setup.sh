#!/bin/bash
# Setup Verification Script
# Run this to verify your development environment is ready

echo "=================================================="
echo "  Todo App Phase 2 - Setup Verification"
echo "=================================================="
echo ""

ERRORS=0

# Check Backend
echo "📦 Checking Backend..."
cd backend 2>/dev/null || { echo "❌ backend/ directory not found"; ERRORS=$((ERRORS+1)); }

if [ -d ".venv" ]; then
    echo "✅ Virtual environment exists"
else
    echo "❌ Virtual environment not found. Run: uv venv"
    ERRORS=$((ERRORS+1))
fi

if [ -f "requirements.txt" ]; then
    echo "✅ requirements.txt exists"
else
    echo "❌ requirements.txt not found"
    ERRORS=$((ERRORS+1))
fi

if [ -f ".env" ]; then
    echo "✅ .env file exists"
else
    echo "⚠️  .env file not found. Copy from .env.example"
    ERRORS=$((ERRORS+1))
fi

if [ -f "main.py" ]; then
    echo "✅ main.py exists"
else
    echo "❌ main.py not found"
    ERRORS=$((ERRORS+1))
fi

cd ..

# Check Frontend
echo ""
echo "🎨 Checking Frontend..."
cd frontend 2>/dev/null || { echo "❌ frontend/ directory not found"; ERRORS=$((ERRORS+1)); }

if [ -d "node_modules" ]; then
    echo "✅ node_modules exists"
else
    echo "❌ node_modules not found. Run: npm install"
    ERRORS=$((ERRORS+1))
fi

if [ -f "package.json" ]; then
    echo "✅ package.json exists"
else
    echo "❌ package.json not found"
    ERRORS=$((ERRORS+1))
fi

if [ -f ".env.local" ]; then
    echo "✅ .env.local file exists"
else
    echo "⚠️  .env.local file not found. Copy from .env.example"
    ERRORS=$((ERRORS+1))
fi

cd ..

# Final Report
echo ""
echo "=================================================="
if [ $ERRORS -eq 0 ]; then
    echo "✅ ALL CHECKS PASSED!"
    echo "   You're ready to start development"
    echo ""
    echo "Next steps:"
    echo "1. Terminal 1: cd backend && .venv/Scripts/activate && uvicorn main:app --reload"
    echo "2. Terminal 2: cd frontend && npm run dev"
    echo "3. Visit: http://localhost:3000"
else
    echo "❌ FOUND $ERRORS ISSUE(S)"
    echo "   Please fix the issues above before starting"
    echo "   See SETUP.md for detailed instructions"
fi
echo "=================================================="
