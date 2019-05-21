from spider import Spider
from spider import MultiThreadedSpider
import pandas as pd

class ShoppingSpider(MultiThreadedSpider):
    start_urls = ["https://www.webscraper.io/test-sites/e-commerce/static/computers/laptops"]

    def on_start(self):
        self.data = []

    def process(self, response):
        for a in response.doc(".caption a").items():
            self.crawl(a.attr("href"), self.detail)
        for a in response.doc(".pagination a").items():
            self.crawl(a.attr("href"), self.process)
            
    def detail(self, response):
        product_name = response.doc("div.caption > h4:nth-child(2)").text()
        price = response.doc("div.caption > .price").text()
        description = response.doc("div.caption > .description").text()
        review = response.doc("div.ratings > p").text()
        self.data.append({"Product Name":product_name, "Price":price, "Description":description, "Review":review})
        
    def on_end(self):
        df = pd.DataFrame.from_dict(self.data)
        df.to_excel("laptops.xlsx")
            
ShoppingSpider().start()