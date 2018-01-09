# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class TencentPipeline(object):
    #创建json文件
    def __init__(self):
        self.f = open("tencent.json","w")
    #把数据转为字符串  -->python字典-->json
    def process_item(self, item, spider):
        content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
        #写入数据
        self.f.write(content)
        return item
    #关闭
    def close_spider(self,spider):
        self.f.close()