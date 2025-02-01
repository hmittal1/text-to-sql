import sqlite3

#connect to sql lite database
connection = sqlite3.connect("student.db")

#create a cursor object to insert record or create table
cursor = connection.cursor()

#create table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), SECTION VARCHAR(25));
"""
cursor.execute(table_info)

#insert records
cursor.execute("""Insert into STUDENT values('Ram', 'Data science', 'A') """)
cursor.execute("""Insert into STUDENT values('Mohan', 'Data science', 'B') """)
cursor.execute("""Insert into STUDENT values('Sita', 'Data science', 'A') """)
cursor.execute("""Insert into STUDENT values('Sham', 'DevOps', 'A') """)
cursor.execute("""Insert into STUDENT values('Sohan', 'DevOps', 'A') """)

#display records
data = cursor.execute("""Select * from STUDENT """)
for row in data:
    print(row)

#commit and close the connection.
connection.commit()
connection.close()