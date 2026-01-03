from fastapi import FastAPI

app = FastAPI(title="IT Asset Management System")

@app.get("/")
def root():
    return {"message": "IT Asset Management API is running"}

@app.get("/health")
def health():
    return {"status": "ok"}

