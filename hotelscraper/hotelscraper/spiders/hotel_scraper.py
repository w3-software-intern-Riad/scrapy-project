import scrapy

import re
import json
import random
from hotelscraper.items import HotelItem
class HotelScraper(scrapy.Spider):
    name = "hotelscraper"
    start_urls = [
        "https://uk.trip.com/hotels/?locale=en-GB&curr=GBP",
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)
    def parse(self, response):
       
       
        script_content = response.css('script[type="text/javascript"]::text').get()

        if 'window.IBU_HOTEL' in script_content:
            # Use regex to extract the JSON-like object
            json_string_match = re.search(r'window.IBU_HOTEL\s*=\s*({.*?});', script_content, re.DOTALL)
            
            if json_string_match:
                json_string = json_string_match.group(1)
                
                # Convert the string to a Python dictionary
                hotel_data = json.loads(json_string)
                
                # Now, you can access any value within the dictionary
                init_data = hotel_data.get('initData', {})
                seo_content = init_data.get('htlsData',{}).get('inboundCities')
                outboundCities=init_data.get('htlsData',{}).get('outboundCities')
                fiveStarHotel=init_data.get('htlsData',{}).get('fiveStarHotels')
                list_of_headings=[seo_content,outboundCities,fiveStarHotel]
                random_list = random.choice(list_of_headings)
                
               
   
              
                url_list = []
                for content in random_list:
                    recommend_hotels = content.get('recommendHotels', [])
                    for link in recommend_hotels:
                        propertyTitle=link.get('hotelName')
                        latitude=link.get('lat')
                        longitude=link.get('lon')
                        location=link.get('fullAddress')
                        jump_url = link.get('hotelJumpUrl')
                        rating=link.get('rating')
                        prices=link.get('prices',{}).get('priceInfos',[])
                        price=prices[0].get('price')
                        item = HotelItem(
                        propertyTitle=propertyTitle,
                        latitude= latitude,
                        longitude= longitude,
                        location= location,
                        rating= rating,
                        price= price
                        )
                        if jump_url:
                            url_list.append(jump_url)
                            yield scrapy.Request(jump_url,callback=self.parse_room_data,meta={'item': item})
                        else:
                            yield hotel_data


                    
                         
                         
                    
               
    def parse_room_data(self, response):
        item = response.meta['item']
        all_script_content = response.css('script::text').getall()
        

        for content in all_script_content:
            if "seoHotelRooms" in content:
                index=content.find("seoHotelRooms")
                extracted_content = content[index-1:]
                
                cleaned_content = extracted_content.replace('\\\"', '"').replace('\\"', '"')
                if "urlDomain" in extracted_content:
                    ind=extracted_content.find("urlDomain")
                    
                    last_content=extracted_content[:ind-3].replace('\\\"', '"').replace('\\"', '"')
                    last_content = '{' + last_content
                    
                    try:
                        json_object = json.loads(last_content)
                        rooms=json_object.get("seoHotelRooms",{}).get("physicRoomMap",{})
                        

                        for room_id, room_info in rooms.items():
                            name = room_info.get("name", "default")
                            picture_info = room_info.get("pictureInfo", [])
                            image_urls = [pic.get("url") for pic in picture_info]
                            item['roomType']=name
                            item['images']=image_urls
                        yield item
                            
                        
                    except json.JSONDecodeError as e:
                        print(f"Error decoding JSON: {e}")
                 
                
                 


            
           