from typing import List

from sqlalchemy.orm import Session

from app.models.models import Grave


def get_all_graves(db: Session) -> List[Grave]:
    return db.query(Grave).all()
