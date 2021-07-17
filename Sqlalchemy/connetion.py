from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import psycopg2

# creating engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/demo', echo= False)
# [DB_TYPE]+[DB_CONNECTOR]://[USERNAME]:[PASSWORD]@[HOST]:[PORT]/[DB_NAME]

# creating session
Session = sessionmaker(bind=engine)
session = Session()

# creating Base class
Base = declarative_base()

# creating a class which represents student table in the databse
class Student(Base):

    __tablename__ = 'student'          # mandatory field

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))


class Subject(Base):

    __tablename__ = 'subject'          # mandatory field

    id = Column(Integer, primary_key=True)
    name = Column(String(50))


# below line is for creating table to selected database
Base.metadata.create_all(engine)



