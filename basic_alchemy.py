from sqlalchemy import create_engine, Column, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import select

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
    salary = Column(Integer,default=10000)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# user_nmae = input('Enter username: ')
# user_email = input('Enter your email: ')
# user_password = input('Enter your Password: ')

# new_user = User(username=user_nmae, email=user_email, password=user_password)
# session.add(new_user)
# session.commit()

# print("\nDetails of Job Postings\n")

# job_role =  input("Enter Job Postings role: ")
# job_location = input("Enter the location: ")
# job_description = input("Enter the job description: ")
# job_level = input("Enter the level ? fresher or experience,and how many years: ")
# job_salary = input("Enter the salary for this job: ")

# new_jobpost = JobPost(role_name=job_role,location=job_location,
#     description=job_description,level=job_level, salary=job_salary)
# session.add(new_jobpost)
# session.commit()
from sqlalchemy import column

# role_name = column(JobPost.role_name)
# salary = column(JobPost.salary)
# columns = [JobPost.role_name, JobPost.salary]

# query = select([role_name, salary])

results = session.query(JobPost).all()


for result in results:
    # role, salary = result
    # print(f"Role: {role}, salary:{salary}")
    print(result.id, result.role_name, result.location, result.salary)

new_result = session.query(JobPost.id, JobPost.role_name, JobPost.salary).all()

for result in new_result:
    print(result)
session.close()


for n in range(1000):
    print("hello")