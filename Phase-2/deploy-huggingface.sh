#!/bin/bash
# Backend Deployment Script for Hugging Face Spaces
# Usage: ./deploy-huggingface.sh

set -e

echo "🤗 Todo App - Backend Deployment to Hugging Face Spaces"
echo "========================================================="
echo ""

# Check if in correct directory
if [ ! -f "requirements.txt" ]; then
    echo "❌ Error: Must run from Phase-2/backend directory"
    exit 1
fi

# Check for required files
echo "📋 Checking required files..."
REQUIRED_FILES=("Dockerfile" "README.md" "requirements.txt" "main.py")
for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "  ✅ $file"
    else
        echo "  ❌ Missing: $file"
        exit 1
    fi
done

echo ""
echo "🔍 Validating Dockerfile..."
if grep -q "EXPOSE 7860" Dockerfile; then
    echo "  ✅ Port 7860 configured"
else
    echo "  ❌ Dockerfile must expose port 7860 for Hugging Face"
    exit 1
fi

echo ""
echo "🔍 Validating README.md frontmatter..."
if grep -q "sdk: docker" README.md; then
    echo "  ✅ Docker SDK specified"
else
    echo "  ❌ README.md must have 'sdk: docker' in frontmatter"
    exit 1
fi

# Test Docker build locally
echo ""
echo "🐳 Testing Docker build locally..."
docker build -t todo-backend-test . || {
    echo "❌ Docker build failed. Fix errors before deploying."
    exit 1
}
echo "✅ Docker build successful"

# Check if git is initialized
if [ ! -d ".git" ]; then
    echo ""
    echo "📦 Initializing git repository..."
    git init
    git branch -M main
fi

# Prompt for Hugging Face username
echo ""
read -p "Enter your Hugging Face username: " HF_USERNAME

if [ -z "$HF_USERNAME" ]; then
    echo "❌ Username cannot be empty"
    exit 1
fi

# Set up Hugging Face remote
SPACE_NAME="todo-app-backend"
HF_REPO="https://huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME"

echo ""
echo "🔗 Setting up Hugging Face remote..."
if git remote | grep -q "^hf$"; then
    echo "  Updating existing remote..."
    git remote set-url hf "$HF_REPO"
else
    echo "  Adding new remote..."
    git remote add hf "$HF_REPO"
fi

echo "  ✅ Remote set to: $HF_REPO"

# Show environment variables reminder
echo ""
echo "⚠️  IMPORTANT: Before deploying, set these environment variables in Hugging Face Space settings:"
echo ""
echo "  1. DATABASE_URL         - Your Neon PostgreSQL connection string"
echo "  2. BETTER_AUTH_SECRET   - Generate with: openssl rand -hex 32"
echo "  3. SECRET_KEY           - Generate with: openssl rand -hex 32"
echo "  4. BACKEND_CORS_ORIGINS - Your frontend URL (e.g., https://app.vercel.app)"
echo ""
echo "📍 Set variables at: https://huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME/settings"
echo ""

read -p "Have you created the Space and set the environment variables? (y/n): " CONFIRMED

if [ "$CONFIRMED" != "y" ]; then
    echo ""
    echo "📝 Next steps:"
    echo "  1. Go to https://huggingface.co/new-space"
    echo "  2. Create Space with name: $SPACE_NAME"
    echo "  3. Select SDK: Docker"
    echo "  4. Set environment variables in Space settings"
    echo "  5. Run this script again"
    exit 0
fi

# Prepare files for deployment
echo ""
echo "📦 Preparing files for deployment..."

# Create .gitignore if needed
if [ ! -f ".gitignore" ]; then
    cat > .gitignore << 'EOF'
__pycache__/
*.pyc
.venv/
.env
.env.local
*.log
.pytest_cache/
.coverage
EOF
fi

# Stage files
git add Dockerfile README.md requirements.txt main.py src/ .dockerignore .gitignore

# Commit
echo ""
echo "💾 Creating commit..."
git commit -m "Deploy backend to Hugging Face Spaces

- FastAPI application with async PostgreSQL
- JWT authentication
- Task management with priority and tags
- Search, filter, and sort capabilities
- Health check endpoint at /health
- API documentation at /docs" || {
    echo "ℹ️  No changes to commit (already up to date)"
}

# Push to Hugging Face
echo ""
echo "🚀 Pushing to Hugging Face..."
echo "  Repository: $HF_REPO"
echo ""

git push hf main || {
    echo ""
    echo "❌ Push failed. This might be because:"
    echo "  1. Space doesn't exist yet - Create it at: https://huggingface.co/new-space"
    echo "  2. Authentication failed - Run: git config credential.helper store"
    echo "  3. You don't have access - Check repository permissions"
    exit 1
}

echo ""
echo "✅ Deployment initiated!"
echo ""
echo "📊 Deployment Status:"
echo "  - Space URL: https://huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME"
echo "  - Building... (this may take 2-3 minutes)"
echo ""
echo "📝 Next steps:"
echo "  1. Monitor build: https://huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME/logs"
echo "  2. Test health: https://$HF_USERNAME-$SPACE_NAME.hf.space/health"
echo "  3. View docs: https://$HF_USERNAME-$SPACE_NAME.hf.space/docs"
echo "  4. Update frontend .env.production with backend URL"
echo ""
echo "🔧 Environment Variables (set in Space settings):"
echo "  https://huggingface.co/spaces/$HF_USERNAME/$SPACE_NAME/settings"
echo ""
echo "🎉 Deployment complete! Your API will be live shortly."
