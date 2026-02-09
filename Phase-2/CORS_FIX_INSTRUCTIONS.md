# CORS Fix - Complete Instructions

## Problem
Frontend unable to connect to backend due to CORS policy and browser cache issues.

## What Was Fixed

### Backend (Already Running)
- ✅ CORS configured for localhost:3000
- ✅ Credentials enabled
- ✅ All methods allowed (GET, POST, PUT, DELETE, PATCH)
- ✅ Timezone handling fixed

### Frontend (Just Fixed)
- ✅ Added `credentials: 'include'` to fetch requests
- File: `frontend/src/lib/api.ts`

## Testing Instructions

### Step 1: Stop Everything

**Kill Frontend (if running):**
```bash
# In frontend terminal, press Ctrl+C
```

### Step 2: Clear Browser Completely

**Option A - Clear Cache (Chrome/Edge):**
1. Press `Ctrl + Shift + Delete`
2. Select "All time"
3. Check only "Cached images and files"
4. Click "Clear data"
5. Close ALL browser windows
6. Reopen browser

**Option B - Use Incognito (Easier!):**
1. Press `Ctrl + Shift + N` (Chrome/Edge)
2. Use this window for testing

### Step 3: Restart Frontend

```bash
cd D:\D\Gov\4rth_semester_2F\all-works\work\Todo-App\Phase-2\frontend
npm run dev
```

**Wait for:**
```
✓ Ready in Xms
○ Local: http://localhost:3000
```

### Step 4: Test

**In Browser (Incognito):**
1. Go to http://localhost:3000
2. Login: h@gmail.com
3. Create task with ALL fields
4. Check browser console (F12) - should be NO errors

### Step 5: Verify CORS Headers

**In Browser Console (F12):**
1. Go to Network tab
2. Create a task
3. Click on the "tasks" request
4. Look at "Response Headers"
5. Should see:
   ```
   access-control-allow-origin: http://localhost:3000
   access-control-allow-credentials: true
   ```

## If Still Getting Errors

### Check 1: Backend Running?
```bash
curl http://localhost:8000/health
```
Should return: `{"status":"healthy",...}`

### Check 2: Frontend Port Correct?
Frontend should be on http://localhost:3000

### Check 3: Token in localStorage?
In browser console:
```javascript
localStorage.getItem('auth_token')
```
Should return a token string (not null)

### Check 4: Request in Network Tab
1. F12 → Network tab
2. Try to create task
3. Look at failed request:
   - If status is (failed) or ERR_FAILED → backend not responding
   - If status is 0 → CORS issue
   - If status is 401 → authentication issue
   - If status is 400/500 → backend error

## Current Status

**Backend:**
- URL: http://localhost:8000
- Status: ✅ Running
- CORS: ✅ Configured
- Database: ✅ Connected

**Frontend:**
- URL: http://localhost:3000
- Status: ✅ Updated with credentials fix
- Needs: Browser cache clear + restart

## Expected Result

After following all steps:
- ✅ Login works
- ✅ Task creation works with all fields
- ✅ No CORS errors in console
- ✅ Tasks save to database
- ✅ Search, filter, sort all work

## Quick Troubleshooting

**Error: CORS policy**
→ Use incognito window or clear browser cache completely

**Error: Not authenticated**
→ Logout and login again to get fresh token

**Error: ERR_FAILED**
→ Check if backend is running: `curl http://localhost:8000/health`

**Error: Connection refused**
→ Backend not running, start it first

## Commands Reference

**Check Backend:**
```bash
curl http://localhost:8000/health
netstat -ano | findstr :8000
```

**Start Frontend:**
```bash
cd D:\D\Gov\4rth_semester_2F\all-works\work\Todo-App\Phase-2\frontend
npm run dev
```

**Test CORS:**
```bash
curl -X OPTIONS http://localhost:8000/api/test/tasks \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" \
  -i | grep access-control
```
