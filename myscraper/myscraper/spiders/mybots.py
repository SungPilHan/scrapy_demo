import scrapy


class MybotsSpider(scrapy.Spider):
    name = 'mybots'
    allowed_domains = ['finance.daum.net/quotes/A005930#home']
    start_urls = ['https://finance.daum.net/quotes/A005930#home/']

    def parse(self, response):
        pass
