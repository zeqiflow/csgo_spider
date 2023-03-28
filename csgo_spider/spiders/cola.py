import sys
sys.path.append('/Users/apple/Desktop/developer/csgo_spider/csgo_spider')

import scrapy
from items import Item
from icecream import ic

class ColaSpider(scrapy.Spider):
    name = "cola"
    allowed_domains = ["4cola.com"]
    start_urls = ["https://www.4cola.com/skins"]

    def parse(self, response):
        items = []
    
        for each in response.xpath("//tr[@class=\"pointer\"]"):
            item = Item()

            name = each.xpath("./td[@class=\"text-no-wrap\"]/a/text()").extract()
            price = each.xpath("./td[@class=\"text-no-wrap\"][3]/text()").extract()

            item['name'] = name[0].strip()
            item['price'] = price[0].strip()

            items.append(item)

        return items
