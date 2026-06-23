import os
import uuid

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile, status
from sqlalchemy.orm import Session

from app.models.models import User
from app.routes.auth import get_current_user, get_db
from app.schemas.photo import PhotoResponse
from app.services.photo_service import (
    create_photo,
    delete_photo,
    get_grave,
    get_photo,
    get_photos_by_grave,
)

router = APIRouter(prefix="/photos", tags=["photos"])
UPLOAD_DIR = "uploads/graves"
ALLOWED_EXTENSIONS = {"jpg", "jpeg", "png"}


def ensure_upload_dir() -> None:
    os.makedirs(UPLOAD_DIR, exist_ok=True)


def validate_file_extension(filename: str) -> str:
    if "." not in filename:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="File must have an extension.",
        )
    extension = filename.rsplit(".", 1)[-1].lower()
    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid file type. Only jpg, jpeg and png are allowed.",
        )
    return extension


@router.post("/upload/{grave_id}", response_model=PhotoResponse)
async def upload_photo(
    grave_id: int,
    file: UploadFile = File(...),
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    grave = get_grave(db, grave_id)
    if not grave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grave not found")

    extension = validate_file_extension(file.filename)
    ensure_upload_dir()

    unique_filename = f"{uuid.uuid4()}.{extension}"
    file_path = os.path.join(UPLOAD_DIR, unique_filename)

    content = await file.read()
    with open(file_path, "wb") as out_file:
        out_file.write(content)

    photo = create_photo(db, grave_id, unique_filename, file_path)
    return photo


@router.get("/grave/{grave_id}", response_model=list[PhotoResponse])
def list_photos_by_grave(
    grave_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    grave = get_grave(db, grave_id)
    if not grave:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Grave not found")
    return get_photos_by_grave(db, grave_id)


@router.delete("/{photo_id}", status_code=status.HTTP_204_NO_CONTENT)
def remove_photo(
    photo_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    photo = get_photo(db, photo_id)
    if not photo:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Photo not found")

    if os.path.exists(photo.file_path):
        os.remove(photo.file_path)

    delete_photo(db, photo)
    return None
