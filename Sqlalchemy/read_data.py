from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connetion import Student

# creating engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/demo', echo= False)

# creating session
Session = sessionmaker(bind=engine)
session = Session()

# get all the data
# students = session.query(Student)
#
# for student in students:
#     print(student.name, student.id, student.age, student.grade)

# get data in order
# students = session.query(Student).order_by(Student.name)
#
# for student in students:
#     print(student.name, student.id, student.age, student.grade)

# Get data by Filtering

# student = session.query(Student).filter(Student.name =='vijay').first()
#students = session.query(Student).filter(or_(Student.name =='vijay', Student.name =='Shivam'))

# for student in students:
#     print(student.name, student.id, student.age, student.grade)

# for getting  count
students = session.query(Student).count()
print(students)



