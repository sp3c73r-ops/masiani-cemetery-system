from datetime import datetime
from sqlalchemy import Boolean, Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Grave(Base):
    __tablename__ = "graves"

    id = Column(Integer, primary_key=True, index=True)
    grave_number = Column(String, unique=True, index=True, nullable=False)
    latitude = Column(String, nullable=False)
    longitude = Column(String, nullable=False)
    status = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    photos = relationship("Photo", back_populates="grave", cascade="all, delete-orphan")
    deceased = relationship("Deceased", back_populates="grave", cascade="all, delete-orphan")


class Deceased(Base):
    __tablename__ = "deceased"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    birth_date = Column(Date, nullable=True)
    death_date = Column(Date, nullable=True)
    grave_id = Column(Integer, ForeignKey("graves.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    grave = relationship("Grave", back_populates="deceased")


class Photo(Base):
    __tablename__ = "photos"

    id = Column(Integer, primary_key=True, index=True)

    file_name = Column(String, nullable=False)
    file_path = Column(String, nullable=False)

    grave_id = Column(Integer, ForeignKey("graves.id"), nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    grave = relationship("Grave", back_populates="photos")
