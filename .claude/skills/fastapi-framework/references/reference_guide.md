# FastAPI Reference Guide

## Installation

```bash
pip install fastapi uvicorn
```

For production features:
```bash
pip install "fastapi[all]"
```

## Core Concepts

### Application Instance
```python
from fastapi import FastAPI

app = FastAPI(
    title="My API",
    description="API description",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)
```

### Path Operations
```python
@app.get("/")
@app.post("/items")
@app.put("/items/{item_id}")
@app.delete("/items/{item_id}")
@app.patch("/items/{item_id}")
```

## Data Types

### Standard Python Types
- `str` - String
- `int` - Integer
- `float` - Float
- `bool` - Boolean
- `list` - List
- `dict` - Dictionary

### Optional Types
```python
from typing import Optional

def read_item(item_id: int, q: Optional[str] = None):
    pass
```

### Lists and Complex Types
```python
from typing import List

def read_items(names: List[str]):
    pass
```

## Pydantic Models

### Basic Model
```python
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
```

### Model with Validation
```python
from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    price: float = Field(..., gt=0)
    category: str = Field(..., regex=r'^[a-zA-Z]+$')
```

### Model Configuration
```python
class Item(BaseModel):
    name: str
    description: str

    class Config:
        orm_mode = True  # Enable SQLAlchemy compatibility
        extra = "forbid"  # Forbid extra fields
```

## Request Body

### Single Body Parameter
```python
@app.post("/items/")
def create_item(item: Item):
    return item
```

### Multiple Body Parameters
```python
@app.put("/items/{item_id}")
def update_item(
    item_id: int,
    item: Item,
    user: User
):
    return {"item_id": item_id, "item": item, "user": user}
```

### Body Fields
```python
from pydantic import Field

@app.post("/items/")
def create_item(
    name: str = Body(...),
    description: str = Body(default=None),
    price: float = Body(..., gt=0)
):
    pass
```

## Response Models

### Basic Response Model
```python
@app.post("/users/", response_model=User)
def create_user(user: UserCreate):
    return user
```

### Response Model with Subset
```python
class UserInDB(User):
    hashed_password: str

@app.post("/user/", response_model=User)
def create_user(user: UserInDB):
    return user
```

## Query Parameters

### Optional Parameters
```python
@app.get("/items/")
def read_items(q: str = None):
    pass
```

### Default Values
```python
@app.get("/items/")
def read_items(skip: int = 0, limit: int = 100):
    pass
```

### Validation
```python
from typing import Optional

@app.get("/items/")
def read_items(
    q: Optional[str] = Query(
        None,
        min_length=3,
        max_length=50,
        regex="^fixedquery$"
    )
):
    pass
```

## Path Parameters

### Basic Path Parameters
```python
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}
```

### Path Parameters with Validation
```python
from fastapi import Path

@app.get("/items/{item_id}")
def read_item(
    item_id: int = Path(..., ge=1)
):
    pass
```

## Cookie and Header Parameters

### Cookies
```python
from fastapi import Cookie

@app.get("/items/")
def read_items(ads_id: str = Cookie(None)):
    pass
```

### Headers
```python
from fastapi import Header

@app.get("/items/")
def read_items(user_agent: str = Header(None)):
    pass
```

## Form Data

```python
from fastapi import Form

@app.post("/login/")
def login(username: str = Form(...), password: str = Form(...)):
    pass
```

## File Uploads

### Single File
```python
from fastapi import File, UploadFile

@app.post("/files/")
def create_file(file: bytes = File(...)):
    return {"file_size": len(file)}

@app.post("/uploadfile/")
def create_upload_file(file: UploadFile):
    return {"filename": file.filename}
```

### Multiple Files
```python
@app.post("/files/")
def create_files(files: list[bytes] = File(...)):
    return {"file_count": len(files)}

@app.post("/uploadfiles/")
def create_upload_files(files: list[UploadFile]):
    return {"filenames": [file.filename for file in files]}
```

## Dependencies

### Simple Dependency
```python
def get_token_header():
    return "fake-super-secret-token"

@app.get("/items/", dependencies=[Depends(get_token_header)])
def read_items():
    pass
```

