from fastapi import FastAPI, Depends
from typing import Optional

from database import engine, SessionLocal
from sqlalchemy.orm import Session
import models
import schemas

app = FastAPI()
models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/dbreq")
def root(requests: schemas.Blog, db: Session = Depends(get_db)):
    new_blog = models.Blog(title=requests.title, body=requests.Name)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
