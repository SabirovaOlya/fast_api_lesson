from slugify import slugify
from sqladmin import ModelView
from product.models import Product, Category


class ProductAdmin(ModelView, model=Product):
    column_list = ['id', 'name']
    form_excluded_columns = ['deleted_at', 'created_at', 'updated_at']


class CategoryAdmin(ModelView, model=Category):
    column_list = ['id', 'name']
    form_rules = ["name",]

    can_export = False
