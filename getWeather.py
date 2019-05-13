# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import re
from pyquery import PyQuery as pq

doc = pq("http://www.weather.com.cn/index/lssj/index.shtml", encoding="utf-8")
doc.make_links_absolute("http://www.weather.com.cn/index/lssj/index.shtml")

for i in range(20):
    for title in doc("body > div.weatherMain > div.weatherLeft > div > ul.newList").items():
        print(title.text())
        nextPageURL = doc("body > div.weatherMain > div.weatherLeft > div > ul.pageClass > li:nth-child(6) > a").attr("href")
        nextPage = pq(nextPageURL)