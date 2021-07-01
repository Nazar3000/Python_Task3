import scrapy
from scrapy.http import Request, FormRequest
import logging


class AmazonImgSpider(scrapy.Spider):
    name = 'amazon_img'
    allowed_domains = ['amazon.com']
    start_urls = ["https://www.amazon.com/"]
    handle_httpstatus_list = [503, 403]

    def parse(self, response):
        """ a method that will be called to handle the response downloaded
        for each of the requests made.

        :param response:TextResponse, is an instance of TextResponse
        that holds the page content and has further helpful methods to handle it.
        :return:dict, scraped data as dicts
        """
        if response.status not in self.handle_httpstatus_list:
            yield Request(
                f"https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Darts-crafts-intl-ship&field-keywords=",
                callback=self.parse_img_url,
                dont_filter=False,
            )
        else:
            logging.info(f"{'*' * 15}Your ip is banned, please try using a different proxy! {'*' * 15}")

    def parse_img_url(self, response):
        """
        :param response: TextResponse, is an instance of TextResponse
        :return: clean_image_urls, nested list of links to images in the dictionary.
        """
        im_urls = response.selector.xpath(
            '//*[contains(@class, "a-image-container")]/img/@src').extract()
        logging.info(f"{'*' * 15} im_url = {im_urls}{'*' * 15}")
        clean_image_urls = []
        for img_url in im_urls:
            clean_image_urls.append(response.urljoin(img_url))
        logging.info(f"{'*' * 15} clean_image_urls = {clean_image_urls}{'*' * 15}")

        yield {
            'image_urls': clean_image_urls
        }
