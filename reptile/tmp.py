#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
import requests
from bs4 import BeautifulSoup
from main import getHtml

url = 'http://fund.eastmoney.com/allfund.html'
url = 'http://fund.eastmoney.com/000011.html'
html = requests.get(url).content

#html = getHtml(url)

soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

# tags = soup.find_all('li', class_='increaseAmount')
# tags = tags.find_all('div')

tags=soup.find_all(class_='ui-font-middle ui-color-red ui-num')
# m1=tags[3].string
# y1=tags[4].string
# m3=tags[5].string
# y3=tags[6].string
# m6=tags[7].string
# rece=tags[8].string
# detail={'近1月':m1,'近3月':m3,'近6月':m6,'近1年':y1,'近3年':y3,'成立来':rece}
# print(detail)

for tag in tags:
    print tag