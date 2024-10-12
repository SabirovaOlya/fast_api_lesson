from sqlalchemy.orm import Session
from product.models import Category, Product
from product.schemas import CreateCategory, CreateProduct


def create_category(db: Session, category: CreateCategory):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def get_category(db: Session, category_id: str):
    return db.query(Category).filter(Category.id == category_id).first()


def get_categories(db: Session):
    return db.query(Category).all()


def create_product(db: Session, product: CreateProduct):
    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        count=product.count,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product(db: Session, product_id: str):
    return db.query(Product).filter(Product.id == product_id).first()


def get_product_list(db: Session):
    return db.query(Product).all()
