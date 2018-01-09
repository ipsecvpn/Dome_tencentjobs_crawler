利用Scrapy框架爬腾讯招聘中的职位、类别、地点等信息

思路：
	1.编写item明确提取的数据
	2.编写spiders下爬虫文件，处理请求和以及提取数据 #yield item
	3.编写管道文件，处理spides返回的item数据
	4.启动管道组件，处理相关设置
	5.处理结果返回到tencent.json中
	
	
	
