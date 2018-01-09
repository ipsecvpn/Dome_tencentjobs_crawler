# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    #爬虫范围
    allowed_domains = ['tencent.com']
    #用来拼接url
    NextNumber = 0
    baseurl = 'http://hr.tencent.com/position.php?&start='
    start_urls = [baseurl+str(NextNumber)]
    #处理response
    def parse(self, response):
        node_list =  response.xpath("//tr[@class='even']|//tr[@class='odd']")
        for node in node_list:
            item = TencentItem()
            #提取职位信息，并将字符串编码
            item['JobTitle'] = node.xpath("//tr[@class='even']/td[1]/a/text()").extract()[0].encode("utf-8")
            item['JobLink'] = node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")
            if len(node.xpath("./td[2]/text()")):
                item['JobType'] = node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
            else:
                item['JobType']=""
            item['Numbers'] = node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
            item['WorkPlace'] = node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
            item['ReleaseTime'] = node.xpath("./td[5]/text()").extract()[0].encode('utf-8')
            #返回数据后继续执行函数
            yield item


        #Response获取需要爬的链接 callback 直到提取完成
        if self.NextNumber < 2190:
            self.NextNumber += 10
            Url = self.baseurl+str(self.NextNumber)
            yield scrapy.Request(Url,callback=self.parse)


