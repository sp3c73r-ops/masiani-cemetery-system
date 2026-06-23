from datetime import date
from typing import Optional

from pydantic import BaseModel


class GraveInfo(BaseModel):
    id: int
    grave_number: str
    latitude: str
    longitude: str
    status: str

    class Config:
        orm_mode = True


class DeceasedSearchResult(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: Optional[date]
    death_date: Optional[date]
    grave: GraveInfo

    class Config:
        orm_mode = True
