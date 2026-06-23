from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.models import User
from app.routes.auth import get_current_user, get_db
from app.schemas.navigation import DeceasedNavigationResponse
from app.services.navigation_service import build_navigation_url, get_deceased_with_grave

router = APIRouter(prefix="/navigation", tags=["navigation"])


@router.get("/deceased/{deceased_id}", response_model=DeceasedNavigationResponse)
def get_deceased_navigation(
    deceased_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deceased = get_deceased_with_grave(db, deceased_id)
    if not deceased:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deceased not found")

    if not deceased.grave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grave not found")

    navigation_url = build_navigation_url(deceased.grave.latitude, deceased.grave.longitude)
    return {
        "id": deceased.id,
        "first_name": deceased.first_name,
        "last_name": deceased.last_name,
        "birth_date": deceased.birth_date,
        "death_date": deceased.death_date,
        "grave": deceased.grave,
        "navigation_url": navigation_url,
    }
