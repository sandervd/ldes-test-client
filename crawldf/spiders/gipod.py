import scrapy


class GipodSpider(scrapy.Spider):
    name = "gipod"
    allowed_domains = ["private-api.gipod.beta-vlaanderen.be"]
    start_urls = ["http://private-api.gipod.beta-vlaanderen.be/"]

    def parse(self, response):
        pass
