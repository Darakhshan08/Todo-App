# Automated Testing Guide - Backend

**Task**: T079 [Phase 12] - Automated tests for critical user flows

---

## 📋 Test Coverage

### Authentication Tests (`tests/test_auth.py`)

1. ✅ User signup with valid data
2. ✅ User signup with duplicate email (should fail)
3. ✅ User login with correct credentials
4. ✅ Login with invalid password (should fail)
5. ✅ Login with non-existent user (should fail)

### Task Management Tests (`tests/test_tasks.py`)

1. ✅ Create task with priority and tags
2. ✅ List all tasks for user
3. ✅ Update task title and priority
4. ✅ Mark task as complete
5. ✅ Delete task
6. ✅ User isolation (users can't access other users' tasks)
7. ✅ Search and filter tasks
8. ✅ Unauthorized access (should require authentication)

**Total Test Cases**: 13 automated tests

---

## 🚀 Running Tests

### Prerequisites

```bash
# Ensure you're in backend directory
cd Phase-2/backend

# Activate virtual environment
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# Install test dependencies (if not already)
pip install pytest pytest-asyncio httpx aiosqlite
```

### Run All Tests

```bash
# Run all tests with verbose output
pytest -v

# Run with coverage report
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_auth.py -v

# Run specific test
pytest tests/test_auth.py::test_user_signup -v
```

### Expected Output

```
======================== test session starts ========================
collected 13 items

tests/test_auth.py::test_user_signup PASSED                    [  7%]
tests/test_auth.py::test_user_signup_duplicate_email PASSED    [ 15%]
tests/test_auth.py::test_user_login PASSED                     [ 23%]
tests/test_auth.py::test_login_invalid_credentials PASSED      [ 30%]
tests/test_auth.py::test_login_nonexistent_user PASSED         [ 38%]
tests/test_tasks.py::test_create_task PASSED                   [ 46%]
tests/test_tasks.py::test_get_tasks PASSED                     [ 53%]
tests/test_tasks.py::test_update_task PASSED                   [ 61%]
tests/test_tasks.py::test_complete_task PASSED                 [ 69%]
tests/test_tasks.py::test_delete_task PASSED                   [ 76%]
tests/test_tasks.py::test_user_isolation PASSED                [ 84%]
tests/test_tasks.py::test_search_filter_tasks PASSED           [ 92%]
tests/test_tasks.py::test_unauthorized_access PASSED           [100%]

======================== 13 passed in 2.45s ========================
```

---

## 🔧 Test Infrastructure

### Test Database

Tests use an in-memory SQLite database:
- Fast (no disk I/O)
- Isolated (each test gets fresh database)
- Automatic cleanup
- No production data affected

### Fixtures

**`client`** - Async HTTP client for API testing
```python
async def test_example(client: AsyncClient):
    response = await client.get("/api/endpoint")
```

**`authenticated_client`** - Pre-authenticated client with user
```python
async def test_example(authenticated_client):
    client, user_id = await authenticated_client
    response = await client.get(f"/api/{user_id}/tasks")
```

### Configuration

`pytest.ini` - Test configuration
- Auto-detect async tests
- Verbose output
- Short traceback on failures

`conftest.py` - Shared fixtures
- Database setup/teardown
- Test client creation
- Dependency overrides

---

## 📊 Test Organization

```
backend/
├── tests/
│   ├── __init__.py           # Package marker
│   ├── conftest.py           # Shared fixtures and config
│   ├── test_auth.py          # Authentication flow tests
│   └── test_tasks.py         # Task management tests
├── pytest.ini                # Pytest configuration
└── requirements.txt          # Includes test dependencies
```

---

## ✅ What's Tested

### Critical User Flows ✅

1. **Authentication Flow**
   - User can sign up
   - User can login
   - Invalid credentials rejected
   - Duplicate signup prevented

2. **Task CRUD Flow**
   - User can create tasks
   - User can view their tasks
   - User can update tasks
   - User can delete tasks
   - User can mark tasks complete

3. **Security & Isolation**
   - Authentication required for all endpoints
   - Users can only access their own data
   - JWT tokens properly validated

4. **Advanced Features**
   - Search functionality works
   - Filtering by priority works
   - Filtering by tags works

---

## 🐛 Debugging Failed Tests

### Test Fails with Database Error

```bash
# Make sure test database dependencies are installed
pip install aiosqlite

# Check that SQLModel models are properly imported
```

### Test Fails with Import Error

```bash
# Ensure you're in the backend directory
cd Phase-2/backend

# Ensure virtual environment is activated
.venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Test Fails with Authentication Error

Check that:
- JWT secret is properly configured
- Token generation logic is correct
- Fixtures are creating users correctly

---

## 🔄 CI/CD Integration

### GitHub Actions Example

```yaml
name: Backend Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.13'

    - name: Install dependencies
      run: |
        cd Phase-2/backend
        pip install -r requirements.txt

    - name: Run tests
      run: |
        cd Phase-2/backend
        pytest -v
```

---

## 📝 Adding New Tests

### Test Template

```python
import pytest
from httpx import AsyncClient
from fastapi import status

@pytest.mark.asyncio
async def test_new_feature(client: AsyncClient):
    """Test description"""
    # Arrange - Set up test data
    test_data = {"key": "value"}

    # Act - Execute the operation
    response = await client.post("/api/endpoint", json=test_data)

    # Assert - Verify results
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["key"] == "value"
```

### Best Practices

1. ✅ One assertion per test (when possible)
2. ✅ Clear test names describing what's tested
3. ✅ Arrange-Act-Assert pattern
4. ✅ Clean up after tests (handled by fixtures)
5. ✅ Test both success and failure cases
6. ✅ Use realistic test data

---

## 🎯 Next Steps

### Expand Test Coverage

1. **API Endpoint Tests**
   - Test all query parameters
   - Test pagination
   - Test sorting options

2. **Validation Tests**
   - Test input validation
   - Test field length limits
   - Test required fields

3. **Performance Tests**
   - Load testing
   - Concurrent request handling
   - Database query optimization

4. **Integration Tests**
   - Full user journey tests
   - Multi-step workflows
   - Error recovery

---

## 📚 Resources

- **Pytest Docs**: https://docs.pytest.org
- **Pytest-Asyncio**: https://pytest-asyncio.readthedocs.io
- **HTTPX**: https://www.python-httpx.org
- **FastAPI Testing**: https://fastapi.tiangolo.com/tutorial/testing/

---

**Status**: ✅ 13 Critical Flow Tests Implemented
**Coverage**: Authentication + Task CRUD + Security
**Test Framework**: Pytest with async support
