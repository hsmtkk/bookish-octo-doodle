from fastapi import Depends, FastAPI, HTTPException, Path, status
from pydantic import EmailStr, PositiveInt
from sqlalchemy.orm import Session

import crud
import model
import schema
from database import SessionLocal, engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/item", response_model=schema.Item)
def post_item(item_create: schema.ItemCreate, db: Session = Depends(get_db)):
    item = crud.post_item(item_create, db)
    return schema.Item(id=item.id, title=item.title, user_id=item.user_id)


@app.get("/item", response_model=list[schema.Item])
def get_item(db: Session = Depends(get_db)):
    items = crud.get_item(db)
    resp = list()
    for item in items:
        resp.append(schema.Item(id=item.id, title=item.title, user_id=item.user_id))
    return resp


@app.get("/item/{id}", response_model=schema.Item)
def get_item_id(id: PositiveInt = Path(), db: Session = Depends(get_db)):
    item = crud.get_item_id(id, db)
    if item is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return schema.Item(id=item.id, title=item.title, user_id=item.user_id)


@app.post("/user", response_model=schema.User)
def post_user(user_create: schema.UserCreate, db: Session = Depends(get_db)):
    user = crud.post_user(user_create, db)
    return schema.User(id=user.id, email=EmailStr(user.email), items=user.items)


@app.get("/user", response_model=list[schema.User])
def get_user(db: Session = Depends(get_db)):
    users = crud.get_user(db)
    resp = list()
    for user in users:
        resp.append(
            schema.User(id=user.id, email=EmailStr(user.email), items=user.items)
        )
    return resp


@app.get("/user/{id}")
def get_user_id(id: PositiveInt = Path(), db: Session = Depends(get_db)):
    user = crud.get_user_id(id, db)
    if user is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND)
    return schema.User(id=user.id, email=EmailStr(user.email), items=user.items)
