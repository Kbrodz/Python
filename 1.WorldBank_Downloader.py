"""
    "title": "World Bank Downloader"
    "description": "A Python script that download the data from World Bank"
    "version": "1.0.1"
    "author": "Konrad Brodziak"
"""

import urllib.request as ur
from bs4 import BeautifulStoneSoup as bs

class Downloader:
    def __init__(self, url, series_code):
        self.url = url
        self.series_code = series_code

    def main(self):
        '''Get the data from World Bank and save to .xml file'''
        web=str(self.url)+str(self.series_code)
        html=ur.urlopen(web).read()

        xml=bs(html)
        with open('WorldBank.xml', 'w', encoding='utf-8') as file_xml:
            file_xml.write(str(xml))

if __name__ == '__main__':
    Downloader(
        'https://api.worldbank.org/v2/country/afg/indicator',
        '/NY.GDP.MKTP.CN'
        ).main()
