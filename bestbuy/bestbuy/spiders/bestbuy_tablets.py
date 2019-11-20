# -*- coding: utf-8 -*-
import scrapy


class BestbuyTabletsSpider(scrapy.Spider):
    name = 'bestbuy_tablets'
    allowed_domains = ['https://www.bestbuy.ca/en-ca/collection/save-on-tablets/63065?icmp=computing_evergreen_tablets_and_ipads_category_detail_feature_orientation_banner']
    start_urls = ['https://www.bestbuy.ca/en-ca/collection/save-on-tablets/63065?icmp=computing_evergreen_tablets_and_ipads_category_detail_feature_orientation_banner']

    custom_settings = {'FEED_URI': "bestbuy_tablets_%(time)s.csv",
                       'FEED_FORMAT': 'csv'}

    #custom_settings={ 'FEED_URI': "bestbuy_tablets_%(time)s.json",
    #                   'FEED_FORMAT': 'json'}

    def parse(self, response):

        print("procesing:"+response.url)
        #Extract data using css selectors
        product_name=response.css(".link_3hcyN  ::text").extract()
        price_range=response.css(".productPricingContainer_3gTS3 ::text").extract()
        #Extract data using xpath
        rating=response.css(".ratingContainer_29ZF- ::text").extract()
        #company_name=response.xpath("//a[@class='store $p4pLog']/text()").extract()

        row_data=zip(product_name,price_range,rating)

        #Making extracted data row wise
        for item in row_data:
            #create a dictionary to store the scraped info
            scraped_info = {
                #key:value
                'page':response.url,
                'product_name' : item[0], #item[0] means product in the list and so on, index tells what value to assign
                'price_range' : item[1],
                'rating' : item[2]
                #'company_name' : item[3],
            }

            #yield or give the scraped info to scrapy
            yield scraped_info

            # NEXT_PAGE_SELECTOR = '.content_3dXxd + a::attr(href)'
            # next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
            # if next_page:
            #     yield scrapy.Request(
            #         response.urljoin(next_page),
            #         callback=self.parse)