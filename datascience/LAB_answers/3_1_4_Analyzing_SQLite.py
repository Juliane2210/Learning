#ANALYZING A REAL WORLD DATA-SET WITH SQL AND PYTHON:
#Same lab but with SQLite:


#CONNECT TO THE DATABASE:
#The syntax for connecting to magic sql using sqllite is %sql sqlite://DatabaseName
#where DatabaseName will be your .db file

%load_ext sql
import csv, sqlite3

con = sqlite3.connect("socioeconomic.db")
cur = con.cursor()
#pip install -q pandas==1.1.5

%sql sqlite:///socioeconomic.db
#'Connected: @socioeconomic.db'


#STORE THE DATASET IN A TABLE:
#In many cases the dataset to be analyzed is available as a .CSV file on the internet.
#To analyze the data using SQL, it first needs to be stored in the database.

#We will first read the csv files from the given url into pandas dataframes.

#Next we will be using the dt.to_sql() function to convert each csv file to a table in sqlite with the csv data loaded in it.

import pandas
df = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
df.to_sql("chicago_socioeconomic_data", con, if_exists='replace', index=False,method="multi")

#You can verify that the table creation was successful by making a basic query like:
%sql SELECT * FROM chicago_socioeconomic_data limit 5;

#PROBLEMS:
#1. 
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;

#2.
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;


#3.
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data; 

#4.
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE hardship_index = 98.0;

#5.
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;

#6.
# !pip install seaborn

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns

income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())

#Correct answer:You can see that as Per Capita Income rises as the Hardship Index decreases.
#  We see that the points on the scatter plot are somewhat closer to a straight line in the negative direction,
#  so we have a negative correlation between the two variables. 






