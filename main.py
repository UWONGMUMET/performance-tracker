from fastapi import FastAPI
from routers import auth
from core.config import settings

app = FastAPI(debug=settings.DEBUG)

app.include_router(auth.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

