from fastapi import APIRouter, Depends, status, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from auth.auth_handler import verify_password, create_access_token, create_refresh_token
from auth.deps import get_current_user
from users.models import User
from users.schemas import CreateUser, ReadUser
from sqlalchemy.orm import Session
from core.database import get_db
from users import crud

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.get('/me', summary='Get details of currently logged in user', response_model=ReadUser)
async def get_me(user: User = Depends(get_current_user)):
    return user


@router.post('/signup', summary="Create new user")
async def create_user(user_in: CreateUser, db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db=db, username=user_in.username)
    if user is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="User with this username already exist"
            )
    return crud.create_user(db=db, user=user_in)


@router.post('/login', summary="Create access and refresh tokens for user")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db=db, username=form_data.username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    hashed_pass = user.password
    if not verify_password(form_data.password, hashed_pass):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect email or password"
        )

    return {
        "access_token": create_access_token(user.id),
        "refresh_token": create_refresh_token(user.id),
    }

