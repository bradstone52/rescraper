import scrapy
from scrapy_splash import SplashRequest



class CbreSpider(scrapy.Spider):
    name = 'CBRE'

    base_url = 'http://www.commerciallistings.cbre.ca'


    def start_requests(self):
        url = 'http://www.commerciallistings.cbre.ca/en-CA/listings/industrial/results?aspects=isSale/'

        yield SplashRequest(url=url, callback=self.parse, args={'wait': 10})

    def parse(self, response):
        links = response.xpath("//a[@class='card_content']/@href").extract()

        for link in links:
            absolute_url = self.base_url + link
            yield SplashRequest(url=absolute_url, callback=self.parse_details, args={'wait': 5})

        
    def parse_details(self, response):
        yield {
            "Size": response.xpath("//div[@class='cbre_table__cell col-xs-6 col-sm-5 col-lg-4'][1]/span/text()").get(),
            "Property Description": response.xpath("//h1[@class='cbre_h1']/div/span/span/text()").get()
        }