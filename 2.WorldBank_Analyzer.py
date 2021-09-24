"""
    "title": "World Bank Analyzer"
    "description": "A Python script that analyse the data from World Bank"
    "version": "1.0.1"
    "author": "Konrad Brodziak"
"""

from math import isnan
from bs4 import BeautifulStoneSoup as bs
import pandas as pd
import pmdarima as pm
from pmdarima.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt

xml_source=open('WorldBank.xml').read()

def main():
    '''A method that analyse the data from World Bank'''
    #Create reverse of list of `dates_list`
    wbd=bs(xml_source).findAll('wb:date')
    dates_list = [list.get_text() for list in wbd][::-1]

    #Create reverse of list of `values_list`
    wbv=bs(xml_source).findAll('wb:value')
    values_list = [list.get_text() for list in wbv][::-1]

    df=pd.DataFrame({'Date': dates_list, 'Values': values_list}).to_numpy()
    df=np.where(df == '', '0', df) #replace '' to '0'
    #print(df[:, 1])
    
    train, test= train_test_split(df[:, 1], train_size=30)
    model=pm.auto_arima(train, seasonal=True, m=12)
    forecasts = model.predict(test.shape[0])
    x = np.arange(df[:, 1].shape[0])

    plt.plot(x[:30], train, c='blue')
    plt.plot(x[30:], forecasts, c='green')
    plt.show()

if __name__ == '__main__':
    main()
