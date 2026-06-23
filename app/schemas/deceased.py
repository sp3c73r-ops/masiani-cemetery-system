from datetime import date
from typing import Optional

from pydantic import BaseModel, Field


class DeceasedBase(BaseModel):
    first_name: str = Field(..., min_length=1)
    last_name: str = Field(..., min_length=1)
    birth_date: date
    death_date: date
    grave_id: int


class CreateDeceased(DeceasedBase):
    pass


class UpdateDeceased(BaseModel):
    first_name: Optional[str] = Field(None, min_length=1)
    last_name: Optional[str] = Field(None, min_length=1)
    birth_date: Optional[date] = None
    death_date: Optional[date] = None
    grave_id: Optional[int] = None


class DeceasedResponse(DeceasedBase):
    id: int
    grave_number: str

    class Config:
        orm_mode = True
