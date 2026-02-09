# Testing Guide - Todo Application Phase 2

## 🧪 Pre-Testing Checklist

### Backend Verification

```bash
cd Phase-2/backend

# 1. Check virtual environment exists
ls .venv/

# 2. Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Verify dependencies installed
pip list | grep -E "(fastapi|sqlmodel|uvicorn|asyncpg|jose|passlib)"

# Expected output:
# fastapi          0.115.0
# sqlmodel         0.0.22
# uvicorn          0.32.1
# asyncpg          0.30.0
# python-jose      3.3.0
# passlib          1.7.4
```

### Frontend Verification

```bash
cd Phase-2/frontend

# 1. Check node_modules exists
ls node_modules/ | wc -l  # Should show many packages

# 2. Verify key dependencies
npm list clsx tailwind-merge next react

# Expected: All should be installed with versions
```

### Environment Configuration

**Backend `.env` file must have:**
```bash
# Phase-2/backend/.env
DATABASE_URL=postgresql+asyncpg://user:password@host/database
BETTER_AUTH_SECRET=your-secret-key
BACKEND_CORS_ORIGINS=http://localhost:3000
SECRET_KEY=your-jwt-secret
```

**Frontend `.env.local` file must have:**
```bash
# Phase-2/frontend/.env.local
NEXT_PUBLIC_API_URL=http://localhost:8000
BETTER_AUTH_SECRET=your-secret-key  # Same as backend
```

---

## 🚀 Test Execution Plan

### Test 1: Backend Server Startup

```bash
cd Phase-2/backend
.venv\Scripts\activate
uvicorn main:app --reload
```

**Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
🚀 Starting up FastAPI backend...
✅ Database initialized
INFO:     Application startup complete.
```

**✅ Pass Criteria:**
- Server starts without errors
- Port 8000 is accessible
- Database initialization message appears

**❌ Fail Indicators:**
- "ModuleNotFoundError" → Dependencies not installed in venv
- "Connection refused" → Database URL incorrect
- "Address already in use" → Port 8000 is occupied

**Verification:**
```bash
# In another terminal
curl http://localhost:8000/health

