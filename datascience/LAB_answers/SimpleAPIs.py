#Application Programming Interface(API):

#REST API allows you to access resources via the internet.
#We will review the Pandas Library in the context of an API and review the basic REST API


#Pandas is an API:

import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.offline import plot
import matplotlib.pyplot as plt
import datetime
from pycoingecko import CoinGeckoAPI
from mplfinance.original_flavor import candlestick2_ohlc

#we create a dictionary:
dict_={'a':[11,21,31],'b':[12,22,32]}

#When we create a pandas object with the dataframe constructor, 
#this is an 'instance' in API lingo.
#the data in the dict is passed along to the pandas API and then we use the dataframe to communicate with the API.

df=pd.DataFrame(dict_)
print(type(df)) #class 'pandas.core.frame.DataFrame'

#when we call the method 'head' the dataframe communicates with the API displaying 
#the first few rows of the dataframe

print(df.head())

#calling 'mean', the API calculates the mean and returns the value:
print(df.mean())

#REST APIs:
#Rest APIs send requests which is communicated via HTTP message.
#The HTTP message usually contains a JSON file.
#The request contains instructions for what operation we would like the service or resource to perform.
#In a similar manner, API returns a response, via HTTP message , usually contained within a JSON.


#in this lab we get an API to create a candlestick graph for bitcoin:

#We will use the API to get the price data for 30 days with 24 observation per day, (1 per hour).
#We find the max, min, open and close price per day meaning we will have 30 candlesticks
#and use that to generate the candlestick graph.
#Although we are using the CoinGecko API, we will use a Python client/wrapper
#for the API called PyCoinGecko.


#Let's start by getting the data we need:
# 'get_coin_market_chart_by_id(id, vs_currency, days).id' is the name of the coin we want
# 'vs_currency' is the currency you want the price in
#'days' is how many days back from today you want



cg = CoinGeckoAPI()

bitcoin_data = cg.get_coin_market_chart_by_id(id='bitcoin', vs_currency='usd', days=30)

print(type(bitcoin_data))#dict
#print(bitcoin_data)#long list of prices

#The response we get is in the form of a JSON which includes the price
#, market caps, and total volumes along with timestamps for each observation.
#we are focused on the prices so we will select that data:

bitcoin_price_data = bitcoin_data['prices']

print(bitcoin_price_data[0:5])

#We turn this data into a DataFrame:
data = pd.DataFrame(bitcoin_price_data, columns=['TimeStamp', 'Price'])
print(data)

#Now that we have the DataFrame we convert the timestamp to datetime and save it as a column
#called Date.
#We map our 'unix_to_datetime' to each timestamp and convert it to a 
#readable datetime.

data['date'] = data['TimeStamp'].apply(lambda d: datetime.date.fromtimestamp(d/1000.0))
print(data['date'])

#using this modified dataset, we now group by the 'Date' and find the
#min, max, open and close for the candlesticks.
candlestick_data = data.groupby(data.date, as_index=False).agg({"Price": ['min', 'max', 'first', 'last']})

#Finally we are now ready to use plotly to create our Candlestick Chart:

fig = go.Figure(data=[go.Candlestick(x=candlestick_data['date'],
                open=candlestick_data['Price']['first'], 
                high=candlestick_data['Price']['max'],
                low=candlestick_data['Price']['min'], 
                close=candlestick_data['Price']['last'])
                ])

fig.update_layout(xaxis_rangeslider_visible=False)

fig.show()

print(fig)



