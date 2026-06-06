from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base, sessionmaker

from src.config import DATABASE_URL

Base = declarative_base()

engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
