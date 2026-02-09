# 🔍 Notification Debugging Guide

**Date**: 2026-02-09
**Status**: Enhanced Debugging Active

## Problem

User created a task with 14-minute due date but:
- ❌ No notification appeared in browser
- ❌ No console log messages appeared

## Enhanced Debugging Implemented

I've added comprehensive console logging to every step of the notification process. This will help us identify exactly where the issue is occurring.

## Testing Steps (CRITICAL - Follow Exactly)

### Step 1: Restart Frontend

```bash
cd D:\D\Gov\4rth_semester_2F\all-works\work\Todo-App\Phase-2\frontend

# Stop if running (Ctrl+C)
npm run dev
```

Wait for: `✓ Ready in X seconds`

### Step 2: Open Browser Console FIRST

**CRITICAL**: You MUST open the console BEFORE loading the page!

1. Open a **new incognito/private window** (to avoid cache issues)
2. Press **F12** to open DevTools
3. Go to **Console** tab
4. Click the gear icon (⚙️) in DevTools
5. Enable "Preserve log" checkbox (IMPORTANT!)
6. NOW navigate to: http://localhost:3000

### Step 3: Login and Check Initial Logs

After logging in and reaching the dashboard, you should see these logs:

```
[Notification Debug] useEffect triggered
[Notification Debug] Window check: true
[Notification Debug] Notification API available: true
[Notification Debug] Tasks count: X
[Notification Debug] Permission: granted (or default/denied)
```

**If you see "BLOCKED" messages**: This tells us exactly why notifications aren't working!

### Step 4: Enable Notifications

If button appears "🔔 Enable Notifications":

1. Click it
2. Browser popup: "Allow localhost to send notifications?"
3. Click **Allow**
4. Should see test notification immediately
5. Console should show new permission status

### Step 5: Create 14-Minute Test Task

**Get exact time for due date**:

1. Open JavaScript console (in the Console tab, bottom prompt)
2. Type and press Enter:
   ```javascript
   new Date(Date.now() + 14 * 60 * 1000).toISOString()
   ```
3. Copy the result (it will look like: `2026-02-09T16:45:30.123Z`)

**Create task**:
- Title: `Notification Test 14min`
- Description: `Testing browser notifications`
- Priority: High
- Due Date: Paste the ISO string from above OR use the date picker to set 14 minutes from now

**Click "Create Task"**

### Step 6: Check Console Output Immediately

After creating the task, console should show:

```
[Notification Debug] useEffect triggered
[Notification Debug] Tasks count: X (increased by 1)
[Notification Debug] ✅ All checks passed, setting up notification monitoring
[Notification Debug] Check running at: [time]
[Notification Debug] 15-minute window: [time]
[Notification Debug] Checking X tasks
[Notification Debug] Task "Notification Test 14min": {...}
[Notification Debug] Task "Notification Test 14min" due in 14 minutes
[Notification Debug] Due date: [timestamp]
[Notification Debug] Is future: true
[Notification Debug] Within 15min window: true
[Notification Debug] ✅ Task "Notification Test 14min" qualifies for notification!
[Notification Debug] Notification ID: task-X-[timestamp]
[Notification Debug] Already shown: false
[Notification] 🔔 SHOWING NOTIFICATION for task "Notification Test 14min" due in 14 minutes
[Notification] ✅ Notification object created successfully
[Notification] Notification marked as shown in localStorage
```

**If you see different output**, copy the EXACT console logs and show me!

## Debug Scenarios

### Scenario A: No Console Logs at All

**Cause**: JavaScript not executing or console not capturing

**Fix**:
1. Check browser console is open (F12)
2. Check "Preserve log" is enabled
3. Refresh page with F5
4. Check no JavaScript errors blocking execution

### Scenario B: "BLOCKED: Permission not granted"

**Cause**: Notification permission denied or not requested

**Fix**:
1. Look for orange button "🔔 Enable Notifications"
2. Click it and allow
3. If button doesn't appear, manually enable:
   - Chrome: Click 🔒 in address bar → Site settings → Notifications → Allow
   - Refresh page

