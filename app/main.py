from fastapi import FastAPI

from app.database.database import Base, SessionLocal, engine
from app.routes.auth import router as auth_router
from app.routes.deceased import router as deceased_router
from app.routes.graves import router as graves_router
from app.routes.photos import router as photos_router
from app.routes.search import router as search_router
from app.routes.map import router as map_router
from app.routes.navigation import router as navigation_router
from app.routes.dashboard import router as dashboard_router
from app.services.auth_service import create_admin_user
import app.models.models  # noqa: F401

app = FastAPI()

app.include_router(auth_router)
app.include_router(graves_router)
app.include_router(deceased_router)
app.include_router(photos_router)
app.include_router(search_router)
app.include_router(navigation_router)
app.include_router(dashboard_router)
app.include_router(map_router)

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
