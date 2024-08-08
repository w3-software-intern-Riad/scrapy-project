import scrapy
from scrapy_splash import SplashRequest # type: ignore
import re
import json

class HotelScraper(scrapy.Spider):
    name = "hotelscraper"
    start_urls = [
        "https://uk.trip.com/hotels/?locale=en-GB&curr=GBP",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
        # Print the entire HTML for debugging purposes
        #
        script_content = response.css('script[type="text/javascript"]::text').get()
   
        yield {"title":script_content}
