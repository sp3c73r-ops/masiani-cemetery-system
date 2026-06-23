from fastapi import FastAPI

from app.database.database import Base, SessionLocal, engine
from app.routes.auth import router as auth_router
from app.routes.deceased import router as deceased_router
from app.routes.graves import router as graves_router
from app.services.auth_service import create_admin_user
import app.models.models  # noqa: F401

app = FastAPI()
app.include_router(auth_router)
app.include_router(graves_router)
app.include_router(deceased_router)


@app.on_event("startup")
def on_startup():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        create_admin_user(db)
    finally:
        db.close()


@app.get("/")
def read_root():
    return {"message": "Masiani Cemetery API"}
