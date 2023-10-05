from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import time
from app.routers import auth
from app.routers import transaction

app = FastAPI()
app.include_router(auth.auth)
app.include_router(transaction.transaction)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def middleware(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


@app.get("/")
def welcome():
    return "Welcome to Restaurant reservation API"
