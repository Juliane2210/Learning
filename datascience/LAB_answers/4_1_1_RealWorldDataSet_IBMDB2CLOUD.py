#WORKING WITH A REAL WORLD DATA-SET USING SQL AND PYTHON:

#-> Chicago Public Schools-Progress Report Cards(2011-2012)
#First we store the dataset into a table using IBM Watson Studio.

#CONNECT TO THE DATABASE:
# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql

%load_ext sql
%sql ibm_db_sa://vjm09314:Ok9eVz8jSEnSViqR@ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:31321/BLUDB?security=SSL


#QUERY THE DATABASE SYSTEM CATALOG TO RETRIEVE TABLE METADATA:
#We verify that the table creation was successful by retrieving the list of all tables
#in our schema and checking wether the SCHOOLS table was created.

# type in your query to retrieve list of all tables in the database for your db2 schema (username)
%sql select TABSCHEMA, TABNAME, CREATE_TIME from SYSCAT.TABLES where TABSCHEMA='vjm09314'

#QUERY THE DATABASE SYSTEM CATALOG TO RETRIEVE COLUMN METADATA:
#The SCHOOLS table contains a large number of columns. How many columns des this table have?

%sql SELECT COUNT(*) FROM SYSCAT.COLUMNS WHERE TABNAME= 'SCHOOLS'
#should get 78

#Now we retrieve the list of columns in SCHOOLS table and their column type (datatype) and length.
%sql select COLNAME, TYPENAME, LENGTH from SYSCAT.COLUMNS where TABNAME = 'SCHOOLS'

#QUESTIONS:
#1. Is the column name for the 'SCHOOL ID' attribute in upper or mixed case? mixed
#2. What is the name of 'Community Area Name' column in our table? Does it have spaces? no spaces but underscore between words
#3. Are there any columns in whose names the spaces and parenthesis have been replaced by the underscore character?yes: 'name_of_school'

#PROBLEMS:
#1. How many Elementary Schools are in the dataset?
%sql select count(*) from SCHOOLS where 'Elementary'='ES'or 'Middle'='ES' or 'High School'='ES'
#Should get 462 ^that doesn't give the correct answer


#2.What is the highest Safety Score?
%sql select MAX(Safety_Score) as MAX_SAFETY_SCORE from SCHOOLS
#should get 99


#3.Which schools have the highest Safety Score?
%sql select Name_of_School, Safety_Score from SCHOOLS where Safety_Score = 99
#Better alternative:('\' to start a new line of statement)
%sql select Name_of_School, Safety_Score from SCHOOLS where \
Safety_Score = (select MAX(Safety_Score) from SCHOOLS)


#4.What are the top 10 schools with the highest "Average Student Attendance"?
%sql select Name_of_School, Average_Student_Attendance from SCHOOLS\
order by Average_Student_Attendance desc nulls last limit 10

#5. Retrieve the list of 5 Schools with the lowest Average Student Attendance sorted in ascending order based on attendance.
%sql select Name_of_School, Average_Student_Attendance\
from SCHOOLS\
order by Average_Student_Attendance\
fetch first 5 rows only 

#6. Now remove the '%' sign from the above result.
%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') \
     from SCHOOLS \
     order by Average_Student_Attendance \
     fetch first 5 rows only


#7. Which Schools have Average Student Attendance lower than 70%?
%sql SELECT Name_of_School, Average_Student_Attendance  \
     from SCHOOLS \
     where DECIMAL ( REPLACE(Average_Student_Attendance, '%', '') ) < 70 \
     order by Average_Student_Attendance

#The default dor DECIMAL() is 0 ...so no decimals


#8. Get the total College Enrollment for each Community Area.
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from SCHOOLS \
   group by Community_Area_Name 

#9.Get the 5 Community Areas with the least total College Enrollment sorted in ascending order.
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from SCHOOLS \
   group by Community_Area_Name \
   order by TOTAL_ENROLLMENT asc \
   fetch first 5 rows only

#10. List 5 schools with the lowest safety score.
%sql SELECT name_of_school, safety_score \
FROM schools \
ORDER BY safety_score \
LIMIT 5
#order by() is ascending by default


#11.Get the hardship index for the community area which has College Enrollment of 4368.
%%sql 
select hardship_index 
   from chicago_socioeconomic_data CD, schools CPS 
   where CD.ca = CPS.community_area_number 
      and college_enrollment = 4368




#12.Get the hardship index for the community area which has the school with the highest enrollment
%sql select ca, community_area_name, hardship_index from chicago_socioeconomic_data \
   where ca in \
   ( select community_area_number from schools order by college_enrollment desc limit 1 )



