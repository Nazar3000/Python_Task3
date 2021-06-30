import scrapy
from scrapy.http import Request, FormRequest
import logging


class AmazonImgSpider(scrapy.Spider):
    name = 'amazon_img'
    allowed_domains = ['amazon.com']
    start_urls = ["https://www.amazon.com/"]
    handle_httpstatus_list = [503, 403]

    def parse(self, response, **kwargs):
        if response.status not in self.handle_httpstatus_list:
            yield Request(
                f"https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Darts-crafts-intl-ship&field-keywords=",
                callback=self.parse_img_url,
                # endpoint='render.html',
                dont_filter=False,
            )

    def parse_img_url(self, response):
        im_url= response.selector.xpath(
            '//*[contains(@class, "a-image-container")]/img/@src').extract()
        logging.info(f"{'*' * 10} im_url = {im_url}")
