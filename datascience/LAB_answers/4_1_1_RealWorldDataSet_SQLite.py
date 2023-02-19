#WORKING WITH A REAL WORLD DATA-SET USING SQL AND PYTHON:

#-> Chicago Public Schools-Progress Report Cards(2011-2012)


#CONNECT TO THE DATABASE:
#We load the ipython-sql extension and establish a connection with the database
#The syntax for connecting to magic sql using sqllite is
#  %sql sqlite://DatabaseName
#where DatabaseName will be your .db file

import csv, sqlite3

con = sqlite3.connect("RealWorldData.db")
cur = con.cursor()
#pip install -q pandas==1.1.5
%load_ext sql
%sql sqlite:///RealWorldData.db



#QUERY THE DATABASE SYSTEM CATALOG TO RETRIEVE TABLE METADATA:
#We verify that the table creation was successful by retrieving the list of all tables
#in our schema and checking wether the SCHOOLS table was created.

%sql SELECT name FROM sqlite_master WHERE type='table'

#QUERY THE DATABASE SYSTEM CATALOG TO RETRIEVE COLUMN METADATA:
#The SCHOOLS table contains a large number of columns. How many columns des this table have?

%sql SELECT count(name) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');
#should get 78

#Now we retrieve the list of columns in SCHOOLS table and their column type (datatype) and length.
%sql SELECT name,type,length(type) FROM PRAGMA_TABLE_INFO('CHICAGO_PUBLIC_SCHOOLS_DATA');

#PROBLEMS:
#Same as previous labs here are the answers

#1.
%sql select count(*) from CHICAGO_PUBLIC_SCHOOLS_DATA where "Elementary, Middle, or High School"='ES'

#2.
%sql select MAX(Safety_Score) AS MAX_SAFETY_SCORE from CHICAGO_PUBLIC_SCHOOLS_DATA

#3.
%sql select Name_of_School, Safety_Score from CHICAGO_PUBLIC_SCHOOLS_DATA where \
  Safety_Score= (select MAX(Safety_Score) from CHICAGO_PUBLIC_SCHOOLS_DATA)

#4.
%sql select Name_of_School, Average_Student_Attendance from CHICAGO_PUBLIC_SCHOOLS_DATA \
    order by Average_Student_Attendance desc nulls last limit 10 

#5.
%sql SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5

#6.
%sql SELECT Name_of_School, REPLACE(Average_Student_Attendance, '%', '') \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     order by Average_Student_Attendance \
     LIMIT 5

#7.
%sql SELECT Name_of_School, Average_Student_Attendance  \
     from CHICAGO_PUBLIC_SCHOOLS_DATA \
     where CAST ( REPLACE(Average_Student_Attendance, '%', '') AS DOUBLE ) < 70 \
     order by Average_Student_Attendance

#8.
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name 

#9.
%sql select Community_Area_Name, sum(College_Enrollment) AS TOTAL_ENROLLMENT \
   from CHICAGO_PUBLIC_SCHOOLS_DATA \
   group by Community_Area_Name \
   order by TOTAL_ENROLLMENT asc \
   LIMIT 5 

#10.
%sql SELECT name_of_school, safety_score \
FROM CHICAGO_PUBLIC_SCHOOLS_DATA  where safety_score !='None' \
ORDER BY safety_score \
LIMIT 5

#11.
%%sql 
select hardship_index from CENSUS_DATA CD, CHICAGO_PUBLIC_SCHOOLS_DATA CPS 
where CD.community_area_number = CPS.community_area_number 
and college_enrollment = 4368

#12.
#Note: For this solution to work the CHICAGO_SOCIOECONOMIC_DATA table 
#      as created in the last lab of Week 3 should already exist

%sql select community_area_number, community_area_name, hardship_index from CENSUS_DATA \
   where community_area_number in \
   ( select community_area_number from CHICAGO_PUBLIC_SCHOOLS_DATA order by college_enrollment desc limit 1 )
