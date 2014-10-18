import scrapy

class AnyItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    desc = scrapy.Field()

class AnySpider(scrapy.Spider):
    def __init__(self, url):
        self.url = url
        start_urls = [url]
        allowed_domains = ["*"]

    def parse(self, response):
        item = AnyItem()
        for sel in response.xpath('//ul/li'):
            item['title'] = sel.xpath('a/text()').extract()
            item['link'] = sel.xpath('a/@href').extract()
            item['desc'] = sel.xpath('text()').extract()
            yield item

