from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine('sqlite:///alchemy_database.db')
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String(8))

class JobPost(Base):
    __tablename__ ='job posts'

    id = Column(Integer, primary_key=True)
    role_name = Column(String(100))
    location = Column(String(50))
    description = Column(String(255))
    level = Column(String(50))
    saralry = Column(Integer,default=10000)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# user_nmae = input('Enter username: ')
# user_email = input('Enter your email: ')
# user_password = input('Enter your Password: ')

# new_user = User(username=user_nmae, email=user_email, password=user_password)
# session.add(new_user)
# session.commit()

print("\nDetails of Job Postings\n")

job_role =  input("Enter Job Postings role: ")
job_location = input("Enter the location: ")
job_description = input("Enter the job description: ")
job_level = input("Enter the level ? fresher or experience,and how many years: ")
job_salary = input("Enter the salary for this job: ")

new_jobpost = JobPost(role_name=job_role,location=job_location,
    description=job_description,level=job_level, saralry=job_salary)
session.add(new_jobpost)
session.commit()

session.close()