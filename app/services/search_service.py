from typing import List

from sqlalchemy.orm import Session

from app.models.models import Deceased


def search_deceased(db: Session, query: str) -> List[Deceased]:
    if not query or not query.strip():
        return []

    search_term = f"%{query.lower()}%"
    return (
        db.query(Deceased)
        .filter(
            (Deceased.first_name.ilike(search_term)) | (Deceased.last_name.ilike(search_term))
        )
        .all()
    )
