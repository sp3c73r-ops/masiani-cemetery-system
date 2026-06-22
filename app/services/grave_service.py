from typing import Optional

from sqlalchemy.orm import Session

from app.models.models import Grave
from app.schemas.grave import CreateGrave, UpdateGrave


def create_grave(db: Session, grave_data: CreateGrave) -> Grave:
    grave = Grave(
        grave_number=grave_data.grave_number,
        latitude=grave_data.latitude,
        longitude=grave_data.longitude,
        status=grave_data.status,
    )
    db.add(grave)
    db.commit()
    db.refresh(grave)
    return grave


def get_grave(db: Session, grave_id: int) -> Optional[Grave]:
    return db.query(Grave).filter(Grave.id == grave_id).first()


def get_graves(db: Session) -> list[Grave]:
    return db.query(Grave).all()


def update_grave(db: Session, grave: Grave, grave_data: UpdateGrave) -> Grave:
    if grave_data.grave_number is not None:
        grave.grave_number = grave_data.grave_number
    if grave_data.latitude is not None:
        grave.latitude = grave_data.latitude
    if grave_data.longitude is not None:
        grave.longitude = grave_data.longitude
    if grave_data.status is not None:
        grave.status = grave_data.status
    db.commit()
    db.refresh(grave)
    return grave


def delete_grave(db: Session, grave: Grave) -> None:
    db.delete(grave)
    db.commit()
