# Deployment Guide - Todo Application Phase 2

**Target Platforms**:
- Frontend: Vercel
- Backend: Railway / Render / Fly.io
- Database: Neon PostgreSQL (already serverless)

---

## Prerequisites

Before deployment, ensure you have:
- [ ] Neon PostgreSQL database created
- [ ] GitHub repository with your code
- [ ] Vercel account (for frontend)
- [ ] Railway/Render account (for backend)
- [ ] All environment variables documented

---

## Part 1: Database Setup (Neon PostgreSQL)

### 1.1 Create Neon Database

1. Visit [https://neon.tech](https://neon.tech)
2. Sign up or login
3. Create new project:
   - Project name: `todo-app-production`
   - Region: Choose closest to your users
   - PostgreSQL version: 16

4. Copy connection string:
   ```
   postgresql://user:password@ep-xxx.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```

5. Convert to async format for FastAPI:
   ```
   postgresql+asyncpg://user:password@ep-xxx.us-east-2.aws.neon.tech/neondb?sslmode=require
   ```

### 1.2 Initialize Database Schema

The database tables will be auto-created on first backend startup thanks to SQLModel's `create_all()` in `main.py`.

**Verify schema creation**:
1. Run backend locally once with production DATABASE_URL
2. Check Neon dashboard → Tables should show:
   - `users` table
   - `tasks` table

---

## Part 2: Backend Deployment (Railway)

### 2.1 Prepare Backend for Deployment

1. Ensure `Phase-2/backend/requirements.txt` is complete:
   ```txt
   fastapi==0.115.0
   sqlmodel==0.0.22
   uvicorn[standard]==0.32.1
   asyncpg==0.30.0
   python-jose[cryptography]==3.3.0
   passlib[bcrypt]==1.7.4
   python-multipart==0.0.12
   pydantic[email]==2.10.3
   ```

2. Create `Phase-2/backend/Procfile`:
   ```
   web: uvicorn main:app --host 0.0.0.0 --port $PORT
   ```

3. Create `Phase-2/backend/runtime.txt`:
   ```
   python-3.13
   ```

### 2.2 Deploy to Railway

1. Visit [https://railway.app](https://railway.app)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Configure:
   - **Root Directory**: `Phase-2/backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`

5. Add Environment Variables:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@ep-xxx.neon.tech/neondb?sslmode=require
   BETTER_AUTH_SECRET=your-production-secret-here
   SECRET_KEY=your-jwt-secret-here
   BACKEND_CORS_ORIGINS=https://your-frontend.vercel.app
   ```

6. Deploy and copy the backend URL:
   ```
   https://todo-backend-production.up.railway.app
   ```

### 2.3 Alternative: Deploy to Render

1. Visit [https://render.com](https://render.com)
2. New → Web Service → Connect GitHub
3. Configure:
   - **Name**: todo-backend-production
   - **Root Directory**: `Phase-2/backend`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Instance Type**: Free (or Starter for production)

4. Add same environment variables as Railway

---

## Part 3: Frontend Deployment (Vercel)

### 3.1 Prepare Frontend for Deployment

1. Update `Phase-2/frontend/.env.production`:
   ```env
   NEXT_PUBLIC_API_URL=https://todo-backend-production.up.railway.app
   BETTER_AUTH_SECRET=your-production-secret-here
   ```

2. Ensure `Phase-2/frontend/package.json` has build script:
   ```json
   {
     "scripts": {
       "dev": "next dev",
       "build": "next build",
       "start": "next start",
       "lint": "next lint"
     }
   }
   ```

### 3.2 Deploy to Vercel

#### Method 1: Vercel CLI (Recommended)

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend
cd Phase-2/frontend

# Login to Vercel
vercel login

# Deploy
vercel --prod

# Follow prompts:
# - Set up and deploy? Y
# - Which scope? Your account
# - Link to existing project? N
# - Project name? todo-app-frontend
# - Directory? ./
# - Override settings? N
```

#### Method 2: Vercel Dashboard

1. Visit [https://vercel.com](https://vercel.com)
2. Import Project → GitHub repository
3. Configure:
   - **Framework Preset**: Next.js
   - **Root Directory**: `Phase-2/frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `.next`

4. Add Environment Variables:
   ```
   NEXT_PUBLIC_API_URL=https://todo-backend-production.up.railway.app
   BETTER_AUTH_SECRET=your-production-secret-here
   ```

5. Deploy → Copy frontend URL:
   ```
   https://todo-app-frontend.vercel.app
   ```

### 3.3 Update Backend CORS

After frontend deployment, update backend environment variable:

```env
BACKEND_CORS_ORIGINS=https://todo-app-frontend.vercel.app
```

**Railway**: Go to project → Variables → Update → Redeploy
**Render**: Go to service → Environment → Update → Manual Deploy

---

## Part 4: Post-Deployment Verification

### 4.1 Health Checks

**Backend Health**:
```bash
curl https://todo-backend-production.up.railway.app/health
# Expected: {"status":"healthy","service":"Todo Application API","version":"1.0.0"}
```

**Frontend Access**:
```bash
curl -I https://todo-app-frontend.vercel.app
# Expected: HTTP/2 200
```

### 4.2 Full Flow Test

1. Visit `https://todo-app-frontend.vercel.app`
2. Sign up with test account
3. Create a task
4. Verify task appears in list
5. Update task priority/tags
6. Mark task complete
7. Delete task
8. Logout and login again

### 4.3 API Documentation

Visit `https://todo-backend-production.up.railway.app/docs` for Swagger UI

---

## Part 5: Environment Variables Reference

### Backend (.env)

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Neon PostgreSQL async connection string | `postgresql+asyncpg://...` |
| `BETTER_AUTH_SECRET` | Secret for JWT signing (same as frontend) | `random-32-char-string` |
| `SECRET_KEY` | Additional secret for auth | `another-random-string` |
| `BACKEND_CORS_ORIGINS` | Allowed frontend origins | `https://your-app.vercel.app` |

### Frontend (.env.production)

| Variable | Description | Example |
|----------|-------------|---------|
| `NEXT_PUBLIC_API_URL` | Backend API base URL | `https://backend.railway.app` |
| `BETTER_AUTH_SECRET` | Secret for JWT verification (same as backend) | `random-32-char-string` |

**Generating Secure Secrets**:
```bash
# Method 1: Node.js
node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"

# Method 2: Python
python -c "import secrets; print(secrets.token_hex(32))"

# Method 3: OpenSSL
openssl rand -hex 32
```

---

## Part 6: Monitoring and Maintenance

### 6.1 Application Monitoring

**Railway Dashboard**:
- View logs: Project → Deployments → Logs
- Monitor metrics: CPU, Memory, Network
- Set up alerts for errors

**Vercel Dashboard**:
- View deployment logs
- Monitor function execution
- Check analytics for page views

**Neon Dashboard**:
- Monitor database connections
- Check query performance
- View storage usage

### 6.2 Logs Access

**Backend Logs (Railway)**:
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login and view logs
railway login
railway logs
```

**Frontend Logs (Vercel)**:
```bash
# View deployment logs
vercel logs <deployment-url>
```

### 6.3 Database Backups

**Neon automatically backs up your database**:
- Point-in-time recovery available
- Access via Neon dashboard → Backups
- Restore to any point in last 7 days (Free tier)

**Manual backup**:
```bash
pg_dump $DATABASE_URL > backup-$(date +%Y%m%d).sql
```

---

## Part 7: Rollback Strategy

### 7.1 Frontend Rollback (Vercel)

1. Go to Vercel dashboard → Deployments
2. Find previous successful deployment
3. Click "..." → "Promote to Production"
4. Instant rollback (zero downtime)

### 7.2 Backend Rollback (Railway)

1. Go to Railway dashboard → Deployments
2. Find previous deployment
3. Click "Redeploy"
4. Wait for health check to pass

### 7.3 Database Rollback (Neon)

1. Neon dashboard → Backups
2. Select restore point
3. Create new branch from backup
4. Update DATABASE_URL to new branch
5. Redeploy backend

---

## Part 8: Production Checklist

Before going live, verify:

- [ ] Database connection works in production
- [ ] All environment variables are set correctly
- [ ] CORS configured with exact frontend URL
- [ ] JWT secrets match between frontend and backend
- [ ] Health endpoints return 200 OK
- [ ] API documentation accessible
- [ ] User signup/login flow works
- [ ] Task CRUD operations work
- [ ] Rate limiting is active
- [ ] Error handling returns proper status codes
- [ ] Mobile responsive design works
- [ ] HTTPS enforced on all endpoints
- [ ] No sensitive data in logs
- [ ] Database backups configured
- [ ] Monitoring and alerts set up

---

## Part 9: Scaling Considerations

### Current Architecture Limits

**Free Tier Limits**:
- Railway: 500 hours/month, 512MB RAM
- Vercel: 100GB bandwidth, unlimited deployments
- Neon: 0.5GB storage, 100 hours compute

### When to Upgrade

Upgrade when you reach:
- **Users**: >100 concurrent users
- **Database**: >500MB storage
- **Backend**: >1000 requests/minute
- **Frontend**: >50GB bandwidth/month

### Scaling Path

1. **First upgrade** (1,000 users):
   - Railway Hobby plan ($5/month)
   - Neon Pro plan ($19/month)
   - Vercel Pro ($20/month)

2. **Second upgrade** (10,000 users):
   - Railway Pro plan ($20/month)
   - Neon Scale plan ($69/month)
   - Add Redis caching
   - Enable CDN for static assets

3. **Enterprise** (100,000+ users):
   - Dedicated infrastructure
   - Load balancing
   - Database replication
   - Multi-region deployment

---

## Part 10: Troubleshooting

### Issue: 500 Internal Server Error

**Check**:
1. Backend logs for stack traces
2. Database connection string format
3. Environment variables are set
4. Database tables exist

**Fix**:
```bash
# View backend logs
railway logs

# Test database connection
curl https://backend.railway.app/health
```

### Issue: CORS Error in Browser

**Symptoms**: `Access-Control-Allow-Origin` error in console

**Fix**:
1. Update `BACKEND_CORS_ORIGINS` to exact frontend URL
2. No trailing slash in URL
3. Redeploy backend
4. Clear browser cache

### Issue: JWT Token Invalid

**Symptoms**: 401 Unauthorized on all API calls

**Fix**:
1. Ensure `BETTER_AUTH_SECRET` matches in both frontend and backend
2. Check token expiration time
3. Verify JWT signing algorithm
4. Clear localStorage and re-login

### Issue: Database Connection Failed

**Symptoms**: `Connection refused` or timeout errors

**Fix**:
1. Verify DATABASE_URL format: `postgresql+asyncpg://...`
2. Check Neon database is active (not suspended)
3. Ensure SSL mode is `require`
4. Test connection from backend logs

---

## Support and Resources

**Documentation**:
- Neon: https://neon.tech/docs
- Railway: https://docs.railway.app
- Vercel: https://vercel.com/docs
- FastAPI: https://fastapi.tiangolo.com
- Next.js: https://nextjs.org/docs

**Community**:
- Railway Discord: https://discord.gg/railway
- Vercel Discord: https://vercel.com/discord
- FastAPI Discord: https://discord.gg/fastapi

---

**Last Updated**: 2026-02-08
**Status**: Production Ready
