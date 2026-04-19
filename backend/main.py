from fastapi import FastAPI

from database import check_db_connection
from routers import auth

app = FastAPI(title="Melodia API")

app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Melodia API is running 🎵"}


@app.get("/health")
def health():
    db_ok = check_db_connection()
    return {
        "status": "ok" if db_ok else "degraded",
        "database": "connected" if db_ok else "unreachable",
    }