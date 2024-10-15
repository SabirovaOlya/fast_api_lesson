from slugify import slugify
from sqlalchemy import func
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
    categories_with_count = db.query(
        Category,
        func.count(Product.id).label('product_count')
    ).outerjoin(Product).group_by(Category.id).all()

    categories = []
    for category, product_count in categories_with_count:
        category.product_count = product_count
        categories.append(category)

    return categories


def create_product(db: Session, product: CreateProduct):
    # product_slug = slugify(product.name)
    # counter = 1
    # while db.query(Product).filter(Product.slug == product_slug).first() is not None:
    #     product_slug = slugify(f"{product.name}-{counter}")
    #     counter += 1

    db_product = Product(
        name=product.name,
        price=product.price,
        description=product.description,
        count=product.count,
        category_id=product.category_id,
        # slug=product_slug
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def get_product(db: Session, product_id: str):
    return db.query(Product).filter(Product.id == product_id).first()


def get_product_list(db: Session):
    return db.query(Product).all()
