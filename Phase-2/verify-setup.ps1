# Setup Verification Script for Windows
# Run this to verify your development environment is ready

Write-Host "==================================================" -ForegroundColor Cyan
Write-Host "  Todo App Phase 2 - Setup Verification" -ForegroundColor Cyan
Write-Host "==================================================" -ForegroundColor Cyan
Write-Host ""

$ERRORS = 0

# Check Backend
Write-Host "📦 Checking Backend..." -ForegroundColor Yellow
if (Test-Path "backend") {
    Push-Location backend

    if (Test-Path ".venv") {
        Write-Host "✅ Virtual environment exists" -ForegroundColor Green
    } else {
        Write-Host "❌ Virtual environment not found. Run: uv venv" -ForegroundColor Red
        $ERRORS++
    }

    if (Test-Path "requirements.txt") {
        Write-Host "✅ requirements.txt exists" -ForegroundColor Green
    } else {
        Write-Host "❌ requirements.txt not found" -ForegroundColor Red
        $ERRORS++
    }

    if (Test-Path ".env") {
        Write-Host "✅ .env file exists" -ForegroundColor Green
    } else {
        Write-Host "⚠️  .env file not found. Copy from .env.example" -ForegroundColor Yellow
        $ERRORS++
    }

    if (Test-Path "main.py") {
        Write-Host "✅ main.py exists" -ForegroundColor Green
    } else {
        Write-Host "❌ main.py not found" -ForegroundColor Red
        $ERRORS++
    }

    Pop-Location
} else {
    Write-Host "❌ backend/ directory not found" -ForegroundColor Red
    $ERRORS++
}

# Check Frontend
Write-Host ""
Write-Host "🎨 Checking Frontend..." -ForegroundColor Yellow
if (Test-Path "frontend") {
    Push-Location frontend

    if (Test-Path "node_modules") {
        Write-Host "✅ node_modules exists" -ForegroundColor Green
    } else {
        Write-Host "❌ node_modules not found. Run: npm install" -ForegroundColor Red
        $ERRORS++
    }

    if (Test-Path "package.json") {
        Write-Host "✅ package.json exists" -ForegroundColor Green
    } else {
        Write-Host "❌ package.json not found" -ForegroundColor Red
        $ERRORS++
    }

    if (Test-Path ".env.local") {
        Write-Host "✅ .env.local file exists" -ForegroundColor Green
    } else {
        Write-Host "⚠️  .env.local file not found. Copy from .env.example" -ForegroundColor Yellow
        $ERRORS++
    }

    Pop-Location
} else {
    Write-Host "❌ frontend/ directory not found" -ForegroundColor Red
    $ERRORS++
}

# Final Report
Write-Host ""
Write-Host "==================================================" -ForegroundColor Cyan
if ($ERRORS -eq 0) {
    Write-Host "✅ ALL CHECKS PASSED!" -ForegroundColor Green
    Write-Host "   You are ready to start development" -ForegroundColor Green
    Write-Host ""
    Write-Host "Next steps:" -ForegroundColor Yellow
    Write-Host "1. Terminal 1: cd backend; .venv\Scripts\activate; uvicorn main:app --reload" -ForegroundColor White
    Write-Host "2. Terminal 2: cd frontend; npm run dev" -ForegroundColor White
    Write-Host "3. Visit: http://localhost:3000" -ForegroundColor White
} else {
    Write-Host "❌ FOUND $ERRORS ISSUE(S)" -ForegroundColor Red
    Write-Host "   Please fix the issues above before starting" -ForegroundColor Red
    Write-Host "   See SETUP.md for detailed instructions" -ForegroundColor Yellow
}
Write-Host "==================================================" -ForegroundColor Cyan
