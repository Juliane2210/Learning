#CREATING AND ACCESS SQLITE DATABASE USING PYTHON:
#SQLite is a software library that implements a self-contained, serverless, zero-configuration,
#transactional SQL database engine.
#SQLite is the most widely deployed SQL database engine in the world.



#TASK 1: (Create database using SQLite)
#Install & load sqlite3
#!pip install sqlite3  ##Uncomment the code to install sqlite3
#no need to install sqlite3...it is already installed
import sqlite3

# Connecting to sqlite
# connection object
conn = sqlite3.connect('INSTRUCTOR.db')

#Cursor class is an instance using which you can invoke methods that execute SQLite statements,
#fetch data from the result sets of the queries.
#You can create Cursor object using the cursor() method of the Connection object/class.

# cursor object
cursor_obj = conn.cursor()

#TASK 2:(Create a table in the database)
#In this step we will create a table in the database with given details.

#Before creating a table, let's first see if the table already exists or not.
#To drop the table from a database use DROP query.
#A cursor is an object which helps to execute the query and fetch the records from the database.


# Drop the table if already exists.
cursor_obj.execute("DROP TABLE IF EXISTS INSTRUCTOR")#<sqlite3.Cursor at 0x7f94603c41f0>

# Creating table
table = """ create table IF NOT EXISTS INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2));"""
 
cursor_obj.execute(table)
 
print("Table is Ready")

#TASK 3:(Insert data into the table) 
#In this step we will insert some rows of data into the table.

#The INSTRUCTOR table we created previously has 3 rows...
cursor_obj.execute('''insert into INSTRUCTOR values (1, 'Rav', 'Ahuja', 'TORONTO', 'CA')''')
 #We get <sqlite3.Cursor at 0x7f94603c41f0> which means mySql database has sqlite3.Cursor
 #object at 0x7f94603c41f0 as output in table.

 #Now we insert the last 2 rows:
cursor_obj.execute('''insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')''')


#TASK 4: (Query data in the table)
#In this step we will retrieve data we inserted into the INSTRUCTOR table.


#fetching all the rows:
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)

print("All the data")
output_all = cursor_obj.fetchall()
for row_all in output_all:
  print(row_all)




#Fetching the first 2 rows:
## Fetch few rows from the table
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
# If you want to fetch few rows from the table we use fetchmany(numberofrows) and mention the number how many rows you want to fetch
output_many = cursor_obj.fetchmany(2) 
for row_many in output_many:
  print(row_many)




# Fetch only FNAME from the table
statement = '''SELECT FNAME FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output_column = cursor_obj.fetchall()
for fetch in output_column:
  print(fetch)

#Now write and execute an update statement that changes the Rav's CITY to MOOSETOWN:

query_update='''update INSTRUCTOR set CITY='MOOSETOWN' where FNAME="Rav"'''
cursor_obj.execute(query_update) 

#now we verify:
statement = '''SELECT * FROM INSTRUCTOR'''
cursor_obj.execute(statement)
  
print("All the data")
output1 = cursor_obj.fetchmany(2)
for row in output1:
  print(row)

#TASK 5: (Retrieve data into Pandas)  
#In this step we will retrieve the contents of the INSTRUCTOR table into a Pandas dataframe

import pandas as pd
#retrieve the query results into a pandas dataframe
df = pd.read_sql_query("select * from instructor;", conn)

#print the dataframe
print(df)

#print just the LNAME for first row in the pandas data frame
print(df.LNAME[0])

#Once the data is in a Pandas dataframe, you can do the typical pandas operations on it.
#For example you can use the shape method to see how many rows and columns are in the dataframe
print(df.shape)#(3,5) -> 3 rows, 5 columns


#TASK 6: (Close the Connection)
# Close the connection
conn.close()



