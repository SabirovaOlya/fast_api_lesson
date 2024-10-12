from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from utils.users import users

router = APIRouter(prefix="/users", tags=["USERS"])
router.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def user_list(request: Request):
    context = {'users': users}
    return templates.TemplateResponse(request=request, name="apps/user/single.html", context=context)


@router.get("/form", response_class=HTMLResponse)
async def user_single(request: Request):
    return templates.TemplateResponse(request=request, name="apps/user/form.html")


@router.get("/{id}", response_class=HTMLResponse)
async def user_single(request: Request, id: int):
    user = None
    for u in users:
        if u['id'] == id:
            user = u
            break
    context = {'user': user}
    return templates.TemplateResponse(request=request, name="apps/user/single.html", context=context)
