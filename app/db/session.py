from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,          # number of connections
    max_overflow=20,       # extra connections
    pool_timeout=30,       # wait time
    pool_pre_ping=True     # check connections
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)