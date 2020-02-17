import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas  as pd

web = requests.get('https://in.finance.yahoo.com/quote/SBIN.NS/history/').text
soup = BeautifulSoup(web,'html.parser')

Date = []
Open = []
High = []
Low = []
Close = []
adjClose = []
Volumne = []

tr = soup.find_all('tr')

for j in range(7):

    for i in range(1, len(tr) - 1):

        if j == 0:
            Date.append(tr[i].find_all('td')[j].get_text())

        elif j == 1:
            Open.append(tr[i].find_all('td')[j].get_text())
        elif j == 2:
            High.append(tr[i].find_all('td')[j].get_text())
        elif j == 3:
            Low.append(tr[i].find_all('td')[j].get_text())
        elif j == 4:
            Close.append(tr[i].find_all('td')[j].get_text())
        elif j == 5:
            adjClose.append(tr[i].find_all('td')[j].get_text())
        elif j == 6:
            Volumne.append(tr[i].find_all('td')[j].get_text())

df = pd.DataFrame()
df['Date'] = Date
df['Open'] = Open
df['High'] = High
df['Low'] = Low
df['Close'] = Close
df['adjClose'] = adjClose
df['Volume'] = Volumne

df.drop([77],axis = 0,inplace=True)


def Open():
    return df.Open.values,df.index.values
