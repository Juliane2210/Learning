# Data Engineering:
#3 steps in the data engineering process:

#1)EXTRACT:
#data extraction= getting data from multiple sources.
#ex.: data extraction from a website using web scraping or gathering the data that
#are stored in different formats(JSON, CVS, XLSX...)


#2)TRANSFORM:
#removing the data that we don't need for further analysis and
#converting the data in the format that all the data from the multiple sources is in the same format.


#3)LOAD:
#Loading the data inside a data warehouse.
#Data warehouse essentially contains large volumes of data that are accessed to gather insights.




#CVS:
#(how to read a CVS file in Pandas Library)

import pandas as pd
import numpy as np

url ='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv'
df = pd.read_csv(url,header=None)
print(df)

#adding a column to the data frame:
df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']
print(df)


#selecting a single column:
print(df["First Name"])

#selecting multiple columns:
df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]
print(df)

#selecting rows using .iloc() and .loc()

#selecting the first row:
df.loc[0]

#Selecting the 0th,1st and 2nd row of "First Name" column only
df.loc[[0,1,2], "First Name"]

df.iloc[[0,1,2], 0]

#Transform Function in Pandas:

#creating a data frame:
df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
print(df)

#applying the transform function
df = df.transform(func = lambda x : x + 10)
print(df)

#again to find the square root:
result = df.transform(func = ['sqrt'])
print(result)




#JSON:
#(JavaScript Object Notation) is a lightweight data-interchange format.
#Is built on two structures:

#1) A collection of name/value pairs. In various languages, this is realized
#  as an object, record, struct, dictionary, hash table, keyed list, or associative array. 

#2) An ordered list of values. In most languages, this is realized as an array,
# vector list, or sequence.

#JSON is a language-independent data format.
#The text in JSON is done through quoted string which contains the values
#in key-value mappings within {}. (similar to dict)

import json


#WRITING json to a file:
#(usually called serialization)Is the process of converting an object into a special
#format which is suitable for transmitting over the network or storing in file/database.

#to handle data flow in file, JsON library in Python uses dump() or dumps()
#to convert the python objects into their respective JSON object.





#json.dump()

#syntax: json.dump(dict, file_pointer)
#parameters: 1) dictionary-name of dict which should be converted to JSON object.
# 2) file pointer-pointer of the file opened in write or append mode.


#dictionary which should be converted to JSON object: 
person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}


with open('peron.json', 'w') as f: #writing JSON object
    json.dump(person, f)


#json.dumps()
#parameters: 1) dictionary-name of dict which should be converted to JSON object.
# 2) indent-defines the number of units for indentation.

# Serializing json  
json_object = json.dumps(person, indent = 4) 
  
# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object)

print(json_object)     


#READING json to a file:
#(usually deserialization)converts the special format returned by the serialization
#back into a usable object.


#json.load() fct loads the json content from a json file into a dictionary.
#takes the file pointer(that points to a json file) as a parameter.

# Opening JSON file 
with open('sample.json', 'r') as openfile: 
  
    # Reading from json file 
    json_object = json.load(openfile) 
  
print(json_object) 
print(type(json_object)) 




#XLSX file format:





