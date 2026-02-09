# Final Testing Steps - Ab Sab Kaam Karega! 🎯

## Current Status

**Backend:**
- ✅ Running on http://localhost:8001 (NOT 8000!)
- ✅ CORS properly configured
- ✅ Database connected
- ✅ Timezone fix applied
- ✅ All features ready

**Frontend:**
- ✅ Updated to use port 8001
- ✅ Credentials included in requests
- ⚠️ Needs restart

## Step-by-Step Instructions

### Step 1: Frontend Restart (MUST DO!)

```bash
# Frontend terminal me jao
cd D:\D\Gov\4rth_semester_2F\all-works\work\Todo-App\Phase-2\frontend

# Agar chal raha hai to Ctrl+C press karen
# Phir start karen:
npm run dev
```

**Wait for:**
```
✓ Ready in 2.5s
○ Local: http://localhost:3000
```

### Step 2: Browser COMPLETELY Clean Karen

**SABSE ZAROORI HAI YE!**

**Option 1 - Incognito Window (Recommended):**
```
Ctrl + Shift + N
```

**Option 2 - Complete Cache Clear:**
1. `Ctrl + Shift + Delete`
2. Select "All time"
3. Check:
   - ✅ Browsing history
   - ✅ Cookies and other site data
   - ✅ Cached images and files
4. Click "Clear data"
5. **Close browser completely**
6. Reopen

### Step 3: Test Karo

**Incognito window me:**

1. **Open:** http://localhost:3000

2. **Login:**
   - Email: h@gmail.com
   - Password: your password

3. **Create Task:**
   ```
   Title: Complete Test
   Description: Testing all features
   Priority: High
   Tags: test, final (press Enter after each)
   Due Date: Select any date/time
   Recurring: Daily
   ```

4. **Click "Create Task"**

### Step 4: Verify

**Should See:**
- ✅ Task appears in list immediately
- ✅ Priority badge (red for High)
- ✅ Tags as blue badges
- ✅ Due date with 📅 icon
- ✅ Recurring with 🔄 icon
- ✅ No errors in console (F12)

**Then Test:**
- ✅ Search: Type "Complete" in search box
- ✅ Filter: Select "Pending" status
- ✅ Sort: Try "Priority (High to Low)"
- ✅ Edit: Click edit button, change priority
- ✅ Complete: Click checkbox to mark done
- ✅ Delete: Click delete button
- ✅ Refresh: Press F5 - all data should persist

## Important Notes

### ❌ Common Mistakes to Avoid

1. **DON'T use old browser window** - Use incognito or clear cache completely
2. **DON'T skip frontend restart** - npm run dev must be restarted
3. **DON'T use port 8000** - Backend is now on 8001
4. **DON'T forget to wait** - Wait for "Ready" message before testing

### ✅ How to Verify Backend

```bash
curl http://localhost:8001/health
```

**Should return:**
```json
{"status":"healthy","service":"Todo Application API","version":"1.0.0"}
```

### ✅ How to Verify CORS

```bash
curl -I -X OPTIONS http://localhost:8001/api/test/tasks \
  -H "Origin: http://localhost:3000" \
  -H "Access-Control-Request-Method: POST" | grep access-control
```

**Should show:**
```
access-control-allow-origin: http://localhost:3000
access-control-allow-credentials: true
```

## If Error Occurs

### Error: "ERR_FAILED" or "Failed to load resource"

**Cause:** Frontend not restarted or using wrong port

**Fix:**
1. Check frontend started: Look for "Ready" message
2. Check backend running: `curl http://localhost:8001/health`
3. Restart frontend completely

### Error: "CORS policy" or "Access-Control-Allow-Origin"

**Cause:** Browser cache

**Fix:**
1. Use incognito window (Ctrl+Shift+N)
2. OR clear ALL browser data (not just cache)
3. Close and reopen browser completely

### Error: "Not authenticated"

**Cause:** Token expired or not saved

**Fix:**
1. Logout completely
2. Close browser
3. Reopen and login again

### Error: Task not creating

**Cause:** Multiple issues possible

**Fix:**
1. Open browser console (F12)
2. Check Network tab
3. Look for failed request
4. Take screenshot and share

## Success Checklist

After testing, you should be able to:

- [x] Login successfully
- [x] Create task with all fields (title, description, priority, tags, due date, recurring)
- [x] See task in list immediately
- [x] Search tasks by keyword
- [x] Filter by status (all/pending/completed)
- [x] Filter by priority (all/high/medium/low)
- [x] Sort by different criteria
- [x] Edit task and update all fields
- [x] Mark task as complete/incomplete
- [x] Delete task
- [x] Refresh page and see all data persist
- [x] No errors in browser console

## Files Changed

1. **Frontend API Client:**
   - File: `frontend/src/lib/api.ts`
   - Changed: Port 8000 → 8001
   - Added: `credentials: 'include'`

2. **Backend:**
   - File: `backend/main.py` (already correct)
   - CORS: Configured for localhost:3000
   - Running: Port 8001 on 0.0.0.0

3. **Task Service:**
   - File: `backend/src/services/task_service.py`
   - Fixed: Timezone handling for due_date

## Contact

If still not working after following ALL steps:
1. Take screenshot of browser console (F12)
2. Take screenshot of Network tab showing failed request
3. Share both screenshots

---

**Port Change Summary:**
- ❌ Old: http://localhost:8000
- ✅ New: http://localhost:8001

**Make sure frontend is restarted and using port 8001!**
