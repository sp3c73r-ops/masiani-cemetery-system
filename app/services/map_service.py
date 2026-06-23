from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.models import Deceased, Grave


def get_all_graves(db: Session) -> List[Grave]:
    return db.query(Grave).all()


def get_deceased_location(db: Session, deceased_id: int) -> Optional[Deceased]:
    return db.query(Deceased).filter(Deceased.id == deceased_id).first()
