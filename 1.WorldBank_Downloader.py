"""
    "title": "World Bank Downloader"
    "description": "A Python script that download the data from World Bank"
    "version": "1.0.0"
    "author": "Konrad Brodziak"
"""

import urllib.request as ur
from bs4 import BeautifulStoneSoup as bs

def main():
    url='https://api.worldbank.org/v2/country/afg/indicator'
    series_code='/NY.GDP.MKTP.CN'
    web=str(url)+str(series_code)
    html=ur.urlopen(web).read()
    xml=bs(html)

    with open('WorldBank.xml', 'w') as f:
        f.write(str(xml))

if __name__ == '__main__':
    main()