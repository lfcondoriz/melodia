from fastapi import FastAPI

from database import check_db_connection

app = FastAPI(title="Melodia API")


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