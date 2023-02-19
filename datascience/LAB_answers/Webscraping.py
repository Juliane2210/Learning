#Web Scraping Lab



#pip install bs4
#pip install lxml==4.6.4
#pip install requests==2.26.0


from bs4 import BeautifulSoup # this module helps in web scrapping.
import requests  # this module helps us to download a web page

html="<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
soup = BeautifulSoup(html, "html.parser")
print(soup)#just to see

#first the document is converted to Unicode, and HTML entities are converted to Unicode characters.
#Beautiful Soup transforms a complex HTML document into a complex tree of Python objects.
#The bs(beautsoup) object can create other types of objects.

#We can use the method 'prettify()' to display the HTML in the nested structure:
print(soup.prettify())


#TAGS:
#let's say we want the title of the page and the name of the top paid player, we can use the tag.
#the tag object corresponds to an HTML tag in the original document (ex.: the tag title).

tag_object=soup.title
print("tag object:",tag_object)#tag object: <title>Page Title</title>

print("tag object type:",type(tag_object)) #tag object type: <class 'bs4.element.Tag'>

#If there is more than one tag with the same name, the first element with that tag name is called,
#this corresponds to the most paid player.

tag_object=soup.h3
print(tag_object)#<h3><b id="boldest">Lebron James</b></h3>

#b is the bold attribute. It helps to use the tree representation.
#We can navigate down the tree using the child attribute to get the name.


#Children, Parents, and Siblings:
#As you can see the object has 2 tags(the outer=parent, the inner=child)

tag_child =tag_object.b
print(tag_child)#<b id="boldest">Lebron James</b>

#you can access the parent with the parent:
parent_tag=tag_child.parent
print( parent_tag)#<h3><b id="boldest">Lebron James</b></h3>

#this is identical to :
print(tag_object)

#the parent of 'tag_object' is the 'body' element:
print(tag_object.parent)

#the sibling of 'tag_object' is the 'paragraph' element:
sibling_1=tag_object.next_sibling
print(sibling_1) #<p> Salary: $ 92,000,000 </p>

#sibling_2 is the header element which is also a sibling of both sibling_1 and tag_object:
sibling_2=sibling_1.next_sibling
print(sibling_2)#<h3> Stephen Curry</h3>

#EXERCISE:
#(next_sibling)
sibling_3=sibling_2.next_sibling
print(sibling_3)


#HTML Attributes:
#If the tag has attributes, the tag id='boldest' has a attribute 'id' whose value is 'boldest'.
#You can access a tag's attributes by treating the tag like a dict.:

print(tag_child['id']) #boldest
#we can access the dict. directly as 'attrs'
print(tag_child.attrs) #{'id': 'boldest'}

#We can also obtain the content if the attribute of the 'tag' using the Python 'get()' method.
print(tag_child.get('id'))


#Navigable String:
#A string corresponds to a bit of text or content within a tag.
#Beautiful soup uses the 'NavigableString' class to contain this text.
#In our HTML we can obtain the name of the first player by extracting the string of the 'Tag' object 'tag_child' as follows:

tag_string=tag_child.string
print(tag_string) #'Lebron James'
print(tag_child)

#we verify the type is Navigable String:
print(type(tag_string))


#A NavigableString is just like a Python string or Unicode string(to be more precise).
#The main difference is that it also supports some BeautifulSoup features.
#We can convert it to string object in Python:

unicode_string = str(tag_string)
print(unicode_string)

#Filter:
#Filters allow you to find complex patterns. The simplest filter is a string.
#Here we pass a string to a different filter method and BeautSoup will perform a match against that exact string.
# We consider the following HTML, stored as a string in the variable 'table':

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, "html.parser")
print(table_bs)


#find All:
#The find_all() method looks through a tag's descendants and retrieves all descendants
#that match your filters.

#The Method signature for find_all(name, attrs, recursive, string, limit, **kwargs)

#NAME:
#When we set the 'name' parameter to a tag name, the method will extract all the tags with that name and its children.
table_rows=table_bs.find_all('tr')
print(table_rows)

#The result is a Python Iterable just like a list, each element is a 'tag' object:
first_row =table_rows[0]
print(first_row) #<tr><td id="flight">Flight No</td><td>Launch site</td> <td>Payload mass</td></tr>

#the type is 'tag':
print(type(first_row))#<class 'bs4.element.Tag'>

#we can obtain the child:
print(first_row.td)#<td id="flight">Flight No</td>

#If we iterate through the list, each element corresponds to a row in the table:
for i,row in enumerate(table_rows):
    print("row",i,"is",row)



#As 'row' is a 'cell' object, we can apply the method 'find_all' to it and extract table cells
# in the object 'cells' using the tag 'td', this is all the children with the name 'td'.
# The result is a list, each element corresponds to a cell and is a 'Tag' object,
# we can iterate through this list as well.
# We can extract the content using the 'string' attribute.    

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('column',j,"cell",cell)

#If we use a list we can match against any item in that list:
list_input=table_bs .find_all(name=["tr", "td"])
print(list_input)


#ATTRIBUTES:

