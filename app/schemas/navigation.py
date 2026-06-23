from datetime import date
from typing import Optional

from pydantic import BaseModel


class NavigationGraveInfo(BaseModel):
    id: int
    grave_number: str
    latitude: str
    longitude: str
    status: str

    class Config:
        orm_mode = True


class DeceasedNavigationResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    birth_date: Optional[date]
    death_date: Optional[date]
    grave: NavigationGraveInfo
    navigation_url: str

    class Config:
        orm_mode = True
