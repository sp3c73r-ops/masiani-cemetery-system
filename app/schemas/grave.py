from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


class GraveBase(BaseModel):
    grave_number: str = Field(..., min_length=1)
    latitude: float
    longitude: float
    status: Literal["identifiee", "supposee", "inconnue", "abandonnee"]


class CreateGrave(GraveBase):
    pass


class UpdateGrave(BaseModel):
    grave_number: Optional[str] = Field(None, min_length=1)
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    status: Optional[Literal["identifiee", "supposee", "inconnue", "abandonnee"]]


class GraveResponse(GraveBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