### Scenario C: "BLOCKED: No tasks available"

**Cause**: Tasks not loaded yet

**Fix**:
1. Check if tasks are visible on the page
2. Check console for API errors
3. Verify backend is running on port 8000

### Scenario D: Task Shows "❌ Skipped: No due date"

**Cause**: Due date not saved to database

**Fix**:
1. Check backend logs for task creation
2. Verify due_date field is in the API response
3. Check browser Network tab for task creation response

### Scenario E: Task Shows "❌ Skipped: Already shown this notification"

**Cause**: Notification was shown before but you didn't see it

**Fix**:
1. Clear notification history:
   ```javascript
   localStorage.removeItem("shownNotifications")
   ```
2. Refresh page
3. Try again

### Scenario F: Task Shows "doesn't qualify: Not in 15-minute window"

**Cause**: Due date is more than 15 minutes away OR less than current time

**Fix**:
1. Check the due date you entered
2. Verify it's between NOW and NOW+15 minutes
3. Use the JavaScript command from Step 5 to get exact time

### Scenario G: Logs Show "✅ Notification object created" but No Popup

**Cause**: Browser or OS blocking notifications

**Fix**:
1. Check browser notification settings
2. Check Windows Focus Assist (Do Not Disturb)
3. Check browser isn't minimized
4. Try in different browser (Chrome/Edge)

## Expected Behavior

When everything works:

1. ✅ Console shows "[Notification Debug]" logs
2. ✅ Console shows "✅ Task qualifies for notification!"
3. ✅ Console shows "🔔 SHOWING NOTIFICATION"
4. ✅ Console shows "✅ Notification object created successfully"
5. ✅ Browser notification popup appears with task title
6. ✅ Notification auto-closes after 10 seconds
7. ✅ Clicking notification focuses the window

## Quick Test Command

Run this in browser console after creating a 14-minute task:

```javascript
// Check notification permission
console.log("Permission:", Notification.permission);

// Check localStorage
console.log("Shown notifications:", localStorage.getItem("shownNotifications"));

// Manual test notification
if (Notification.permission === "granted") {
  new Notification("Test", { body: "Manual test notification" });
}
```

## Next Steps

After following these steps:

1. **Copy ALL console output** (right-click in console → Save as...)
2. **Take screenshot** of console logs
3. **Tell me**:
   - What console logs you see
   - Where it stops or shows errors
   - Whether notification popup appears

This will help me identify the exact issue!

## Common Issues & Solutions

### Issue: "Notifications blocked" alert appears

**Solution**: Enable notifications in browser settings:
- Chrome: `chrome://settings/content/notifications`
- Edge: `edge://settings/content/notifications`
- Add localhost to "Allow" list

### Issue: Notification appears but disappears instantly

**Solution**: This is expected! Notifications auto-close after 10 seconds. If you want to test, temporarily increase timeout in code (line 10000ms → 60000ms for 60 seconds).

### Issue: Multiple notifications for same task

**Solution**: Clear localStorage:
```javascript
localStorage.removeItem("shownNotifications")
```

### Issue: No logs appear even after creating task

**Solution**:
1. Check if tasks state is updating (look for task in UI)
2. Check if useEffect is running (should see "useEffect triggered")
3. Check for JavaScript errors in console (red text)
4. Verify you're on the dashboard page (not login page)

---

## Success Checklist

After running the test, you should have:

- [ ] Frontend restarted
- [ ] Browser console open with "Preserve log" enabled
- [ ] Logged into dashboard
- [ ] Console shows "[Notification Debug]" logs
- [ ] Created task with 14-minute due date
- [ ] Console shows "✅ Task qualifies for notification!"
- [ ] Console shows "🔔 SHOWING NOTIFICATION"
- [ ] Browser notification popup appeared
- [ ] Can see notification message with task title

**If ANY step fails, that's where the problem is!** Share the console output at that step.
