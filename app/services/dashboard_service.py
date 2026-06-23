from sqlalchemy.orm import Session

from app.models.models import Deceased, Grave, Photo


def get_dashboard_stats(db: Session) -> dict:
    total_graves = db.query(Grave).count()
    identified_graves = db.query(Grave).filter(Grave.status == "identifiee").count()
    supposed_graves = db.query(Grave).filter(Grave.status == "supposee").count()
    total_deceased = db.query(Deceased).count()
    total_photos = db.query(Photo).count()

    return {
        "total_graves": total_graves,
        "identified_graves": identified_graves,
        "supposed_graves": supposed_graves,
        "total_deceased": total_deceased,
        "total_photos": total_photos,
    }
