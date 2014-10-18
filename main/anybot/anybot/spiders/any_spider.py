import scrapy

class AnySpider(scrapy.Spider):
    name = "any"
    allowed_domains = ["dmoz.org"]
    start_urls = [
                    "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
                    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
                    ]

    def parse(self, response):
        for sel in response.xpath('//ul/li'):
            title = sel.xpath('a/text()').extract()
            link = sel.xpath('a/@href').extract()
            desc = sel.xpath('text()').extract()
            yield title, link, desc