### Class-based Dependency
```python
class CommonQueryParams:
    def __init__(self, q: str = None, skip: int = 0, limit: int = 100):
        self.q = q
        self.skip = skip
        self.limit = limit

@app.get("/items/")
def read_items(commons: CommonQueryParams = Depends()):
    pass
```

## Security

### OAuth2 Password Bearer
```python
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/users/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

### HTTP Basic Auth
```python
from fastapi.security import HTTPBasic, HTTPBasicCredentials

security = HTTPBasic()

@app.get("/users/me")
def read_current_user(credentials: HTTPBasicCredentials = Depends(security)):
    return {"username": credentials.username, "password": credentials.password}
```

## Error Handling

### HTTPException
```python
from fastapi import HTTPException

@app.get("/items/{item_id}")
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(
            status_code=404,
            detail="Item not found",
            headers={"X-Error": "There goes my error"}
        )
```

### Custom Exception Handler
```python
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return PlainTextResponse(str(exc), status_code=400)
```

## Middleware

### Adding Middleware
```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Custom Middleware
```python
from starlette.middleware.base import BaseHTTPMiddleware

class CustomHeaderMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)
        response.headers["Custom-Header"] = "Value"
        return response

app.add_middleware(CustomHeaderMiddleware)
```

## Background Tasks

```python
from fastapi import BackgroundTasks

def send_email(email: str):
    # Simulate sending email
    pass

@app.post("/send-notification/{email}")
def send_notification(
    email: str, background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, email)
    return {"message": "Notification sent in the background"}
```

## Testing

### Basic Test
```python
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
```

### Test with Parameters
```python
def test_create_item():
    response = client.post(
        "/items/",
        json={"name": "Foo", "price": 50.5}
    )
    assert response.status_code == 200
    assert response.json()["name"] == "Foo"
```

## Async Support

### Async Endpoints
```python
@app.get("/async-items/")
async def get_async_items():
    await asyncio.sleep(1)  # Simulate async operation
    return [{"id": 1, "name": "Item 1"}]
```

### Async Dependencies
```python
async def get_query_value():
    return "async_query_value"

@app.get("/items/")
async def read_items(query: str = Depends(get_query_value)):
    return {"query": query}
```

## APIRouter

### Creating Routers
```python
from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/")
def get_users():
    pass

@router.get("/{user_id}")
def get_user(user_id: int):
    pass
```

### Including Routers
```python
app.include_router(router)
```

## Database Integration (SQLAlchemy)

### Database Connection
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
```

### Database Dependency
```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    pass
```

## Environment Variables

### Using Pydantic Settings
```python
from pydantic import BaseSettings

class Settings(BaseSettings):
    app_name: str = "FastAPI App"
    admin_email: str
    database_url: str
    secret_key: str

    class Config:
        env_file = ".env"

settings = Settings()
```

## Response Classes

### Custom Response
```python
from fastapi.responses import HTMLResponse, RedirectResponse

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return "<h1>Hello HTML</h1>"

@app.get("/redirect")
def redirect_to_docs():
    return RedirectResponse(url="/docs")
```

## Lifespan Events

### Startup and Shutdown
```python
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("Starting up...")
    yield
    # Shutdown
    print("Shutting down...")

app = FastAPI(lifespan=lifespan)
```

## Custom Request and Response

### Custom Request
```python
from starlette.requests import Request

@app.get("/")
async def get_raw_request(request: Request):
    return {"headers": dict(request.headers)}
```

### Streaming Response
```python
from fastapi.responses import StreamingResponse

def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"

@app.get("/")
def main():
    return StreamingResponse(fake_video_streamer())
```

## OpenAPI Customization

### Custom Tags
```python
tags_metadata = [
    {
        "name": "users",
        "description": "Operations with users."
    },
    {
        "name": "items",
        "description": "Operations with items."
    }
]

app = FastAPI(openapi_tags=tags_metadata)
```

### Custom Operation ID
```python
@app.get("/items/{item_id}", operation_id="get_specific_item_by_id")
def read_item(item_id: int):
    return {"item_id": item_id}
```

## Deployment

### Uvicorn Command
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### With Reload (Development)
```bash
uvicorn main:app --reload
```

### With Custom Config
```python
# config.py
import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        workers=4,
        log_level="info",
        reload=True
    )
```