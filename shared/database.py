from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from shared.settings import settings


SQLALCHEMY_DATABASE_URL = str(settings.SQLALCHEMY_DATABASE_URI)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
