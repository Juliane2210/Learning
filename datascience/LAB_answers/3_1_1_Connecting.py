


#IMPORT THE 'ibm_db' PYTHON LIBRARY:
#The 'ibm_db' API provides a variety of useful Python functions for accessing and manipulating
#data in an IBM data server database. (such as)
#-fcts for connecting to a database
#-preparing and issuing SQL statements
#-fetching rows from result sets
#-calling stored procedures
#-committing and rolling back transactions
#-handling errors
#-retrieving metadata





#Connecting to a database instance

#latest version: pip install ibm-db==3.1.1
#!pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
#!pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
#!pip install ipython-sql


import ibm_db

#IDENTIFY THE DATABASE CONNECTION CREDENTIALS:

#Replace the placeholder values with your actual Db2 hostname, username, and password:
dsn_hostname = "ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud"
dsn_uid = "vjm09314"        # e.g. "abc12345"
dsn_pwd = "Ok9eVz8jSEnSViqR"      # e.g. "7dBZ3wWt9XN6$o0J"
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "BLUDB"            # e.g. "BLUDB"
dsn_port = "31321"                # e.g. "32733"
dsn_protocol = "TCPIP"            # i.e. "TCPIP"
dsn_security = "SSL"  # i.e. "SSL"



#CREATE THE DB2 DATABASE CONNECTION:
#Ibm_db API uses the IBM Data Server Driver for ODBC and CLI APIs to connect to IBM DB2 and Informix.
#Let's build the dsn connection string using the credentials entered above:


dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd, dsn_security)

print(dsn)


#now we establish the connection to the database:
try:
    conn = ibm_db.connect(dsn, "", "")
    print ("Connected to database: ", dsn_database, "as user: ", dsn_uid, "on host: ", dsn_hostname)

except:
    print ("Unable to connect: ", ibm_db.conn_errormsg() )


#Retrieve Metadata for the Database Server
server = ibm_db.server_info(conn)

print ("DBMS_NAME: ", server.DBMS_NAME)
print ("DBMS_VER:  ", server.DBMS_VER)
print ("DB_NAME:   ", server.DB_NAME)

#Retrieve Metadata for the Database Client / Driver
client = ibm_db.client_info(conn)

print ("DRIVER_NAME:          ", client.DRIVER_NAME) 
print ("DRIVER_VER:           ", client.DRIVER_VER)
print ("DATA_SOURCE_NAME:     ", client.DATA_SOURCE_NAME)
print ("DRIVER_ODBC_VER:      ", client.DRIVER_ODBC_VER)
print ("ODBC_VER:             ", client.ODBC_VER)
print ("ODBC_SQL_CONFORMANCE: ", client.ODBC_SQL_CONFORMANCE)
print ("APPL_CODEPAGE:        ", client.APPL_CODEPAGE)
print ("CONN_CODEPAGE:        ", client.CONN_CODEPAGE)

#CLOSE THE CONNECTION
#We free all resources by closing the connection.
#It is important to close connections so that we can avoid unused connections taking up resources.

print(ibm_db.close(conn)) #True












