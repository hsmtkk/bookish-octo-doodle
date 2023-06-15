from typing import Sequence

from pydantic import BaseModel, EmailStr, PositiveInt


class ItemBase(BaseModel):
    title: str
    user_id: PositiveInt


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: PositiveInt

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: PositiveInt
    items: Sequence[Item]

    class Config:
        orm_mode = True
