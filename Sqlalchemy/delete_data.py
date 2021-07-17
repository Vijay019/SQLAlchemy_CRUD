from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connetion import Student

# creating engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/demo', echo= False)

# creating session
Session = sessionmaker(bind=engine)
session = Session()

# delete data
student = session.query(Student).filter(Student.name =='Shivam').first()
session.delete(student)
session.commit()