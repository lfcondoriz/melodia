from fastapi import FastAPI
from app.routers.auth import router as auth_router

app = FastAPI(title="Melodia API")

@app.get("/health")
def health():
    return {"status": "ok"}

app.include_router(auth_router)