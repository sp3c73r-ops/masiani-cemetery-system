from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.models import Grave, User
from app.schemas.grave import CreateGrave, GraveResponse, UpdateGrave
from app.services.grave_service import (
    create_grave,
    delete_grave,
    get_grave,
    get_graves,
    update_grave,
)
from app.routes.auth import get_current_user, get_db

router = APIRouter(prefix="/graves", tags=["graves"])


@router.post("/", response_model=GraveResponse, status_code=status.HTTP_201_CREATED)
def create_grave_route(
    grave_data: CreateGrave,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return create_grave(db, grave_data)


@router.get("/", response_model=list[GraveResponse])
def list_graves(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    return get_graves(db)


@router.get("/{grave_id}", response_model=GraveResponse)
def get_grave_route(
    grave_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    grave = get_grave(db, grave_id)
    if not grave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grave not found")
    return grave


@router.put("/{grave_id}", response_model=GraveResponse)
def update_grave_route(
    grave_id: int,
    grave_data: UpdateGrave,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    grave = get_grave(db, grave_id)
    if not grave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grave not found")
    return update_grave(db, grave, grave_data)


@router.delete("/{grave_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_grave_route(
    grave_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    grave = get_grave(db, grave_id)
    if not grave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grave not found")
    delete_grave(db, grave)
    return None
