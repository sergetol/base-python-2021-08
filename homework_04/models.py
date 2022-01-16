"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""

import os
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, as_declarative, declared_attr, relationship
from sqlalchemy import Column, Integer, DateTime, func, String, ForeignKey, Text
from datetime import datetime


PG_CONN_URI = (
    os.environ.get("SQLALCHEMY_PG_CONN_URI")
    or "postgresql+asyncpg://postgres:password@localhost/postgres"
)

engine = create_async_engine(PG_CONN_URI, echo=True)
Session = sessionmaker(engine, class_=AsyncSession)


@as_declarative()
class Base:
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


class User(Base):
    name = Column(String(128), nullable=False)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String(128), nullable=False, unique=True)
    phone = Column(String(32))
    website = Column(String(128))

    posts = relationship("Post", order_by="Post.id", back_populates="user")


class Post(Base):
    user_id = Column(
        Integer,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
    )
    title = Column(String(256), nullable=False)
    body = Column(Text, nullable=False)

    user = relationship("User", back_populates="posts")
