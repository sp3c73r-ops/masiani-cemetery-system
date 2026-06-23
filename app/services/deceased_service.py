from typing import Optional

from sqlalchemy.orm import Session

from app.models.models import Deceased, Grave
from app.schemas.deceased import CreateDeceased, UpdateDeceased


def get_grave(db: Session, grave_id: int) -> Optional[Grave]:
    return db.query(Grave).filter(Grave.id == grave_id).first()


def get_deceased(db: Session, deceased_id: int) -> Optional[Deceased]:
    return db.query(Deceased).filter(Deceased.id == deceased_id).first()


def get_deceased_list(db: Session) -> list[Deceased]:
    return db.query(Deceased).all()


def create_deceased(db: Session, deceased_data: CreateDeceased) -> Deceased:
    grave = get_grave(db, deceased_data.grave_id)
    if not grave:
        raise ValueError("Grave not found")

    deceased = Deceased(
        first_name=deceased_data.first_name,
        last_name=deceased_data.last_name,
        birth_date=deceased_data.birth_date,
        death_date=deceased_data.death_date,
        grave_id=deceased_data.grave_id,
    )
    db.add(deceased)
    db.commit()
    db.refresh(deceased)
    return deceased


def update_deceased(db: Session, deceased: Deceased, deceased_data: UpdateDeceased) -> Deceased:
    if deceased_data.grave_id is not None:
        grave = get_grave(db, deceased_data.grave_id)
        if not grave:
            raise ValueError("Grave not found")
        deceased.grave_id = deceased_data.grave_id
    if deceased_data.first_name is not None:
        deceased.first_name = deceased_data.first_name
    if deceased_data.last_name is not None:
        deceased.last_name = deceased_data.last_name
    if deceased_data.birth_date is not None:
        deceased.birth_date = deceased_data.birth_date
    if deceased_data.death_date is not None:
        deceased.death_date = deceased_data.death_date
    db.commit()
    db.refresh(deceased)
    return deceased


def delete_deceased(db: Session, deceased: Deceased) -> None:
    db.delete(deceased)
    db.commit()
