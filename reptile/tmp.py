#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import requests
from bs4 import BeautifulSoup

url = 'http://fund.eastmoney.com/allfund.html'
#url = 'http://fund.eastmoney.com/000011.html'



def get_all_list(url):
    html = requests.get(url).content


    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

    # tags = soup.find_all('li', class_='increaseAmount')
    # tags = tags.find_all('div')

    tags=soup.find_all('li', class_='b')

    # m1=tags[3].string
    # y1=tags[4].string
    # m3=tags[5].string
    # y3=tags[6].string
    # m6=tags[7].string
    # rece=tags[8].string
    # detail={'近1月':m1,'近3月':m3,'近6月':m6,'近1年':y1,'近3年':y3,'成立来':rece}
    # print(detail)

    all_list = []
    for tag in tags:
        pattern = '\d{6}'
        tag = tag.prettify()
        result = re.search(pattern, tag)
        if result:
            all_list.append(result.group())

    print len(all_list), all_list
    return all_list
