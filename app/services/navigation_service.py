from typing import Optional

from sqlalchemy.orm import Session

from app.models.models import Deceased


def get_deceased_with_grave(db: Session, deceased_id: int) -> Optional[Deceased]:
    return db.query(Deceased).filter(Deceased.id == deceased_id).first()


def build_navigation_url(latitude: str, longitude: str) -> str:
    return f"https://www.google.com/maps?q={latitude},{longitude}"
