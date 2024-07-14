from sqlalchemy.orm import Session
from app.database.models import Media
from app.api.schemas.media import MediaCreate, MediaUpdate


def get_media(*, db: Session, media_id: int):
    return db.query(Media).filter(Media.id == media_id).first()


def get_all_media(*, db: Session, skip: int = 0, limit: int = 10):
    return db.query(Media).offset(skip).limit(limit).all()


def create_media(*, db: Session, media: MediaCreate):
    db_media = Media(**media.model_dump())
    db.add(db_media)
    db.commit()
    db.refresh(db_media)
    return db_media


def update_media(*, db: Session, media_id: int, media: MediaUpdate):
    db_media = db.query(Media).filter(Media.id == media_id).first()
    if not db_media:
        return None
    for key, value in media.model_dump().items():
        setattr(db_media, key, value)
    db.commit()
    db.refresh(db_media)
    return db_media


def delete_media(*, db: Session, media_id: int):
    db_media = db.query(Media).filter(Media.id == media_id).first()
    if not db_media:
        return None
    db.delete(db_media)
    db.commit()
    return db_media
