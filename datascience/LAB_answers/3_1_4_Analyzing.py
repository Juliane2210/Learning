#ANALYZING A REAL WORLD DATA-SET WITH SQL AND PYTHON:

#Read Jupyter notebook for information on 'Selected Socioeconomic Indicators in Chicago'.
#1) ca: Used to uniquely identify each row of the dataset
#2) community_area_name: The name of the region in the city of Chicago
#3) percent_of_housing_crowded: Percent of occupied housing units with more than one person  per room
#4) percent_households_below_poverty: Percent of households living below the federal poverty line
#5) percent_aged_16_unemployed: Percent of persons over the age of 16 years that are unemployed.
#6) percent_aged_25_without_high_school_diploma: Percent of persons over the age of 25 years without a high school education
#7) percent_aged_under_18_or_over_64: Percent of population under 18 or over 64 years of age
#8) per_capita_income_: Community area per capita income is estimated as the sum of tract-level aggregate incomes divided by the total population
#9)hardship_index: Score that incorporates each of the six selected socioeconomic indicators



#CONNECTION TO THE DATABASE
#we first load the SQL extension and establish a connection with the database.

# These libraries are pre-installed in SN Labs. If running in another environment please uncomment lines below to install them:
# !pip install --force-reinstall ibm_db==3.1.0 ibm_db_sa==0.3.3
# Ensure we don't load_ext with sqlalchemy>=1.4 (incompadible)
# !pip uninstall sqlalchemy==1.4 -y && pip install sqlalchemy==1.3.24
# !pip install ipython-sql


%load_ext sql

%sql ibm_db_sa://vjm09314:Ok9eVz8jSEnSViqR@ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud:31321/BLUDB?security=SSL
#'Connected: vjm09314@BLUDB'

#STORE THE DATASET IN A TABLE:
#In many cases the dataset to be analyzed is available as a .CSV file on the internet.
#To analyze the data using SQL, it first needs to be stored in the database.
#We will first read the dataset source .CSV from the internet into pandas dataframe.
#Then we need to create a table in our Db2 database to store the dataset.
#The PERSIST command in SQL "magic" simplifies the process of table creation and writing the data from a 'pandas' dataframe into the table.

import pandas
chicago_socioeconomic_data = pandas.read_csv('https://data.cityofchicago.org/resource/jcxq-k9xf.csv')
%sql PERSIST chicago_socioeconomic_data

#PROBLEMS:
#1. How many rows in the dataset?
%sql SELECT COUNT(*) FROM chicago_socioeconomic_data;
#should get 78

#2.How many community areas in Chicago have hardship index greater than 50.0?
%sql  SELECT COUNT(*) FROM chicago_socioeconomic_data WHERE hardship_index > 50.0;
#should get 38

#3. What is the maximum value of hardship index in this dataset?
%sql SELECT MAX(hardship_index) FROM chicago_socioeconomic_data;
#should get 98.0

#4. Which community area has the highest hardship index?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE hardship_index = 98.0;
#should get Riverdale

#ANOTHER OPTION: 
# %sql select community_area_name 
# from chicago_socioeconomic_data where hardship_index = ( select max(hardship_index) from chicago_socioeconomic_data ) 


#5. Which Chicago community areas have per-capita incomes greater than $60,000?
%sql SELECT community_area_name FROM chicago_socioeconomic_data WHERE per_capita_income_ > 60000;
#should get: Lake View, Lincoln Park, Near North Side, Loop

#6. Create a scatter plot using the variables 'per_capita_income_' and 'hardship_index'.
#Explain the correlation between the two variables.

# !pip install seaborn==0.9.0
import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns


income_vs_hardship = %sql SELECT per_capita_income_, hardship_index FROM chicago_socioeconomic_data;
plot = sns.jointplot(x='per_capita_income_',y='hardship_index', data=income_vs_hardship.DataFrame())
#Correct answer:You can see that as Per Capita Income rises as the Hardship Index decreases.
#  We see that the points on the scatter plot are somewhat closer to a straight line in the negative direction,
#  so we have a negative correlation between the two variables. 



#CONCLUSION:
#Now that you know how to do basic exploratory data analysis using SQL and python visualization tools,
#you ca further explore this dataset to see how the variable 'per_capita_income' is related to 'percent_households_below_poverty'
#and 'percent_aged_16_unemployed'. Try to create interesting visualizations.