#If the argument is not recognized it will be turned into a filter on the tag's attributes.
#For ex.: the 'id' argument. Beautsoup will filter against each tag's 'id' attribute.
#For ex.: the first 'td' elements have a value of 'id' of 'flight',
#therefore we can filter based on that 'id' value. -> [<td id="flight">Flight No</td>]



#We can find all the elements that have links to the Florida Wiki page.

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")
print(list_input)

#If we set the 'href' attribute to True, regardless of what the value is, the code finds all tags with 'href' value:

print(table_bs.find_all(href=True))

#EXERCISE:

#find all elements without 'href' value:
print(table_bs.find_all(href=False))

#Using the soup object 'soup', find the element with the 'id' attribute content set to "boldest".
print(soup.find_all(id="boldest"))

#string:
#With string you can search for strings instead of tags, where we find all the elements with Florida:
print(table_bs.find_all(string="Florida")) #['Florida', 'Florida']

#find:
#The 'find_all()' method scans the entire document looking for results, it's if you are looking
# for one element you can use the 'find()' method to find the first element in the document.
#Consider the following table: (we store the HTML as a Python string and assign 'two_tables')

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

#We create a BeatSoup object 'two_tables_bs':
two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

#We can find the table using the tag name 'table':

print(two_tables_bs.find("table"))

#We can filter on the class attribute to find the second table, but because 'class' is a keyword in Python we add an underescore.

print(two_tables_bs.find("table",class_='pizza'))

#Downloading and Scraping the contents of a webpage:

#first we download the contents of the web page:
url = "http://www.ibm.com"

#We use 'get' to download the contents of the webpage in text format and store in a variable called 'data'.
data  = requests.get(url).text 

#We create a BeautSoup object using the BeautSoup constructor:
soup = BeautifulSoup(data,"html.parser")  # create a soup object using the variable 'data'

#Scrape all links: (?)

#SCRAPE ALL IMAGE TAGS:
for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


#SCRAPE DATA FROM HTML TABLES:
#The below url contains an html table with data about colors and color codes.
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

#Before proceeding to scrape a web site, we need to examine the contents, and the way data is organized on the website.
# We open the url(above) in our browser to check how many rows and columns are there in the color table.

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find a html table in the web page
table = soup.find('table') # in html table is represented by the tag <table>


#Get all rows from the table
for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].string # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))


    #SCRAPE DATA FROM HTML TABLES INTO A DATAFRAME USING BEAUTIFULSOUP AND PANDAS:

    import pandas as pd

#The below url contains html tables with data about world population.
url = "https://en.wikipedia.org/wiki/World_population"    

#Before proceeding to scrape a website, we need to examine the contents, and the data organization. 
#We open the above url in our browser to check the tables on the webpage.

# get the contents of the webpage in text format and store in a variable called data
data  = requests.get(url).text

soup = BeautifulSoup(data,"html.parser")

#find all html tables in the web page
tables = soup.find_all('table') # in html table is represented by the tag <table>

print(len(tables)) #26

#Assume that we are looking for the '10 most densely populated countries' table,
#we can look through the tables list and find the right one we are looking for based on the data
#in each table or we can search for the table name if it is in the table but this option might not always work.

for index,table in enumerate(tables):
    if ("10 most densely populated countries" in str(table)):
        table_index = index
print(table_index)

#See if you can locate the table name of the table, '10 most densely populated countries', below.
print(tables[table_index].prettify())


#We create our own dataframe from this table:
population_data = pd.DataFrame(columns=["Rank", "Country", "Population", "Area", "Density"])

for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if (col != []):
        rank = col[0].text
        country = col[1].text
        population = col[2].text.strip()
        area = col[3].text.strip()
        density = col[4].text.strip()
        population_data = population_data.append({"Rank":rank, "Country":country, "Population":population, "Area":area, "Density":density}, ignore_index=True)

population_data

#SCRAPE DATA FROM HTML TABLES INTO A DATAFRAME USING BEAUTIFULSOUP and read_html:
#Using the same 'url', 'data', 'soup' and 'tables' object as in the last section, we can
#use the 'read_html' function to create a DataFrame.

#The table we need is located in the 'tables[table_index]'.

#We can now use the 'pandas' function 'read_html' and give it the string version of the table
# as well as the 'flavor' which is the parsing engine 'bs4'.

print(pd.read_html(str(tables[5]), flavor='bs4'))

#The function 'read_html' always returns a list of DataFrames so we must pick the one we want out of the list.
population_data_read_html = pd.read_html(str(tables[5]), flavor='bs4')[0]

print(population_data_read_html)








#SCRAPE DATA FROM HTML TABLES INTO A DATAFRAME USING read_html:
#We can also use the 'read_html' function to directly get DataFrames from a 'url'.

dataframe_list = pd.read_html(url, flavor='bs4')

#We can see there are 25 DataFrames just like when we used 'find_all' on the 'soup' object.

print(len(dataframe_list))

#Finally we can pick the DataFrame we need out of the list:
print(dataframe_list[5])

#We can also use the 'match' parameter to select the specific table we want.
#If the table contains a string matching the text it will be read.

print(pd.read_html(url, match="10 most densely populated countries", flavor='bs4')[0])








