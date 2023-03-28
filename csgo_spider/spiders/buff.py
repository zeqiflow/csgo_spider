import sys
sys.path.append('/Users/apple/Desktop/developer/csgo_spider/csgo_spider')

import scrapy
from items import Item
from icecream import ic

class BuffSpider(scrapy.Spider):
    name = "buff"
    allowed_domains = ["buff.163.com"]
    start_urls = ["https://buff.163.com/market/csgo#tab=selling&page_num=1&category=weapon_knife_skeleton"]

    def parse(self, response):
        items = []
    
        for each in response.xpath("//*[@id=\"j_list_card\"]"):
            item = CsgoItem()
            name = each.extract()

            # price = each.xpath("./td[@class=\"text-no-wrap\"]/h3/a/text()").extract()
            item['name'] = name[0].strip()
            # item['price'] = price[0].strip()

            items.append(item)
        return items
