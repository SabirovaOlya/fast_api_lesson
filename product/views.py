import uuid
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from product import crud
from product.schemas import CreateCategory, CreateProduct
from core.database import get_db

category_router = APIRouter(prefix="/categories", tags=["Category"])
product_router = APIRouter(prefix="/products", tags=["Product"])


@category_router.get("/")
def get_list(db: Session = Depends(get_db)):
    return crud.get_category_list(db=db)


@category_router.post("/")
def create_category(category: CreateCategory, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)


@category_router.get("/{id}")
def get_list(id: str, db: Session = Depends(get_db)):
    return crud.get_category(db=db, category_id=id)


@product_router.get("/")
def get_product_list(db: Session = Depends(get_db)):
    return crud.get_product_list(db=db)


@product_router.post("/")
def create_product(product: CreateProduct, db: Session = Depends(get_db)):
    return crud.create_product(db=db, product=product)


@product_router.get("/{id}")
def get_product_list(id: str, db: Session = Depends(get_db)):
    return crud.get_product(db=db, product_id=id)

