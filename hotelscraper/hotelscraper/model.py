from sqlalchemy import create_engine, Column, Integer, String, Float, Text, ARRAY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Hotel(Base):
    __tablename__ = 'hotels'

    id = Column(Integer, primary_key=True)
    propertyTitle = Column(String, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    location = Column(Text)
    rating = Column(Float)
    price = Column(Float)
    roomType = Column(String)
    images = Column(ARRAY(Text))

# Set up the database engine and session
def db_connect():
    return create_engine('postgresql://postgres:admin@localhost/hotel')

def create_table(engine):
    Base.metadata.create_all(engine)
