from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.api.schemas.user import UserCreate, UserUpdate
from app.database.models import User
from app.api.utils.auth import get_password_hash


def create_user(db: Session, user: UserCreate) -> User:
    try:
        hashed_password = get_password_hash(user.password)
        db_user = User(
            identification=user.identification,
            name=user.name,
            password=hashed_password,
            phone=user.phone,
            company_id=user.company_id,
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def get_user(db: Session, user_id: int) -> User:
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_identification(db: Session, identification: str) -> User:
    return db.query(User).filter(User.identification == identification).first()


def get_users(db: Session, skip: int = 0, limit: int = 10) -> List[User]:
    return db.query(User).offset(skip).limit(limit).all()


def update_user(db: Session, user_id: int, user: UserUpdate) -> User:
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return None
        if user.password:
            user.password = get_password_hash(user.password)
        for key, value in user.model_dump(exclude_unset=True).items():
            setattr(db_user, key, value)
        db.commit()
        db.refresh(db_user)
        return db_user
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_user(db: Session, user_id: int) -> bool:
    try:
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user is None:
            return False
        db.delete(db_user)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise e
