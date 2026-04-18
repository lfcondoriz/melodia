from fastapi import FastAPI

app = FastAPI(title="Melodia API")

@app.get("/")
def root():
    return {"message": "Melodia API funcionando"}