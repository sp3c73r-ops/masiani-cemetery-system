from pydantic import BaseModel


class DashboardStatsResponse(BaseModel):
    total_graves: int
    identified_graves: int
    supposed_graves: int
    total_deceased: int
    total_photos: int
