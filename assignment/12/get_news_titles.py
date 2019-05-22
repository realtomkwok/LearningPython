import re
import os
from pyquery import PyQuery as pq

# get the website
doc = pq("http://www.weather.com.cn/index/lssj/index.shtml", encoding="utf-8")
doc.make_links_absolute("http://www.weather.com.cn/index/lssj/index.shtml")

# get the count of total pages
match = re.search("\d+",  doc("body > div.weatherMain > div.weatherLeft > div > ul.pageClass > li:nth-child(2)").text())
if match:
        totalPages = int(match.group(0))

# main program
with open("news_titles.txt", "a") as file:
        for i in range(totalPages):
                try:
                        for title in doc("body > div.weatherMain > div.weatherLeft > div > ul.newList").items():
                                print(title.text())
                                file.write(title.text() + "\n")
                                # go to next page if posible
                                nextPageURL = doc("body > div.weatherMain > div.weatherLeft > div > ul.pageClass > li:nth-child(6) > a").attr("href")
                        doc = pq(nextPageURL)
                        doc.make_links_absolute(nextPageURL)
                except TypeError:
                        print("News Titles are sucessfully extracted!")
                        break