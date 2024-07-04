from sqlalchemy.orm import Session
from app.api.schemas.company import CompanyBase
from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/{id}",
    response_model=CompanyBase,
)
def get_company(company_id: int):
    # return db.query(models.Company).filter(models.Company.id == company_id).first()
    return {
        "id": company_id,
        "name": "company 1",
        "url": "c1",
        "address": "pereira",
        "timezone": "America/Bogota",
    }


# def get_companies(db: Session, skip: int = 0, limit: int = 10):
#     return db.query(models.Company).offset(skip).limit(limit).all()


# def create_company(db: Session, company: schemas.CompanyCreate):
#     db_company = models.Company(**company.dict())
#     db.add(db_company)
#     db.commit()
#     db.refresh(db_company)
#     return db_company


# def update_company(db: Session, company_id: int, company: schemas.CompanyUpdate):
#     db_company = get_company(db, company_id)
#     if db_company is None:
#         return None
#     for key, value in company.dict(exclude_unset=True).items():
#         setattr(db_company, key, value)
#     db.commit()
#     db.refresh(db_company)
#     return db_company


# def delete_company(db: Session, company_id: int):
#     db_company = get_company(db, company_id)
#     if db_company is None:
#         return None
#     db.delete(db_company)
#     db.commit()
#     return db_company
