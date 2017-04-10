from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from models import User


class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    description = Column(String(20), nullable=False)
    price = Column(Float, nullable=False, precision=2)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

