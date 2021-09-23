"""
    "title": "World Bank Analyzer"
    "description": "A Python script that analyse the data from World Bank"
    "version": "1.0.0"
    "author": "Konrad Brodziak"
"""

from bs4 import BeautifulSoup, BeautifulStoneSoup as bs
import pandas as pd
import pmdarima as pm
from pmdarima.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

def main():
    with open('WorldBank.xml', 'r') as f:
        data = f.read()
    # Passing the stored data inside
    # the beautifulsoup parser, storing
    # the returned object
    bs_data = bs(data)
 
    # Finding all instances of tag
    # `wb:date` & `wb:value`
    wb_dates = bs_data.findAll('wb:date')
    wb_values = bs_data.findAll('wb:value')

    #Create list of `dates_list`
    dates_list = []
    for list in wb_dates:
        dates_list.append(list.get_text())
    #Create list of `values_list`
    values_list = []
    for list in wb_values:
        values_list.append(list.get_text())
    #Reverse lists
    dates=dates_list[::-1]
    values=values_list[::-1]
    values_a=values[0:5]
    df=pd.DataFrame({'Date': dates, 'Values': values})

    df_head=df.head()
    df_tail=df.tail()

    split_point = round(len(df_head)*(3/4))
    df1_train = df_head[:split_point]
    len_train = len(df1_train)
    df1_test = df_head[split_point:]
    len_test = len(df1_test)
    
    arima1 = pm.auto_arima(df1_train.Values, start_p=1, start_q=1,
                      max_p=3, max_q=3, # maximum p and q
                      m=10,              # frequency of series
                      seasonal=False,   # No Seasonality
                      start_P=0, 
                      suppress_warnings=True, 
                      stepwise=True, 
                      maxiter = 100, )
    print(arima1.summary())
    

if __name__ == '__main__':
    main()