import scrapy, time
from stockscrap.items import StockscrapItem


class StockbotsSpider(scrapy.Spider):
    name = 'stockbots'
    allowed_domains = ['finance.naver.com/item/main.nhn?code=005930']
    start_urls = ['https://finance.naver.com/item/main.nhn?code=005930']

    def parse(self, response):
        read_time = time.strftime('%c', time.localtime(time.time()))
        volume = response.xpath('//*[@id="middle"]/dl/dd[11]/text()').extract()
        price = response.xpath('//*[@id="middle"]/dl/dd[4]/text()').extract()
        max_price = response.xpath('//*[@id="middle"]/dl/dd[7]/text()').extract()
        min_price = response.xpath('//*[@id="middle"]/dl/dd[9]/text()').extract()
        ticker_code = response.xpath('//*[@id="middle"]/dl/dd[3]/text()').extract()

        print('-----------------------------------------')
        print('read_time : ', read_time)
        print('volume : ', volume)
        print('price : ', price)
        print('max_price : ', max_price)
        print('min_price : ', min_price)
        print('ticker_code : ', ticker_code)
        print('-----------------------------------------')
        item = StockscrapItem()
        item['read_time'] = read_time
        item['volume'] = volume[0].split(' ')[1]
        item['price'] = price[0].split(' ')[1]
        item['max_price'] = max_price[0].split(' ')[1]
        item['min_price'] = min_price[0].split(' ')[1]
        item['ticker_code'] = ticker_code[0].split(' ')[1]
        return item