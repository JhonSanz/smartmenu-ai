from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from app.database.connection import get_db
from app.api.crud.auth import (
    authenticate_user,
    create_access_token,
    ACCESS_TOKEN_EXPIRE_MINUTES,
)
from app.api.schemas.auth import Token, AuthRequest


router = APIRouter()


@router.post("/token", response_model=Token)
async def login_for_access_token(
    auth_request: AuthRequest, db: Session = Depends(get_db),
):
    user = authenticate_user(
        db=db, identification=auth_request.username, password=auth_request.password
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.identification}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}
