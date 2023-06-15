from pydantic import PositiveInt
from sqlalchemy import select
from sqlalchemy.orm import Session

import model
import schema


def post_item(item_create: schema.ItemCreate, db: Session) -> model.Item:
    item = model.Item(title=item_create.title, user_id=item_create.user_id)
    db.add(item)
    db.commit()
    return item


def get_item(db: Session) -> list[model.Item]:
    return db.query(model.Item).all()


def get_item_id(id: PositiveInt, db: Session) -> model.Item | None:
    return db.query(model.Item).filter(model.Item.id == id).first()


def post_user(user_create: schema.UserCreate, db: Session) -> model.User:
    user = model.User(email=user_create.email)
    db.add(user)
    db.commit()
    return user


def get_user(db: Session) -> list[model.User]:
    return db.query(model.User).all()


def get_user_id(id: PositiveInt, db: Session) -> model.User | None:
    return db.query(model.User).filter(model.User.id == id).first()
