import scrapy
from insurance.items import InsuranceItem

import sys

class XyzSpider(scrapy.Spider):
	name = "num"
	allowed_domains = ["xyz.cn"]
	start_urls = ["http://www.xyz.cn/mall/yiwaixian/zonghe/","http://www.xyz.cn/mall/yiwaixian/jiaotong/"]

	def parse(self, response):
		sel = scrapy.selector.Selector(response)
		sites = sel.xpath('//li[@class="hazardC_pro_con_item"]')
		items = []
		for site in sites:
			item = InsuranceItem()
			item['number'] = site.xpath('div[@class="hazardC_pro_con_main"]/div[@class="hazardC_pro_con_box"]/div/span[@class="hazardC_pro_proDucts_num"]/text()').extract()
			item['sale'] = site.xpath('div[@class="hazardC_pro_con_main"]/div[@class="hazardC_pro_con_box"]/div/span[@class="hazardC_pro_proDucts_sales"]/text()').extract()
			item['price'] = site.xpath('div[@class="hazardC_pro_con_footer"]/div[@class="hazardC_pro_products_btn"]/span/span/span/text()').extract()
			items.append(item)

		return items

