from datetime import date
from typing import Annotated
from uuid import UUID

from annotated_types import MinLen, MaxLen
from pydantic import BaseModel


class CreateUser(BaseModel):
    fullname: Annotated[str, MinLen(3), MaxLen(100)]
    username: Annotated[str, MinLen(3), MaxLen(100)]
    position: Annotated[str, MinLen(3), MaxLen(25)]
    location: Annotated[str, MinLen(5), MaxLen(255)]
    email: Annotated[str, MinLen(5), MaxLen(100)]
    phone: Annotated[str, MinLen(3), MaxLen(100)]
    password: Annotated[str, MinLen(3), MaxLen(100)]
    birthday: date

    class Config:
        orm_mode = True


class UserBaseModel(BaseModel):
    id: UUID

    class Config:
        orm_mode = True


class ReadUser(UserBaseModel):
    fullname: Annotated[str, MinLen(3), MaxLen(100)]
    username: Annotated[str, MinLen(3), MaxLen(100)]
    email: Annotated[str, MinLen(5), MaxLen(100)]
    phone: Annotated[str, MinLen(3), MaxLen(100)]
    birthday: date

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    email: Annotated[str, MinLen(5), MaxLen(100)]
    password: Annotated[str, MinLen(3), MaxLen(100)]

