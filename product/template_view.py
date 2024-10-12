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
    context = {'products': products}
    return templates.TemplateResponse(request=request, name="apps/product/list.html", context=context)


@router.get("/{product_id}", response_class=HTMLResponse)
async def user_single(request: Request, product_id: str):
    user = None
    context = {'user': user}
    return templates.TemplateResponse(request=request, name="apps/product/single.html", context=context)
