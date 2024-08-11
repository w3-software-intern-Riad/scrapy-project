import scrapy

class HotelItem(scrapy.Item):
    propertyTitle = scrapy.Field()
    latitude = scrapy.Field()
    longitude = scrapy.Field()
    location = scrapy.Field()
    rating = scrapy.Field()
    price = scrapy.Field()
    roomType = scrapy.Field()
    images = scrapy.Field()
