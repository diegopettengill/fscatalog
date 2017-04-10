from sqlalchemy import Column, Integer, String

from database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), nullable=False)
    password = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    profile_picture = Column(String(150), nullable=False)
