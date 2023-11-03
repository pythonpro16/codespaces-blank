import sqlite3

db_connection = sqlite3.connect('my_database.db')
cursor = db_connection.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS mytable (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)""")
# cursor.execute("INSERT INTO mytable (name,age) VALUES (?, ?)", ("Jobi", 21))
# cursor.execute("INSERT INTO mytable (name, age) VALUES (?, ?)", ("Bob", 30))

db_connection.commit()

# query data from the database

cursor.execute("SELECT * FROM mytable")

datas = cursor.fetchall()

for data in datas:
    print(data)

cursor.execute( """ 
    DELETE FROM mytable
    WHERE id NOT IN (
        SELECT MIN(id) FROM mytable GROUP BY name,age
    )
""")
db_connection.commit()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS job_postings(
        id INTEGER PRIMARY KEY,
        role TEXT,
        salary INTEGER,
        location TEXT
    )
""")

cursor.execute("""INSERT INTO job_postings(role, salary, location) VALUES
    ('python developer',  15000, 'Nagercoil'),
    ('python programmar',  35000, 'kanniyakumar'),
    ('Data Scientist',  25000, 'Trivandrum')
        """)


db_connection.commit()

cursor.execute("""
    DELETE FROM job_postings
    WHERE id NOT IN(
        SELECT min(id) FROM job_postings GROUP BY role, salary, location
    )
""")

db_connection.commit()

cursor.execute("SELECT * FROM job_postings")
datas = cursor.fetchall()
for data in datas:
    print(data)

# DELETING USER SELECTED ID

delete_id = int(input("Enter the id number which you want to deleted"))

cursor.execute(f"DELETE FROM job_postings WHERE id = {delete_id}")
db_connection.commit()

cursor.execute("SELECT * FROM job_postings")
datas = cursor.fetchall()
for data in datas:
    print(data)


# Updated the ID number is ascending order

cursor.execute('''
    UPDATE job_postings
    SET id = (SELECT COUNT(*) FROM job_postings t2 WHERE t2.id <= job_postings.id) 
''')
db_connection.commit()

cursor.execute("SELECT * FROM job_postings")
datas = cursor.fetchall()
for data in datas:
    print(data)

cursor.execute("DROP TABLE IF EXISTS mytable;")
db_connection.commit()


db_connection.close()

