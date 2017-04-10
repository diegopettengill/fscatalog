from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker, scoped_session
from sqlalchemy import create_engine

engine = create_engine('sqlite:///catalog.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    from models import User
    Base.metadata.create_all(bind=engine)

# class MenuItem(Base):
#     __tablename__ = 'menu_item'
#
#     name = Column(String(80), nullable=False)
#     id = Column(Integer, primary_key=True)
#     description = Column(String(250))
#     price = Column(String(8))
#     course = Column(String(250))
#     restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
#     restaurant = relationship(Restaurant)
#
#     @property
#     def serialize(self):
#         return {
#             'id': self.id,
#             'name': self.name,
#             'description': self.description,
#             'price': self.price,
#             'course': self.course
#         }
