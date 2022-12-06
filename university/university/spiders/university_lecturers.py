import scrapy
from ..items import UniversityItem



class UniversityLecturersSpider(scrapy.Spider):
    name = 'university_lecturers'
    start_urls = ['https://www.runi.ac.il/en/about/management/']

    def parse(self,response):

        items=UniversityItem()
        lecturers=response.xpath('//div[@role="rowgroup"]/li/text()').extract()


        #for lecturer in lecturers:
        name=response.css('div.name::text').extract()
        job=response.xpath('//div[@class="info"]/p/text()').extract()
       
        items['name']=name #nsrkjgnjksenjv#
        items['job']=job
        yield items
