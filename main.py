from fastapi import FastAPI
from app.routes import analysis

app = FastAPI(title="Text Analysis Service")

app.include_router(analysis.router)

@app.get("/")
def root():
    return {"status": "ok"}
