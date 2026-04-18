from fastapi import FastAPI
from backend.app.database import engine, Base
from backend.app.router import router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Melodia API")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Melodia API funcionando"}