from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from connetion import Student, Subject

# creating engine
engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/demo', echo= False)

# creating session
Session = sessionmaker(bind=engine)
session = Session()

# creating student object(instance of the student class)
# student1 = Student(name='vijay', age=28, grade='cs')
#
# student2 = Student(name='Raj', age=23, grade='ec')
# student3 = Student(name='Shivam', age=27, grade='it')

subject1= Subject(name='DSA')
subject2=Subject(name='ADA')

# adding the data(instance) to the session we have created
#session.add(student1)  # for adding a single record

session.add_all([subject2, subject1])  # for adding multiple values

# commit the changes
session.commit()
