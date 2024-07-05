from sqlalchemy.orm import Session
from app.database.models import Company
from app.api.schemas.company import CompanyCreate, CompanyUpdate


def get_company(*, db: Session, company_id: int):
    return db.query(Company).filter(Company.id == company_id).first()


def get_companies(*, db: Session, skip: int = 0, limit: int = 10):
    return db.query(Company).offset(skip).limit(limit).all()


def create_company(*, db: Session, company: CompanyCreate):
    db_company = Company(
        name=company.name,
        url=company.url,
        address=company.address,
        timezone=company.timezone,
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company


def update_company(*, db: Session, company_id: int, company: CompanyUpdate):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None:
        return None
    db_company.name = company.name
    db_company.url = company.url
    db_company.address = company.address
    db_company.timezone = company.timezone
    db.commit()
    db.refresh(db_company)
    return db_company


def delete_company(*, db: Session, company_id: int):
    db_company = db.query(Company).filter(Company.id == company_id).first()
    if db_company is None:
        return None
    db.delete(db_company)
    db.commit()
    return db_company
