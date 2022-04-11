# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

# create Items
class ScrapedInfo(scrapy.Item):
    title = scrapy.Field(serializer=str)
    summary = scrapy.Field(serializer=str)
    date = scrapy.Field(serializer=str)
    text = scrapy.Field(serializer=str)
    url = scrapy.Field(serializer=str)

