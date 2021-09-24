"""
    "title": "World Bank Downloader"
    "description": "A Python script that download the data from World Bank"
    "version": "1.0.3"
    "author": "Konrad Brodziak"
"""

import urllib.request as ur
from bs4 import BeautifulStoneSoup as bs
import json

datajson=json.load(open('WorldBank.json'))

class Downloader:
    '''Get the data from World Bank and save to .xml file'''
    def __init__(self, url, countryiso3code, indicator, series_code):
        self.url = url
        self.countryiso3code = countryiso3code
        self.indicator = indicator
        self.series_code = series_code

    def main(self):
        '''Save the data to .xml file'''
        web=str(self.url)+str(self.countryiso3code)+str(self.indicator)+str(self.series_code)
        html=ur.urlopen(web).read()

        xml=bs(html)
        with open('WorldBank.xml', 'w', encoding='utf-8') as file_xml:
            file_xml.write(str(xml))

if __name__ == '__main__':
    Downloader(
        datajson['url'],
        datajson['countryiso3code'],
        datajson['indicator'],
        datajson['seriescode']
        ).main()
