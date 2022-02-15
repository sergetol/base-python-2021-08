import os

SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    "postgresql+psycopg2://postgres:password@localhost:5432/postgres",
)

SECRET_KEY = os.getenv(
    "SECRET_KEY",
    "defaultSecretKey",
)


class Config:
    ENV = "production"
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI
    SECRET_KEY = SECRET_KEY


class ProdConfig(Config):
    pass


class DevConfig(Config):
    ENV = "development"
    DEBUG = True


class TestConfig(Config):
    ENV = "development"
    DEBUG = True
    TESTING = True
