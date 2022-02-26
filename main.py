from fastapi import FastAPI, Depends, Response, status
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
def root(tablename: str, requests: schemas.Blog, db: Session = Depends(get_db)):
    if tablename == "Table1":
        new_blog = models.Table1(title=requests.title, body=requests.Name)
    elif tablename == "Table2":
        new_blog = models.Table2(title=requests.title, body=requests.Name)
    else:
        return "NO SUCH TABLE EXIST AT ALL...."

    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


@app.get("/table1")
def root(ids: int, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Table1).filter(models.Table1.id == ids).first()
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "NOT FOUND!!!😩"
    return blogs


@app.get("/table2")
def root(ids: int, response: Response, db: Session = Depends(get_db)):
    blogs = db.query(models.Table2).filter(models.Table2.id == ids).first()
    if not blogs:
        response.status_code = status.HTTP_404_NOT_FOUND
        return "NOT FOUND!!!😩"
    return blogs


@app.put("/update")
def root(ids: int, response: Response, requests: schemas.Blog, db: Session = Depends(get_db)):
    db.query(models.Table1).filter(models.Table1.id == ids).update({"title": requests.title, "body": requests.Name})

    db.commit()
    return "updates"


@app.delete("/delete")
def root(ids: int, response: Response, db: Session = Depends(get_db)):
    db.query(models.Table1).filter(models.Table1.id == ids).delete()
    db.commit()
    return "Delete"
