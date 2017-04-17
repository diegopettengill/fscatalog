from sqlalchemy import Column, Integer, String, ForeignKey, Text, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

get_current_time = func.now()

"""User model"""


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    email = Column(String(120), unique=True)
    name = Column(String(120), nullable=True)
    avatar = Column(String(200), nullable=True)
    telephone = Column(String(30), nullable=True)
    created_at = Column(DateTime, default=get_current_time)
    updated_at = Column(DateTime, default=get_current_time,
                        onupdate=get_current_time)


"""Category model"""


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)


"""Product model"""


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    title = Column(String(50), unique=True, nullable=False)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship(User)
    picture = Column(String(250))
    price = Column(Integer)
    created_at = Column(DateTime, default=get_current_time)
    updated_at = Column(DateTime, default=get_current_time,
                        onupdate=get_current_time)
