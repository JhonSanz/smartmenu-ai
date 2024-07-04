from pydantic import BaseModel
from typing import List, Optional


class CompanyBase(BaseModel):
    name: str
    url: str
    address: str
    timezone: str


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(CompanyBase):
    pass


# class CompanyOut(CompanyBase):
#     id: int

#     class Config:
#         orm_mode = True
