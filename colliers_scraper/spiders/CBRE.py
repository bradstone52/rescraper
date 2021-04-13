import scrapy


class CbreSpider(scrapy.Spider):
    name = 'CBRE'
    allowed_domains = ['www.commerciallistings.cbre.ca/en-CA/listings/industrial/results?aspects=isSale']
    start_urls = ['http://www.commerciallistings.cbre.ca/en-CA/listings/industrial/results?aspects=isSale/']

    def parse(self, response):
        pass
