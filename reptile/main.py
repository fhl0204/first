#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import re
import csv
import codecs

codes = ['513050', '001668', '110011', '110012', '000011', '210009', '000961']

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
    req_timeout = 5
    req = urllib2.Request(url, None, req_header)
    resp = urllib2.urlopen(req, None, req_timeout)
    html = resp.read()
    return html


def parse_one(code):
    url = 'http://fund.eastmoney.com/' + code + '.html'
    html = getHtml(url)

    pattern = '<dl class="dataItem02">.*?</dl>'
    m = re.search(pattern, html)
    content = m.group(0)  # dateIemm02

    pattern2 = '<dd class="dataNums">.*?</dd>'
    content2 = re.search(pattern2, content).group(0)

    pattern3 = '<span\sclass="[^">]+">([^<>]+)</span>'
    content3 = re.search(pattern3, content2)
    price = content3.group(1)

    pattern4 = '<dt>.*?</dt>'  # 带时间的dt->p->
    content4 = re.search(pattern4, content).group(0)

    pattern5 = '\(</span>.*?<'  # (</span>2016-10-27)<
    content5 = re.search(pattern5, content4).group(0)

    time = content5[8: len(content5) - 2]

    pattern6 = '<div class="fundDetail-tit">.*?</div>'
    content6 = re.search(pattern6, html).group(0)
    content6 = content6.replace('<div class="fundDetail-tit">', '')
    pattern7 = 'left">.*?<span'

    content7 = re.search(pattern7, content6).group(0)
    name = content7[6:len(content7) - 5]

    pattern8 = '<dd><span>近1月：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd>'
    month1 = re.search(pattern8, html).group(2)

    pattern9 = '<dd><span>近3月：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd>'
    month3 = re.search(pattern9, html).group(2)

    pattern10 = '<dd><span>近6月：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,5}.\d{2}%|--)</span></dd>'
    month6 = re.search(pattern10, html).group(2)

    pattern11 = '<dd><span>近1年：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd></dl>'
    year1 = re.search(pattern11, html).group(2)

    pattern12 = '<dd><span>近3年：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,3}.\d{2}%|--)</span></dd>'
    year3 = re.search(pattern12, html).group(2)

    pattern13 = '<dd><span>成立来：</span><span class="ui-font-middle (ui-color-red|ui-color-green)? ui-num">(-?\d{1,5}.\d{2}%|--)</span></dd>'
    until_now = re.search(pattern13, html).group(2)

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