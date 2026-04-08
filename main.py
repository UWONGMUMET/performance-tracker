from fastapi import FastAPI
from routers import auth, user, dashboard
from core.config import settings

app = FastAPI(debug=settings.DEBUG)

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(dashboard.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}

