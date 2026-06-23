from pydantic import BaseModel


class GraveMapResponse(BaseModel):
    id: int
    grave_number: str
    latitude: str
    longitude: str
    status: str

    class Config:
        orm_mode = True
