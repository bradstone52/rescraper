import scrapy

from scrapy_splash import SplashRequest

class ColliersSpider(scrapy.Spider):
    name = 'colliers'

    base_url = 'https://www.collierscanada.com'

    
    
    def start_requests(self):
        url = 'https://www.collierscanada.com/en-ca/properties'

        yield SplashRequest(url=url, callback=self.parse, args={'wait': 10})

    def parse(self, response):
        links = response.xpath("//div[@class='teaser-card-container']/a[@class='CoveoResultLink']/@href").extract()

        for link in links:
            absolute_url = self.base_url + link
            yield SplashRequest(url=absolute_url, callback=self.parse_details, args={'wait': 5})

        
    def parse_details(self, response):
        yield {
            "Address": response.xpath("//h2[@class='property-address']/text()").get(),
            "Property Description": response.xpath("normalize-space(//h3[@class='property-description']/text())").get()
        }