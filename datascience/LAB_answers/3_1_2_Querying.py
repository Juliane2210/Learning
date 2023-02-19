#Querying in databases with python

import ibm_db
import pandas
import ibm_db_dbi


#TASK 1:(install ibm_db)
#Latest version: pip install ibm-db==3.1.1
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql



#TASK 2:(database credentials)
#Replace the placeholder values with your actual Db2 hostname, username, and password:
dsn_hostname = "ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
dsn_uid = "vjm09314"        # e.g. "abc12345"
dsn_pwd = "Ok9eVz8jSEnSViqR"      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "31321"                # e.g. "32733"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"  # i.e. "SSL"



#TASK 3:(Create database connection)
#DO NOT MODIFY THIS CELL. Just RUN it with Shift + Enter
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )   



#TASK 4: (Create a table in the database)
#Lets first drop the table INSTRUCTOR in case it exists from a previous attempt
dropQuery = "drop table INSTRUCTOR"

#Now execute the drop statement
dropStmt = ibm_db.exec_immediate(conn, dropQuery)
#We get an error because the INSTRUCTOR table does not exist in the table (hasn't been created previously)


createQuery = "create table INSTRUCTOR(ID INTEGER PRIMARY KEY NOT NULL, FNAME VARCHAR(20), LNAME VARCHAR(20), CITY VARCHAR(20), CCODE CHAR(2))"

createStmt = ibm_db.exec_immediate(conn,createQuery)

#TASK 5:(Insert data into the table)
#In this step we will insert some rows of data into the table.
#The INSTRUCTOR table we created in the previous step contains 3 rows of data.
#We start by inserting the first row:

#Construct the query - replace ... with the insert statement
insertQuery = "Insert into instructor values(1, 'Rav', 'Ahuja', 'TORONTO', 'CA');"

#execute the insert statement
insertStmt = ibm_db.exec_immediate(conn, insertQuery)

#Now use a single query to insert the remaining two rows of data.
insertQuery2 = "insert into INSTRUCTOR values (2, 'Raul', 'Chong', 'Markham', 'CA'), (3, 'Hima', 'Vasudevan', 'Chicago', 'US')"

insertStmt2 = ibm_db.exec_immediate(conn, insertQuery2)


#TASK 6: (Query data in the table)
#In this step we will retrieve data we inserted into the INSTRUCTOR table.

#Construct the query that retrieves all rows from the INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#Execute the statement
selectStmt = ibm_db.exec_immediate(conn, selectQuery)

#Fetch the Dictionary (for the first row only) - replace ... with your code
ibm_db.fetch_both(selectStmt)

#Fetch the rest of the rows and print the ID and FNAME for those rows
while ibm_db.fetch_row(selectStmt) != False:
   print (" ID:",  ibm_db.result(selectStmt, 0), " FNAME:",  ibm_db.result(selectStmt, "FNAME"))


#Bonus: now write and execute an update statement that changes the Rav's CITY to MOOSETOWN

updateQuery="update INSTRUCTOR set CITY='MOOSETOWN' where FNAME='Rav'"
updateStmt= ibm_db.exec_immediate(conn, updateQuery)

#TASK 7:(Retrieve data into Pandas)
#In this step we will retrieve the contents of the INSTRUCTOR table into a Pandas dataframe.

#connection for pandas
pconn = ibm_db_dbi.Connection(conn)

#query statement to retrieve all rows in INSTRUCTOR table
selectQuery = "select * from INSTRUCTOR"

#retrieve the query results into a pandas dataframe
pdf = pandas.read_sql(selectQuery, pconn)

#print just the LNAME for first row in the pandas data frame
print(pdf.LNAME[0])

#print the entire data frame
print(pdf)


#Once the data is in a Pandas dataframe, you can do the typical pandas operations on it.
#For example, you can use the shape method to see how many rows and columns are in the dataframe.
print(pdf.shape)

#TASK 8: (Close the Connection)
#We free all resources by closing the connection.
#  Remember that it is always important to close connections so that we can avoid unused connections taking up resources.

ibm_db.close(conn)




