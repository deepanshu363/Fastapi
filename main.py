from fastapi import FastAPI
from typing import Optional

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/fetch")
def root():
    return {"message": "just fetching the request"}


@app.get("/query/{idi}")
def root(message: str, idi, name: Optional[str] = None):
    return {"message": f'"{message} just fetching the request {idi}"'}
