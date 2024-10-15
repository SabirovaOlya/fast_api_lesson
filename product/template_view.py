from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from core.database import get_db
from product import crud

router = APIRouter(prefix="/temp_product")
router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def user_list(request: Request, db: Session = Depends(get_db)):
    products = crud.get_product_list(db=db)
    categories = crud.get_categories(db=db)
    context = {'products': products, 'categories': categories}
    print(categories)
    return templates.TemplateResponse(request=request, name="apps/product/list.html", context=context)


@router.get("/{product_id}", name='product_single', response_class=HTMLResponse)
async def user_single(request: Request, product_id: str, db: Session = Depends(get_db)):
    product = crud.get_product(db=db, product_id=product_id)
    context = {'product': product}
    return templates.TemplateResponse(request=request, name="apps/product/single.html", context=context)
