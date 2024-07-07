from typing import List
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException
from app.database.connection import get_db
from app.api.crud import company as crud_company
from app.api.schemas.company import CompanyBase, CompanyCreate, CompanyUpdate, CompanyOut

router = APIRouter()


@router.get(
    "/{company_id}",
    response_model=CompanyBase,
)
def get_company(company_id: int, db: Session = Depends(get_db)):
    db_company = crud_company.get_company(db=db, company_id=company_id)
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company


@router.get("/companies/", response_model=List[CompanyOut])
def read_companies(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    companies = crud_company.get_companies(db=db, skip=skip, limit=limit)
    return companies


@router.post(
    "/",
    response_model=CompanyBase,
)
def create_company(company: CompanyCreate, db: Session = Depends(get_db)):
    return crud_company.create_company(db=db, company=company)


@router.put("/companies/{company_id}", response_model=CompanyBase)
def update_company(
    company_id: int, company: CompanyUpdate, db: Session = Depends(get_db)
):
    db_company = crud_company.update_company(
        db=db, company_id=company_id, company=company
    )
    if db_company is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return db_company


@router.delete("/companies/{company_id}", response_model=bool)
def delete_company(company_id: int, db: Session = Depends(get_db)):
    success = crud_company.delete_company(db=db, company_id=company_id)
    if not success:
        raise HTTPException(status_code=404, detail="Company not found")
    return success