# Expected response:
# {"status":"healthy","service":"Todo Application API","version":"1.0.0"}
```

### Test 2: API Documentation Access

**Visit:** http://localhost:8000/docs

**✅ Pass Criteria:**
- Swagger UI loads successfully
- Shows endpoints:
  - POST /api/auth/signup
  - POST /api/auth/login
  - POST /api/auth/logout
  - GET /api/{user_id}/tasks
  - POST /api/{user_id}/tasks
  - PUT /api/{user_id}/tasks/{id}
  - DELETE /api/{user_id}/tasks/{id}
  - PATCH /api/{user_id}/tasks/{id}/complete

### Test 3: Frontend Server Startup

```bash
cd Phase-2/frontend
npm run dev
```

**Expected Output:**
```
▲ Next.js 15.1.5
- Local:        http://localhost:3000
- Ready in 2.5s
```

**✅ Pass Criteria:**
- Server starts on port 3000
- No compilation errors
- Ready message appears

**❌ Fail Indicators:**
- "Module not found" → Run `npm install`
- "EADDRINUSE" → Port 3000 is occupied
- TypeScript errors → Check component syntax

**Verification:**
```bash
# Visit in browser
http://localhost:3000
```

---

## 🔐 Test 4: User Authentication Flow

### 4.1 User Signup

**Steps:**
1. Open http://localhost:3000/signup
2. Fill in form:
   - Name: "Test User"
   - Email: "test@example.com"
   - Password: "Password123!"
3. Click "Sign up"

**✅ Expected Result:**
- Redirect to /dashboard
- No error messages
- User logged in

**❌ Failure Cases:**
- Error: "Email already registered" → User exists, try different email
- Error: "Failed to create account" → Check backend logs
- Network error → Check backend is running on port 8000

**Backend Verification:**
```bash
# Check backend terminal for log:
[PERF] Task creation took 0.123s for user <user_id>
```

### 4.2 User Login

**Steps:**
1. Open http://localhost:3000/login
2. Enter credentials from signup
3. Click "Sign in"

**✅ Expected Result:**
- Redirect to /dashboard
- Welcome message shows user name
- No errors

**Frontend Console Check:**
```javascript
// Open browser DevTools (F12) → Console
// Check for:
// - No error messages
// - localStorage has "auth_token"
// - localStorage has "user" JSON
```

### 4.3 Session Persistence

**Steps:**
1. Login successfully
2. Refresh page (F5)
3. Check if still logged in

**✅ Expected Result:**
- User remains logged in
- Dashboard still accessible
- User data persists

---

## 📝 Test 5: Task CRUD Operations

### 5.1 Create Task

**Steps:**
1. Login to dashboard
2. Fill in task form:
   - Title: "Test Task 1"
   - Description: "This is a test task"
3. Click "Create Task"

**✅ Expected Result:**
- Task appears in task list immediately
- Form clears after submission
- No error messages

**Verification:**
- Task shows with "Pending" status badge (yellow)
- Task title and description display correctly
- Timestamp shows current date

### 5.2 View Tasks

**Steps:**
1. Create 2-3 tasks
2. Check task list displays all tasks
3. Test filter buttons:
   - Click "All" → Shows all tasks
   - Click "Pending" → Shows only incomplete tasks
   - Click "Completed" → Shows only completed tasks

**✅ Expected Result:**
- All tasks visible
- Filters work correctly
- Loading spinner shows during fetch

### 5.3 Mark Task Complete

**Steps:**
1. Click checkbox next to a task
2. Observe changes

**✅ Expected Result:**
- Task text gets strikethrough
- Badge changes from "Pending" (yellow) to "Completed" (green)
- UI updates immediately
- Click again to unmark → reverses changes

### 5.4 Edit Task

**Steps:**
1. Hover over a task
2. Click edit icon (pencil)
3. Modal opens with current values
4. Change title to "Updated Task"
5. Click "Save Changes"

**✅ Expected Result:**
- Modal opens with pre-filled values
- Changes save successfully
- Modal closes
- Task list updates with new values

### 5.5 Delete Task

**Steps:**
1. Hover over a task
2. Click delete icon (trash)
3. Confirmation dialog appears
4. Click "OK" to confirm

**✅ Expected Result:**
- Confirmation dialog shows
- Task removed from list
- No error messages

---

## 🎨 Test 6: UI/UX Verification

### 6.1 Responsive Design

**Test on different screen sizes:**

**Desktop (1920x1080):**
- ✅ Dashboard shows 2-column layout (form left, tasks right)
- ✅ All elements properly spaced

**Tablet (768px):**
- ✅ Layout stacks vertically
- ✅ Form and tasks take full width

**Mobile (375px):**
- ✅ All content readable
- ✅ Buttons touchable (min 44px)
- ✅ Form inputs full width

**How to Test:**
1. Open DevTools (F12)
2. Click device toolbar icon (Ctrl+Shift+M)
3. Select different devices
4. Verify layout adapts

### 6.2 Loading States

**Test:**
1. Login to dashboard
2. Observe loading spinner while fetching tasks
3. Create/edit/delete task → observe button shows loading text

**✅ Expected:**
- Spinner shows during data fetch
- Button text changes: "Creating..." / "Saving..." / "Deleting..."
- No flickering or UI jumps

### 6.3 Error Handling

**Test Error Scenarios:**

1. **Network Error:**
   - Stop backend server
   - Try to create a task
   - ✅ Should show error message (red box)

2. **Validation Error:**
   - Try to create task with empty title
   - ✅ Should show "Title is required"

3. **Authentication Error:**
   - Clear localStorage
   - Refresh page
   - ✅ Should redirect to /login

---

## 🔒 Test 7: Security Verification

### 7.1 User Isolation

**Steps:**
1. Create Account A (user1@test.com)
2. Create 2 tasks
3. Logout
4. Create Account B (user2@test.com)
5. Check task list

**✅ Expected Result:**
- User B sees NO tasks from User A
- User B can only see their own tasks

### 7.2 JWT Token Validation

**Steps:**
1. Login successfully
2. Open DevTools → Application → Local Storage
3. Modify "auth_token" value
4. Refresh page or try to create task

**✅ Expected Result:**
- Invalid token rejected
- Redirect to login page
- Error message shown

### 7.3 SQL Injection Protection

**Test with malicious input:**
```
Title: "'; DROP TABLE tasks; --"
Description: "1' OR '1'='1"
```

**✅ Expected Result:**
- Input treated as literal string
- Task created with exact text
- No SQL execution
- No server errors

---

## 📊 Test Results Template

```markdown
## Test Execution Report
**Date:** 2026-02-08
**Tester:** [Your Name]
**Environment:** Local Development

