from fastapi import FastAPI
from . import models
from .database import engine

print(">>> MAIN.PY LOADED")
print(">>> MODELS:", models.Base.metadata.tables.keys())

app = FastAPI(title="IT Asset Management System")
models.Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "IT Asset Management API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

