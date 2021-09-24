"""
    "title": "World Bank Analyzer"
    "description": "A Python script that analyse the data from World Bank"
    "version": "1.0.1"
    "author": "Konrad Brodziak"
"""

from bs4 import BeautifulSoup, BeautifulStoneSoup as bs
import pandas as pd
import pmdarima as pm
from pmdarima.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

xml_source=open('WorldBank.xml').read()

def main():
    #Create reverse of list of `dates_list`
    wbd=bs(xml_source).findAll('wb:date')
    dates_list = [list.get_text() for list in wbd][::-1]

    #Create reverse of list of `values_list`
    wbv=bs(xml_source).findAll('wb:value')
    values_list = [list.get_text() for list in wbv][::-1]

    df=pd.DataFrame({'Date': dates_list, 'Values': values_list})

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
