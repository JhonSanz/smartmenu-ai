from fastapi import APIRouter

from app.api.routes import company

api_router = APIRouter()

api_router.include_router(company.router, prefix="/company", tags=["company"])
