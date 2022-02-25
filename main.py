from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class Blog(BaseModel):
    title: str
    Name: "str"


@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/fetch")
def root():
    return {"message": "just fetching the request"}


@app.get("/query/{idi}")
def root(message: str, idi, name: Optional[str] = None):
    return {"message": f'"{message} just fetching the request {idi}"'}


@app.post("/base")
def root(requests: Blog):
    return {"message": f'"{requests.Name} deepanshu"'}


@app.post("/base2")
def root(requests: Blog):
    return {"message": f'"{requests.Name} deepanshu"'}