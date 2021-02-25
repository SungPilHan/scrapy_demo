import scrapy
import time
from myscraper.items import MyscraperItem


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.daum.net/quotes/A005930#home']
    start_urls = ['https://finance.daum.net/quotes/A005930#home/']

    def parse(self, response):
        read_time = time.strftime('%c', time.localtime(time.time()))
        volume = response.xpath('//*[@id="boxSummary"]/div/span[2]/ul/li[3]/p/text()').extract()
        price = response.xpath('//*[@id="boxSummary"]/div/span[1]/span[1]/span[3]/strong/text()').extract()
        max_price = response.xpath('//*[@id="boxSummary"]/div/span[2]/ul/li[2]/p/text()').extract()
        min_price = response.xpath('//*[@id="boxSummary"]/div/span[2]/ul/li[5]/p/text()').extract()
        ticker_code = response.xpath('//*[@id="favorite"]/em/text()').extract()

        item = MyscraperItem()
        item['read_time'] = read_time
        item['volume'] = volume
        item['price'] = price
        item['max_price'] = max_price
        item['min_price'] = min_price
        item['ticker_code'] = ticker_code
        return item