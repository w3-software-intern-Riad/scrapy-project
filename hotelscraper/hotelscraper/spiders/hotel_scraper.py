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
# Use regex to extract the JSON-like part from the JavaScript variable
        if 'window.IBU_HOTEL' in script_content:
            # Use regex to extract the JSON-like object
            json_string_match = re.search(r'window.IBU_HOTEL\s*=\s*({.*?});', script_content, re.DOTALL)
            
            if json_string_match:
                json_string = json_string_match.group(1)
                
                # Convert the string to a Python dictionary
                hotel_data = json.loads(json_string)
                
                # Now, you can access any value within the dictionary
                init_data = hotel_data.get('initData', {})
                seo_content = init_data.get('recommends', {})
                
            
                
                yield {
                    'title1': init_data,
                    'content1': seo_content,
                }
