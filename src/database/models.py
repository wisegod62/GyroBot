from sqlalchemy import Column, Integer, String
from src.database.database import Base


class Profile(Base):
    __tablename__ = "profiles"

    user_id = Column(Integer, primary_key=True)

    pronouns = Column(String, default="Not Set")

    gender = Column(String, default="Not Set")

    sexuality = Column(String, default="Not Set")

    bio = Column(String, default="Not Set")

    interests = Column(String, default="Not Set")

    flag = Column(String, default="Not Set")

    card_color = Column(Integer, default=0x5865F2)
