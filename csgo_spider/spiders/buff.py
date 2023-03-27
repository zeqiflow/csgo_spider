import scrapy


class BuffSpider(scrapy.Spider):
    name = "buff"
    allowed_domains = ["buff.163.com"]
    start_urls = ["http://buff.163.com/"]

    def parse(self, response):
        pass
