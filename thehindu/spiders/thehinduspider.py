from scrapy.spider import Spider
from scrapy.selector import Selector
from thehindu.items import TheHinduItem

class TheHinduSpider(Spider):
    name = "thehindu"
    allowed_domains = ["thehindu.com"]
    #The Hindu uses a seperate REST service to load the data
    #The web url is "http://www.thehindu.com/archive/web/2014/06/02/"
    start_urls = [
        "http://www.thehindu.com/template/1-0-1/widget/archive/archiveWebDayRest.jsp?d=2014-06-02"
    ]

    def parse(self, response):
        #filename = response.url.split("/")[-2]
        #open(filename, 'wb').write(response.body)
        sel = Selector(response)
        links = sel.xpath("//ul[@class='archiveDayRestList hide']/li/a")
        items = []
        for link in links:
            item = TheHinduItem()
            url = link.xpath("@href").extract()[0]
            title = link.xpath("text()").extract()[0]
            item['url'] = url
            item['title'] = title
            items.append(item)

        return items
