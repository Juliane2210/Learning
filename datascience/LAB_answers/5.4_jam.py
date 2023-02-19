import pandas as pd

import urllib.request

urllib.request.urlretrieve(
    "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx", "sample.xlsx")
df = pd.read_excel("sample.xlsx")


print(df)


#testing:

import pandas as pd

path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"
df = pd.read_csv(path)

#Identify and handle missing values:
#.isnull() or .notnull() -> output is boolean->True=missing, False=not missing
missing_data = df.isnull()
print(missing_data.head(5))


#Count  missing values in each column:
#(using a for loop):
for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("") 





