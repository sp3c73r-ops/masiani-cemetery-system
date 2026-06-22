from datetime import timedelta

from jose import JWTError
from sqlalchemy.orm import Session

from app.models.models import User
from app.utils.security import (
    ACCESS_TOKEN_EXPIRE_MINUTES,
    create_access_token,
    get_password_hash,
    verify_password,
)


def get_user_by_email(db: Session, email: str) -> User | None:
    return db.query(User).filter(User.email == email).first()


def authenticate_user(db: Session, email: str, password: str) -> User | None:
    user = get_user_by_email(db, email)
    if not user or not verify_password(password, user.password):
        return None
    return user


def create_admin_user(db: Session) -> User:
    admin = get_user_by_email(db, "admin@masiani.cd")
    if admin:
        return admin

    hashed_password = get_password_hash("admin123")
    new_user = User(
        nom="Administrateur",
        email="admin@masiani.cd",
        password=hashed_password,
        role="admin",
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def create_token_for_user(user: User) -> dict:
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": str(user.id), "email": user.email, "role": user.role},
        expires_delta=access_token_expires,
    )
    return {"access_token": access_token, "token_type": "bearer"}
