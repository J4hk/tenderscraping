# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IlanSpider(CrawlSpider):
    name = 'ilan'
    allowed_domains = ['www.ilan.gov.tr']
    start_urls = ['https://www.ilan.gov.tr/kategori-ihale?type=21628']

    rules = (
        Rule(LinkExtractor(restrict_xpaths=('//li[@class = "item column col-12"]/div/a')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            'ihalekayıtno' : response.xpath("normalize-space(//div[@class = 'crazy-box']/div[@class = 'table-div']/div[@class = 'tr'][2]/div[@class = 'td'][1])").get(),
            'nitelikturmıktar' : response.xpath("normalize-space(//div[@class = 'crazy-box']/div[@class = 'table-div']/div[@class = 'tr'][3]/div[@class = 'td'][1])").get(),
            'date' : response.xpath("normalize-space(//div[@class = 'crazy-box']/div[@class = 'table-div']/div[@class = 'tr'][4]/div[@class = 'td'][1])").get(),
            'ihaleplace' : response.xpath("normalize-space(//div[@class = 'crazy-box']/div[@class = 'table-div']/div[@class = 'tr'][5]/div[@class = 'td'][1])").get(),
            'ihaleusulü' : response.xpath("normalize-space(//div[@class = 'crazy-box']/div[@class = 'table-div']/div[@class = 'tr'][6]/div[@class = 'td'][1])").get(),
            'ihaletürü' : response.xpath("normalize-space(//div[@class = 'crazy-box']/div[@class = 'table-div']/div[@class = 'tr'][7]/div[@class = 'td'][1])").get()


        }


        for x in range(2,127):
            
            next_page = "https://www.ilan.gov.tr/kategori-arama?currentPage="+ str(x) + "&npdab=on&type=21628"
            yield scrapy.Request(url=next_page, callback=self.parse)  
