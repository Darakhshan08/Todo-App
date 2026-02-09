#!/bin/bash
# Backend Deployment Script for Railway
# Usage: ./deploy-railway.sh

set -e

echo "🚀 Todo App - Backend Deployment to Railway"
echo "============================================="
echo ""

# Check if in correct directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: Must run from Phase-2/backend directory"
    exit 1
fi

# Check if railway CLI is installed
if ! command -v railway &> /dev/null; then
    echo "📦 Installing Railway CLI..."
    npm install -g @railway/cli
fi

# Login check
echo "🔐 Checking Railway authentication..."
railway whoami &> /dev/null || {
    echo "Please login to Railway:"
    railway login
}

echo "✅ Authenticated"
echo ""

# Environment check
echo "📋 Required environment variables:"
echo "  - DATABASE_URL (from Neon)"
echo "  - BETTER_AUTH_SECRET (shared secret)"
echo "  - SECRET_KEY (JWT secret)"
echo "  - BACKEND_CORS_ORIGINS (frontend URL)"
echo ""
echo "⚠️  Make sure these are set in Railway dashboard before deploying"
echo ""
read -p "Press Enter to continue..."

# Create Procfile if missing
if [ ! -f "Procfile" ]; then
    echo "📝 Creating Procfile..."
    echo "web: uvicorn main:app --host 0.0.0.0 --port \$PORT" > Procfile
fi

# Create runtime.txt if missing
if [ ! -f "runtime.txt" ]; then
    echo "📝 Creating runtime.txt..."
    echo "python-3.13" > runtime.txt
fi

# Link or create project
if [ ! -f "railway.json" ]; then
    echo "🔗 Linking to Railway project..."
    railway link
fi

# Deploy
echo "🚀 Deploying to Railway..."
railway up

echo ""
echo "✅ Deployment initiated!"
echo ""
echo "📝 Next steps:"
echo "1. Check deployment status: railway status"
echo "2. View logs: railway logs"
echo "3. Get deployment URL: railway domain"
echo "4. Update frontend .env.production with backend URL"
echo "5. Test API health: curl https://your-backend.railway.app/health"
echo ""
echo "🔧 Environment variable commands:"
echo "  - List: railway variables"
echo "  - Set: railway variables set KEY=value"