| Test ID | Test Name | Status | Notes |
|---------|-----------|--------|-------|
| T1 | Backend Startup | ✅ PASS | Server started on port 8000 |
| T2 | API Documentation | ✅ PASS | Swagger UI accessible |
| T3 | Frontend Startup | ✅ PASS | Next.js running on port 3000 |
| T4.1 | User Signup | ✅ PASS | Account created successfully |
| T4.2 | User Login | ✅ PASS | Login successful, redirected |
| T4.3 | Session Persist | ✅ PASS | Session maintained after refresh |
| T5.1 | Create Task | ✅ PASS | Task created and displayed |
| T5.2 | View Tasks | ✅ PASS | All tasks visible, filters work |
| T5.3 | Complete Task | ✅ PASS | Toggle works, UI updates |
| T5.4 | Edit Task | ✅ PASS | Modal opens, updates save |
| T5.5 | Delete Task | ✅ PASS | Confirmation shown, task deleted |
| T6.1 | Responsive Design | ✅ PASS | Layout adapts to screen sizes |
| T6.2 | Loading States | ✅ PASS | Spinners and loading text shown |
| T6.3 | Error Handling | ✅ PASS | Errors displayed properly |
| T7.1 | User Isolation | ✅ PASS | Users see only their tasks |
| T7.2 | JWT Validation | ✅ PASS | Invalid tokens rejected |
| T7.3 | SQL Injection | ✅ PASS | Input sanitized properly |

**Overall Status:** ✅ ALL TESTS PASSED
**Issues Found:** None
**Ready for:** Production deployment
```

---

## 🐛 Common Issues & Solutions

### Issue: Backend won't start

**Symptoms:** Import errors, module not found

**Solutions:**
```bash
# Ensure virtual environment is activated
.venv\Scripts\activate

# Reinstall dependencies
uv pip install -r requirements.txt

# Check Python version
python --version  # Should be 3.13+
```

### Issue: Frontend build errors

**Symptoms:** "Module not found", TypeScript errors

**Solutions:**
```bash
# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install

# Clear Next.js cache
rm -rf .next
npm run dev
```

### Issue: Database connection failed

**Symptoms:** "Connection refused", "Invalid connection string"

**Solutions:**
1. Check DATABASE_URL in `.env`
2. Verify Neon database is accessible
3. Test connection string format:
   ```
   postgresql+asyncpg://user:password@host/database
   ```

### Issue: CORS errors in browser

**Symptoms:** "Access-Control-Allow-Origin" error

**Solutions:**
1. Check BACKEND_CORS_ORIGINS in backend `.env`
2. Should include: `http://localhost:3000`
3. Restart backend server

### Issue: Tasks not appearing

**Symptoms:** Empty task list after creation

**Solutions:**
1. Check browser console (F12) for errors
2. Verify API_URL in frontend `.env.local`
3. Check backend logs for errors
4. Verify JWT token in localStorage

---

## ✅ Final Testing Checklist

Before marking application as "ready":

- [ ] Backend starts without errors
- [ ] Frontend starts without errors
- [ ] User can sign up
- [ ] User can login
- [ ] Session persists after refresh
- [ ] User can create tasks
- [ ] User can view all tasks
- [ ] Filters work (All/Pending/Completed)
- [ ] User can edit tasks
- [ ] User can delete tasks (with confirmation)
- [ ] User can mark tasks complete/incomplete
- [ ] Responsive design works on mobile
- [ ] Error messages display properly
- [ ] Loading states show during operations
- [ ] User isolation works (users see only their tasks)
- [ ] Invalid JWT tokens are rejected
- [ ] SQL injection protection works

**Completion Criteria:** All items checked ✅

---

## 📝 Next Steps After Testing

If all tests pass:
1. ✅ Update documentation with test results
2. ✅ Create deployment guide
3. ✅ Set up production environment
4. ✅ Deploy to Vercel (frontend) and cloud (backend)

If issues found:
1. Document all issues
2. Prioritize by severity
3. Fix critical bugs first
4. Re-test after fixes

---

**Last Updated:** 2026-02-08
**Status:** Ready for Testing
