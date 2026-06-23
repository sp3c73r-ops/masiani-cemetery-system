from typing import List, Optional

from sqlalchemy.orm import Session

from app.models.models import Grave, Photo


def get_grave(db: Session, grave_id: int) -> Optional[Grave]:
    return db.query(Grave).filter(Grave.id == grave_id).first()


def create_photo(db: Session, grave_id: int, file_name: str, file_path: str) -> Photo:
    grave = get_grave(db, grave_id)
    if not grave:
        raise ValueError("Grave not found")

    photo = Photo(
        grave_id=grave_id,
        file_name=file_name,
        file_path=file_path,
    )
    db.add(photo)
    db.commit()
    db.refresh(photo)
    return photo


def get_photos_by_grave(db: Session, grave_id: int) -> List[Photo]:
    return db.query(Photo).filter(Photo.grave_id == grave_id).all()


def get_photo(db: Session, photo_id: int) -> Optional[Photo]:
    return db.query(Photo).filter(Photo.id == photo_id).first()


def delete_photo(db: Session, photo: Photo) -> None:
    db.delete(photo)
    db.commit()
