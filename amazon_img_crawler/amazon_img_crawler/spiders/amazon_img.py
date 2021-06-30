import scrapy


class AmazonImgSpider(scrapy.Spider):
    name = 'amazon_img'
    allowed_domains = ['amazon.com']
    start_urls = ['https://amazon.com/']

    def parse(self, response):
        pass
