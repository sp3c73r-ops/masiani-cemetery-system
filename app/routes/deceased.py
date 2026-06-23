from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.models.models import Deceased, Grave, User
from app.routes.auth import get_current_user, get_db
from app.schemas.deceased import CreateDeceased, DeceasedResponse, UpdateDeceased
from app.services.deceased_service import (
    create_deceased,
    delete_deceased,
    get_deceased,
    get_deceased_list,
    update_deceased,
)

router = APIRouter(prefix="/deceased", tags=["deceased"])


@router.post("/", response_model=DeceasedResponse, status_code=status.HTTP_201_CREATED)
def create_deceased_route(
    deceased_data: CreateDeceased,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    try:
        deceased = create_deceased(db, deceased_data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    return {
        "id": deceased.id,
        "first_name": deceased.first_name,
        "last_name": deceased.last_name,
        "birth_date": deceased.birth_date,
        "death_date": deceased.death_date,
        "grave_id": deceased.grave_id,
        "grave_number": deceased.grave.grave_number,
    }


@router.get("/", response_model=list[DeceasedResponse])
def list_deceased(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deceased_list = get_deceased_list(db)
    return [
        {
            "id": deceased.id,
            "first_name": deceased.first_name,
            "last_name": deceased.last_name,
            "birth_date": deceased.birth_date,
            "death_date": deceased.death_date,
            "grave_id": deceased.grave_id,
            "grave_number": deceased.grave.grave_number,
        }
        for deceased in deceased_list
    ]


@router.get("/{deceased_id}", response_model=DeceasedResponse)
def get_deceased_route(
    deceased_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deceased = get_deceased(db, deceased_id)
    if not deceased:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deceased not found")
    return {
        "id": deceased.id,
        "first_name": deceased.first_name,
        "last_name": deceased.last_name,
        "birth_date": deceased.birth_date,
        "death_date": deceased.death_date,
        "grave_id": deceased.grave_id,
        "grave_number": deceased.grave.grave_number,
    }


@router.put("/{deceased_id}", response_model=DeceasedResponse)
def update_deceased_route(
    deceased_id: int,
    deceased_data: UpdateDeceased,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deceased = get_deceased(db, deceased_id)
    if not deceased:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deceased not found")
    try:
        deceased = update_deceased(db, deceased, deceased_data)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc))
    return {
        "id": deceased.id,
        "first_name": deceased.first_name,
        "last_name": deceased.last_name,
        "birth_date": deceased.birth_date,
        "death_date": deceased.death_date,
        "grave_id": deceased.grave_id,
        "grave_number": deceased.grave.grave_number,
    }


@router.delete("/{deceased_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_deceased_route(
    deceased_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    deceased = get_deceased(db, deceased_id)
    if not deceased:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Deceased not found")
    delete_deceased(db, deceased)
    return None
