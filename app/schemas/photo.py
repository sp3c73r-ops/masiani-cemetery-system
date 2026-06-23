from datetime import datetime

from pydantic import BaseModel


class PhotoResponse(BaseModel):
    id: int
    grave_id: int
    file_name: str
    file_path: str
    created_at: datetime

    class Config:
        orm_mode = True
