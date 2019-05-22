import os
import re
from spider.spider import Spider, MultiThreadedSpider, ChromeSpider
from pyquery import PyQuery as pq
import pandas as pd

class houseSpider(MultiThreadedSpider):
    start_urls = ["https://gz.lianjia.com/zufang/"]

    def on_start(self):
        self.data = []

    def process(self, response):
        # current page
        for a in response.doc("p.content__list--item--title.twoline > a").items():
            self.crawl(a.attr("href"), self.detail)
        # next page
        # for a in response.doc(".content__pg a:not(.next)").items():
        #     self.crawl(a.attr("href"))

    def detail(self, response):
        data = {
            "title": response.doc(".content__title").text(),
            "rent": response.doc(".content__aside--title").text(),
            "type": response.doc(".content__aside__list span:nth-child(2)").text(),
            "area": response.doc(".content__aside__list span:nth-child(3)").text()
        }
        if response.data:
            data.update(response.data)
        self.data.append(data)

    def on_end(self):
        print(self.data)
        # df = pd.DataFrame.from_dict(self.data)
        # df.to_excel("houses.xlsx")
    
houseSpider().start()