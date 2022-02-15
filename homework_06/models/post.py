from sqlalchemy.orm import declared_attr
from sqlalchemy import Column, Integer, DateTime, func, String, Text
from datetime import datetime

from .database import db


class Post(db.Model):
    @declared_attr
    def __tablename__(cls):
        return f"{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )
    updated_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
        onupdate=datetime.utcnow,
    )
    title = Column(String(256), nullable=False)
    body = Column(Text, nullable=False)
