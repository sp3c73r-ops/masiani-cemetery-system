from datetime import date
from typing import Optional

from pydantic import BaseModel


class GraveMapResponse(BaseModel):
    id: int
    grave_number: str
    latitude: str
    longitude: str
    status: str

    class Config:
        orm_mode = True


class GraveLocationInfo(BaseModel):
    id: int
    grave_number: str
    latitude: str
    longitude: str
    status: str

    class Config:
        orm_mode = True


class DeceasedMapResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: Optional[date]
    death_date: Optional[date]
    grave: GraveLocationInfo

    class Config:
        orm_mode = True
