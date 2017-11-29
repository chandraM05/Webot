from scrapy.spider import BaseSpider
from tutorial.items import DmozItem
import scrapy

class DmozSpider(BaseSpider):
    name = "dmoz"
    allowed_domains = ["goibibo.com"]
    start_urls = [
        "https://www.goibibo.com/travel-guide/india/destination-pachmarhi/how-to-reach/"
    ]

    #scraps website dmoz for 2 seed URLs, response content written in current directory
    def parse(self, response):
        hxs = scrapy.Selector(response)
        sites = hxs.xpath('//ul/li')
        items = []
        for site in sites:
           item = DmozItem()
           item['title'] = site.select('a/text()').extract()
           item['link'] = site.select('a/@href').extract()
           item['desc'] = site.select('text()').extract()
           items.append(item)
        return items
