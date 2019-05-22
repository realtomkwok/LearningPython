import os
import re
import time
from spider import Spider, MultiThreadedSpider, ChromeSpider
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
import pandas as pd

class WeatherSpider(Spider):
    start_urls = ['http://www.weather.com.cn/index/lssj/index.shtml']

    def process(self, response):
        for link in response.doc(".newList a").items():
            print(link.text())
        for link in response.doc(".pageClass a").items():
            self.crawl(link.attr("href"))


class LaptopSpider(MultiThreadedSpider):
    start_urls = ['https://www.webscraper.io/test-sites/e-commerce/static/computers/laptops']

    def on_start(self):
        self.data = []

    def process(self, response):
        for a in response.doc(".caption a").items():
            self.crawl({
                "url": a.attr("href"),
                "page_id": response.doc(".pagination .active").text()
                }, self.detail)
        for a in response.doc(".pagination a").items():
            self.crawl(a.attr("href"))

    def detail(self, response):
        data = {
            "price": response.doc(".price").text(),
            "title": response.doc("div.caption > h4:nth-child(2)").text(),
            "review": response.doc("div.ratings > p").text()
        }
        if response.data:
            data.update(response.data)
        self.data.append(data)

    def on_end(self):
        print(self.data, len(self.data))


class AjaxSpider(MultiThreadedSpider, ChromeSpider):
    headless = False

    def on_start(self):
        url = "https://tool.vample.com/courses/oop/resources/js-scrape.html"
        self.start_urls = ["{}?q={}".format(url, str(i)) for i in range(3)]

    def process(self, response):
        response.browser.find_element_by_css_selector("#btn").click()
        print(response.browser.find_element_by_css_selector("#info").text)


class AdvancedAjaxSpider(ChromeSpider):
    start_urls = ["https://tool.vample.com/courses/oop/resources/ajax-scrape/"]
    headless = False

    def process(self, response):
        year_links = response.browser.find_elements_by_css_selector(".year-link")
        for link in year_links:
            link.click()
            # https://selenium-python.readthedocs.io/waits.html
            wait = WebDriverWait(response.browser, 10)  # timeout after 10 secs
            time.sleep(2)
            wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "table"))
            )
            doc = pq(response.browser.page_source)
            table_data = [[td.text() for td in tr.find("td").items()] for tr in doc(".table tr").items()]
            print(table_data)


if __name__ == "__main__":
    start = time.time()
    # WeatherSpider().start()
    LaptopSpider().start()
    # AjaxSpider().start()
    # AdvancedAjaxSpider().start()
    print(time.time() - start)
