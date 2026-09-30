import os

from fastapi import FastAPI, Query

VERSION = os.getenv("APP_VERSION", "1.0.0")

app = FastAPI(title="Cloudalpha Python demo API", version=VERSION)


@app.get("/health")
def health() -> dict:
    return {"status": "ok", "version": VERSION}


@app.get("/api/greeting")
def greeting(name: str = Query(default="world", max_length=50)) -> dict:
    return {"message": f"Hello, {name}!"}
