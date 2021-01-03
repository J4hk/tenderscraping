# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class IlanSpider(CrawlSpider):
    name = 'ilan'
    allowed_domains = ['www.ilan.gov.tr']
    start_urls = ['https://www.ilan.gov.tr/kategori-ihale-duyurulari-299012?currentPage=1&field=publish_time&npdMin=04.09.2019&npdMax=04.09.2020&npda=1&npdab=on&cid=299012&type=21628']

    rules = (
        #her ihalenin içine girip verileri çekmek için xpath yolunu bulup linkin içine girmesinin sağlanması
        Rule(LinkExtractor(restrict_xpaths=('//li[@class = "item column col-12"]/div/a')), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        yield{
            #ihale ilanında bulunan bilgilerin xpath yolunun belirlenip get metoduyla alınması
            'İhaleKayıtNumarası' : response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'İKN') or contains(.,'İhale Kayıt Numarası')]/following-sibling::td[2])").get(),
            'Başlık' : response.xpath("normalize-space(//h1)").get(),
            'İhaleUsülü' : response.xpath("normalize-space(//div[@class = 'table-div']/div[@class = 'tr'][contains(. , 'İhale Usulü')]/div[@class = 'td'])").get(),
            'İhaleTürü' : response.xpath("normalize-space(//div[@class = 'table-div']/div[@class = 'tr'][contains(. , 'İhale Türü')]/div[@class = 'td'])").get(),
            'İhaleveTeklifAçmaTarihi' : response.xpath("normalize-space(//div[@class = 'table-div']/div[@class = 'tr'][contains(. , 'İhale ve Teklif')]/div[@class = 'td'])").get(),
            'İdareAdı' : response.xpath("normalize-space(//table[@border ='1']/tbody[1]/tr/td[contains(.,'a) Adı')]/following-sibling::td[2])").get(),
            'İdareninAdresin' : response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'Adre')]/following-sibling::td[2])").get(),
            'İdareninTelefonNumarası' : response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'Telefon')]/following-sibling::td[2])").get(),
            'İdareEmail' : response.xpath("normalize-space(//table[@border ='1']/tbody[1]/tr[1]/td[contains(.,'a) Adı')]/following-sibling::td[2])").get(),
            'İhaleDökümanSayfası' : response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'e-imza')]/following-sibling::td[2])").get(),
            'İhaleKonusuAlımınAdı' : response.xpath("normalize-space(//table[@border ='1']/tbody[1]/tr[1]/td[contains(.,'a) Adı')]/following-sibling::td[2])").get(),
            'NiteliğiTürüMiktarı' : response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'miktarı')]/following-sibling::td[2])").get(),
            'YapılacakYer' :  response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'teslim e')]/following-sibling::td[2])").get(),
            'TeslimTarihi' :  response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'teslim t')]/following-sibling::td[2])").get(),
            'İşeBaşlamaTarihi' : response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'başl')]/following-sibling::td[2])").get(),
            'SonTeklifTarihi' : response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'teklif v')]/following-sibling::td[2])").get(),
            'İhaleKomToplantıYeri' :  response.xpath("normalize-space(//table[@border ='1']/tbody/tr/td[contains(.,'komisyonunu')]/following-sibling::td[2])").get(),
            'BağlıveİlgiliKuruluş' : response.xpath("normalize-space(//div[@class = 'table-div']/div[@class = 'tr'][contains(. , 'Bağlı')]/div[@class = 'td'])").get(),
            'ihalekayııtno' : response.xpath("normalize-space(//div[@class = 'table-div']/div[@class = 'tr'][contains(. , 'İhale Kayı')]/div[@class = 'td'])").get(),


        }

        #pagination
        for x in range(2,1947):
            
            next_page = "https://www.ilan.gov.tr/kategori-arama-299012?currentPage=" +str(x) + "&field=publish_time&npdMin=04.09.2019&npdMax=04.09.2020&npda=1&npdab=on&cid=299012&type=21628"
            yield scrapy.Request(url=next_page, callback=self.parse)  




            