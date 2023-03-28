import sys
sys.path.append('/Users/apple/Desktop/developer/csgo_spider/csgo_spider')

import scrapy
from items import Item
from icecream import ic

class BuffSpider(scrapy.Spider):
    name = "buff"
    allowed_domains = ["4cola.com"]
    start_urls = ["https://www.4cola.com/skins"]

    def parse(self, response):
        items = []
    
        for each in response.xpath("//div[@id=\"v-data-table__wrapper\"]"):
            item = Item()

            name = each.xpath("./table/tbody/tr/td[2]/a/text()").extract()
            price = each.xpath("./table/tbody/tr/td[3]/text()").extract()

            item['name'] = name[0].strip()
            item['price'] = price[0].strip()

            items.append(item)
        return items
