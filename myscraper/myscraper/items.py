# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscraperItem(scrapy.Item):
    ticker_code = scrapy.Field()
    volume = scrapy.Field()
    price = scrapy.Field()
    max_price = scrapy.Field()
    min_price = scrapy.Field()
    read_time = scrapy.Field()
