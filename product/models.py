from sqlalchemy import String, Float, Integer, UUID, ForeignKey
from sqlalchemy.orm import mapped_column, Mapped, relationship
from core.base import TimeModel


class Category(TimeModel):
    __tablename__ = 'categories'

    name: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    products: Mapped[list["Product"]] = relationship(back_populates="category", cascade="all, delete-orphan", lazy='selectin')

    def __str__(self):
        return self.name


class Product(TimeModel):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(String, nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    description: Mapped[str | None] = mapped_column(String, nullable=True)
    # slug: Mapped[str] = mapped_column(String, nullable=False, unique=True)
    count: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    category_id: Mapped[UUID] = mapped_column(UUID, ForeignKey("categories.id"))

    category: Mapped["Category"] = relationship(back_populates="products", lazy="selectin")

    def __str__(self):
        return self.name
