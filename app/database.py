import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

load_dotenv()


class Base(DeclarativeBase):
    """Base class all ORM models inherit from."""


def _build_engine():
    """Create a SQLAlchemy engine.

    - Local dev: set DATABASE_URL (e.g. postgresql+pg8000://user:pass@localhost:5432/sisen)
    - Cloud Run: set INSTANCE_CONNECTION_NAME + DB_USER/DB_PASS/DB_NAME; connects via Unix socket
    """
    db_url = os.environ.get("DATABASE_URL")
    if db_url:
        return create_engine(db_url, future=True)

    instance = os.environ["INSTANCE_CONNECTION_NAME"]
    user = os.environ["DB_USER"]
    password = os.environ["DB_PASS"]
    db_name = os.environ["DB_NAME"]

    return create_engine(
        f"postgresql+pg8000://{user}:{password}@/{db_name}",
        connect_args={"unix_sock": f"/cloudsql/{instance}/.s.PGSQL.5432"},
        future=True,
    )


engine = _build_engine()
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)


def get_db():
    """FastAPI dependency: yields a DB session and closes it after the request."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
