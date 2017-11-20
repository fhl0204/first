#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import csv
import codecs
from tmp import get_all_list

codes = ['513050', '001668', '110011', '110012', '000011', '210009', '000961']
url = 'http://fund.eastmoney.com/allfund.html'

codes = get_all_list(url)

filename = 'result.csv'


def getHtml(url):
    req_header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Accept': 'text/html;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'utf-8',
        'Connection': 'close',
        'Referer': None  # 注意如果依然不能抓取的话，这里可以设置抓取网站的host
        }
    req_timeout = 10
    req = urllib2.Request(url, None, req_header)
    resp = urllib2.urlopen(req, None, req_timeout)
    html = resp.read()
    return html


def parse_one(code):
    url = 'http://fund.eastmoney.com/' + code + '.html'
    html = getHtml(url)

    pattern = '<dl class="dataItem02">.*?</dl>'
    m = re.search(pattern, html)
    if m:
        content = m.group(0)  # dateIemm02
    else:
        content = 'NULL'

    pattern2 = '<dd class="dataNums">.*?</dd>'
    content2 = re.search(pattern2, content)
    if content2:
        content2 = content2.group(0)
    else:
        content2 = 'NULL'

    pattern3 = '<span\sclass="[^">]+">([^<>]+)</span>'
    content3 = re.search(pattern3, content2)
    if content3:
        price = content3.group(1)
    else:
        price = 'NULL'

    pattern4 = '<dt>.*?</dt>'  # 带时间的dt->p->
    content4 = re.search(pattern4, content)
    if content4:
        content4 = content4.group(0)
    else:
        content4 = 'NULL'

    pattern5 = '\(</span>.*?<'  # (</span>2016-10-27)<
    content5 = re.search(pattern5, content4)
    if content5:
        content5 = content5.group()

    if content5:
        time = content5[8: len(content5) - 2]
    else:
        time = 'NULL'

    pattern6 = '<div class="fundDetail-tit">.*?</div>'
    content6 = re.search(pattern6, html)
    if content6:
        content6 = content6.group(0)
        content6 = content6.replace('<div class="fundDetail-tit">', '')
    else:
        content6 = 'NULL'

    pattern7 = 'left">.*?<span'

    content7 = re.search(pattern7, content6)
    if content7:
        content7 = content7.group(0)
        name = content7[6:len(content7) - 5]
    else:
        content7 = 'NULL'


    pattern8 = '<dd><span>近1月：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd>'
    month1 = re.search(pattern8, html)
    if month1:
        month1 = month1.group(2)
    else:
        month1 = 'NULL'

    pattern9 = '<dd><span>近3月：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd>'
    month3 = re.search(pattern9, html)
    if month3:
        month3 = month3.group(2)
    else:
        month3 = 'NULL'

    pattern10 = '<dd><span>近6月：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,5}.\d{2}%|--)</span></dd>'
    month6 = re.search(pattern10, html)
    if month6:
        month6 = month6.group(2)
    else:
        month6 = 'NULL'

    pattern11 = '<dd><span>近1年：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd></dl>'
    year1 = re.search(pattern11, html)
    if year1:
        year1 = year1.group(2)
    else:
        year1 = 'NULL'

    pattern12 = '<dd><span>近3年：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd>'
    year3 = re.search(pattern12, html)
    if year3:
        year3 = year3.group(2)
    else:
        year3 = 'NULL'

    pattern13 = '<dd><span>成立来：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,5}.\d{2}%|--)</span></dd>'
    until_now = re.search(pattern13, html)
    if until_now:
        until_now = until_now.group(2)
    else:
        until_now = 'NULL'

    writeResult(name, code, price, time, month1, month3, month6, year1, year3, until_now)


def writeResult(name, code, price, time, month1, month3, month6, year1, year3, until_now):
    item = [name, code, price, time, month1, month3, month6, year1, year3, until_now]
    csvfile = open(filename, 'ab')
    csvfile.write(codecs.BOM_UTF8)
    writer = csv.writer(csvfile, dialect='excel')
    writer.writerow(item)
    csvfile.close()


item = ['name', 'number', 'value', '     time     ', 'month1' , 'month3', 'month6', 'year1', 'year3', 'until_now']
csvfile = open(filename, 'wb')
csvfile.write(codecs.BOM_UTF8)
writer = csv.writer(csvfile)
writer.writerow(item)
csvfile.close()

for code in codes:
        parse_one(code)

print '\n'