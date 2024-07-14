from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.api.crud import media as crud_media
from app.api.schemas.media import Media, MediaCreate, MediaUpdate

router = APIRouter()


@router.post("/", response_model=Media)
def create_media(media: MediaCreate, db: Session = Depends(get_db)):
    return crud_media.create_media(db=db, media=media)


@router.get("/{media_id}", response_model=Media)
def read_media(media_id: int, db: Session = Depends(get_db)):
    db_media = crud_media.get_media(db=db, media_id=media_id)
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return db_media


@router.get("/", response_model=List[Media])
def read_media(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud_media.get_all_media(db=db, skip=skip, limit=limit)


@router.put("/{media_id}", response_model=Media)
def update_media(media_id: int, media: MediaUpdate, db: Session = Depends(get_db)):
    db_media = crud_media.update_media(db=db, media_id=media_id, media=media)
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return db_media


@router.delete("/{media_id}", response_model=Media)
def delete_media(media_id: int, db: Session = Depends(get_db)):
    db_media = crud_media.delete_media(db=db, media_id=media_id)
    if db_media is None:
        raise HTTPException(status_code=404, detail="Media not found")
    return db_media
