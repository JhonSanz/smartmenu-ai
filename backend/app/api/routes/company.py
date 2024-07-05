from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.connection import get_db
from app.api.crud import company as crud_company
from app.api.schemas.company import CompanyBase, CompanyCreate

router = APIRouter()


@router.get(
    "/{id}",
    response_model=CompanyBase,
)
def get_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud_company.get_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company


@router.post(
    "/",
    response_model=CompanyBase,
)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return crud_company.create_company(db=db, company=company)
