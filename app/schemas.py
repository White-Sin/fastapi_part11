from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class AdvertisementBase(BaseModel):
    title: str
    description: str
    price: float
    author: str

class AdvertisementCreate(AdvertisementBase):
    pass

class AdvertisementUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None
    author: Optional[str] = None

class AdvertisementInDB(AdvertisementBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class Advertisement(AdvertisementInDB):
    pass
