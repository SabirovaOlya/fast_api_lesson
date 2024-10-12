import uvicorn
from fastapi import FastAPI
from sqladmin import Admin
from core.database import engine
from core.base import Base
from users.views import router as user_router
from product.views import category_router, product_router
from product.template_view import router as template_product_router
from core.admin import ProductAdmin, CategoryAdmin
from auth.auth import router as auth_router


app = FastAPI()
admin = Admin(app, engine)
admin.add_view(ProductAdmin)
admin.add_view(CategoryAdmin)

app.include_router(user_router)
app.include_router(category_router)
app.include_router(product_router)
app.include_router(template_product_router)
app.include_router(auth_router)

Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
