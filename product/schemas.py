from typing import Annotated
from uuid import UUID as UUID4
from annotated_types import MinLen, MaxLen, Gt
from pydantic import BaseModel


class CreateCategory(BaseModel):
    name: Annotated[str, MinLen(4), MaxLen(25)]


class CreateProduct(BaseModel):
    name: Annotated[str, MinLen(5), MaxLen(25)]
    description: Annotated[str, MinLen(5), MaxLen(255)]
    price: Annotated[float, Gt(0)]
    count: Annotated[int, Gt(0)]
    category_id: UUID4

    class Config:
        from_attributes = True
