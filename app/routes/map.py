from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.models.models import User
from app.routes.auth import get_current_user, get_db
from app.schemas.map import GraveMapResponse
from app.services.map_service import get_all_graves

router = APIRouter(prefix="/map", tags=["map"])


@router.get("/graves", response_model=list[GraveMapResponse])
def list_graves(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_all_graves(db)
