from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.models import User
from app.routes.auth import get_current_user, get_db
from app.schemas.map import DeceasedMapResponse, GraveMapResponse
from app.services.map_service import get_all_graves, get_deceased_location

router = APIRouter(prefix="/map", tags=["map"])


@router.get("/graves", response_model=list[GraveMapResponse])
def list_graves(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_all_graves(db)


@router.get("/deceased/{deceased_id}", response_model=DeceasedMapResponse)
def get_deceased_map_location(
    deceased_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deceased = get_deceased_location(db, deceased_id)
    if not deceased:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deceased not found")
    return deceased
