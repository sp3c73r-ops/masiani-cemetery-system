from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.models.models import User
from app.routes.auth import get_current_user, get_db
from app.schemas.search import DeceasedSearchResult
from app.services.search_service import search_deceased

router = APIRouter(prefix="/search", tags=["search"])


@router.get("/deceased", response_model=list[DeceasedSearchResult])
def search_deceased_route(
    q: str = Query(..., min_length=1),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    results = search_deceased(db, q)
    return results
