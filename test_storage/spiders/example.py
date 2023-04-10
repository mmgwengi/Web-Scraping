# import scrapy
# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from ..items import TestStorageItem
# # https://www.youtube.com/watch?v=o1g8prnkuiQ&list=PLRzwgpycm-Fjvdf7RpmxnPMyJ80RecJjv&index=12
# class ExampleSpider(CrawlSpider):
#     name = "tst_storage"
#     allowed_domains=['sipwhiskey.com']
#     start_urls = [
#         'https://sipwhiskey.com/'
#     ]

#     rules=(
#         Rule(LinkExtractor(allow='collections/japanese-whisky',deny='products')),
#         Rule(LinkExtractor(allow='products'),callback='parse_item')
#         )


#     def parse_item(self, response):

#         yield{
#             'brand':response.css('div.vendor a::text').get()
#         }

###################################################################
###################################################################
###################################################################
###################################################################
import scrapy
import requests
import csv
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.linkextractors import IGNORED_EXTENSIONS
import logging
logging.getLogger("urllib3").setLevel(logging.WARNING) 
logging.getLogger("requests").setLevel(logging.WARNING)
# https://www.youtube.com/watch?v=o1g8prnkuiQ
# class PDFSpider(scrapy.Spider):


# class PDFSpider(CrawlSpider):
#     name = "tst_spider"
#     allowed_domains=['uah.edu']
#     start_urls = [
#         'https://www.uah.edu/hr/benefits/insurance/health'
#     ]
#     # custom_settings = {
#     #     "DEPTH_LIMIT": 5
#     # }

#     rules=(Rule(LinkExtractor(),callback='parse_pdf',follow=True),)

#     def parse_pdf(self, response):
#         # items = MunicipalitypdfItem()
#         for link in response.xpath("//a[@href]"):
#             url = link.xpath("@href").get()
#             # https://www.tiktok.com/@uahuntsville
#             complete_url=response.urljoin(url)
#             # print(complete_url)
#             try:
#                 response_complete_url=requests.get(complete_url,timeout=1) # only wait max of 3 seconds to get response
#             except requests.exceptions.RequestException:
#                 logging.error(f'Failed to download {complete_url}')
#             else:
#                 if 'Content-Type' in response_complete_url.headers and response_complete_url.headers['Content-Type'] == 'application/pdf':
#                 # print(complete_url)
#                     yield{'url':complete_url,
#                     'page':response.url}  


######################################################
######################################################


class PDFSpider(CrawlSpider):
    name = "tst_spider"
    allowed_domains=['rsa-al.gov']
    # start_urls = [
    #     'https://www.uah.edu/hr/benefits/insurance/health'
    # ]
    start_urls = ['https://www.rsa-al.gov/peehip/publications/']
    # custom_settings = {
    #     "DEPTH_LIMIT": 5
    # }

    rules=(Rule(LinkExtractor(),callback='parse_pdf',follow=True),)
    # rules = (
    #     Rule(
    #         LinkExtractor(
    #             unique=True,
    #             allow_domains = allowed_domains,
    #             deny_extensions=[i for i in IGNORED_EXTENSIONS if i!="pdf"],
    #         ),
    #         callback='parse_pdf',
    #         follow=True,
    #     ),
    # )

    def parse_pdf(self, response):
        # items = MunicipalitypdfItem()
        for link in response.xpath("//a[@href]"):
            url = link.xpath("@href").get()
            # https://www.tiktok.com/@uahuntsville
            complete_url=response.urljoin(url)
            # print(complete_url)
            response_complete_url=requests.get(complete_url,timeout=1) # only wait max of 3 seconds to get response
            if 'Content-Type' in response_complete_url.headers and response_complete_url.headers['Content-Type'] == 'application/pdf':
                # print(complete_url)
                    yield{'url':complete_url,
                    'page':response.url}  