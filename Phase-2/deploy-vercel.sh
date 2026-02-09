#!/bin/bash
# Frontend Deployment Script for Vercel
# Usage: ./deploy-vercel.sh [--production]

set -e

echo "🚀 Todo App - Frontend Deployment to Vercel"
echo "=============================================="
echo ""

# Check if in correct directory
if [ ! -f "package.json" ]; then
    echo "❌ Error: Must run from Phase-2/frontend directory"
    exit 1
fi

# Check if vercel CLI is installed
if ! command -v vercel &> /dev/null; then
    echo "📦 Installing Vercel CLI..."
    npm install -g vercel
fi

# Verify environment file
if [ ! -f ".env.local" ]; then
    echo "⚠️  Warning: .env.local not found"
    echo "Creating from .env.example..."
    cp .env.example .env.local
    echo ""
    echo "❗ IMPORTANT: Update .env.local with production values before deploying:"
    echo "  - NEXT_PUBLIC_API_URL (backend URL)"
    echo "  - BETTER_AUTH_SECRET (must match backend)"
    echo ""
    read -p "Press Enter after updating .env.local..."
fi

# Run build test
echo "🔨 Testing production build..."
npm run build

if [ $? -ne 0 ]; then
    echo "❌ Build failed. Fix errors before deploying."
    exit 1
fi

echo "✅ Build successful"
echo ""

# Deploy
if [ "$1" == "--production" ]; then
    echo "🌐 Deploying to PRODUCTION..."
    vercel --prod
else
    echo "🧪 Deploying to PREVIEW..."
    vercel
fi

echo ""
echo "✅ Deployment complete!"
echo ""
echo "📝 Next steps:"
echo "1. Copy the deployment URL from above"
echo "2. Update backend CORS settings with new URL"
echo "3. Test the deployed application"
echo "4. If preview looks good, run: ./deploy-vercel.sh --production"
