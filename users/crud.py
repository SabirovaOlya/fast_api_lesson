from sqlalchemy.orm import Session

from auth.auth_handler import get_hashed_password
from users.schemas import CreateUser
from users.models import User


def create_user(db: Session, user: CreateUser):
    hashed_password: str = get_hashed_password(user.password)

    db_user = User(
        fullname=user.fullname,
        username=user.username,
        email=user.email,
        phone=user.phone,
        position=user.position,
        location=user.location,
        password=hashed_password,
        birthday=user.birthday
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session, user_id: str):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()


def login_user(db: Session, username: str, password: str):
    user = db.query(User).filter(User.username == username).first()
    if user.password == password:
        return user
    else:
        return {
            "message": "Wrong login data"
        }


def get_users(db: Session):
    return db.query(User).all()
