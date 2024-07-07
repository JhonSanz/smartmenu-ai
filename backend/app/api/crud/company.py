from typing import List
from sqlalchemy.orm import Session
from app.database.models import Company
from app.api.schemas.company import CompanyCreate, CompanyUpdate
from sqlalchemy.exc import SQLAlchemyError


def get_company(*, db: Session, company_id: int) -> Company:
    return db.query(Company).filter(Company.id == company_id).first()


def get_companies(*, db: Session, skip: int = 0, limit: int = 10) -> List[Company]:
    return db.query(Company).offset(skip).limit(limit).all()


def create_company(*, db: Session, company: CompanyCreate) -> Company:
    try:
        db_company = Company(**company.model_dump())
        db.add(db_company)
        db.commit()
        db.refresh(db_company)
        return db_company
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def update_company(*, db: Session, company_id: int, company: CompanyUpdate) -> Company:
    try:
        db_company = db.query(Company).filter(Company.id == company_id).first()
        if db_company is None:
            return None
        for key, value in company.model_dump().items():
            setattr(db_company, key, value)
        db.commit()
        db.refresh(db_company)
        return db_company
    except SQLAlchemyError as e:
        db.rollback()
        raise e


def delete_company(*, db: Session, company_id: int) -> bool:
    try:
        db_company = db.query(Company).filter(Company.id == company_id).first()
        if db_company is None:
            return False
        db.delete(db_company)
        db.commit()
        return True
    except SQLAlchemyError as e:
        db.rollback()
        raise e
