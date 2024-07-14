from pydantic import BaseModel


class MediaBase(BaseModel):
    url: str


class MediaCreate(MediaBase):
    pass


class MediaUpdate(MediaBase):
    pass


class Media(MediaBase):
    id: int

    class Config:
        orm_mode = True
