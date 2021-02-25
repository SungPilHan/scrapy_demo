# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class StockscrapPipeline:
    def __init__(self):
        self.setupDBConnect()
        self.createTable()

    def process_item(self, item, spider):
        self.storeInDB(item)
        return item
    
    def storeInDB(self, item):
        # self.cur.execute("""
        # INSERT INTO movie_review(title, grade, review, user, date)
        # VALUES(\'{0}\', \'{1}\', \'{2}\', \'{3}\', \'{4}\')
        # """.format(item.get('title'), item.get('grade'), item.get('review'), item.get('user'), item.get('date')))

        sql = "INSERT INTO stock_view(ticker_code, volume, price, max_price, min_price, read_time) VALUES(%s, %s, %s, %s, %s, %s)"
        self.cur.execute(sql, (item.get('ticker_code'), item.get('volume'), item.get('price'), item.get('max_price'), item.get('min_price'), item.get('read_time')))

        self.conn.commit()

    def setupDBConnect(self):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='1234', db='mydb', charset='utf8')
        # self.conn = pymysql.connect(host='127.0.0.1', user='root', password='', db='mydb', charset='utf8')
        self.cur = self.conn.cursor()

        print("DB Connected")

    def createTable(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS stock_view(
            id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
            ticker_code VARCHAR(20),
            volume VARCHAR(20),
            price VARCHAR(20),
            max_price VARCHAR(20),
            min_price VARCHAR(20),
            read_time VARCHAR(50)
            )
        """)
