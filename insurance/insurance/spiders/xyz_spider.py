import scrapy
from insurance.items import InsuranceItem

class XyzSpider(scrapy.Spider):
	name = "xyz"
	allowed_domains = ["xyz.cn"]
	start_urls = ["http://www.xyz.cn/mall/yiwaixian/zonghe/","http://www.xyz.cn/mall/yiwaixian/jiaotong/"]

	def parse(self, response):
		sel = scrapy.selector.Selector(response)
		sites = sel.xpath('//div[@class="hazardC_pro_con_main"]')
		items = []
		for site in sites:
			item = InsuranceItem()
			item['title'] = site.xpath('div[@class="hazardC_pro_con_box"]/h3/a[@class="f16 dev_trialSuccess"]/text()').extract()
			item['number'] = site.xpath('div[@class="hazardC_pro_con_box"]/div/span[@class="hazardC_pro_proDucts_num"]/text()').extract()
			item['sale'] = site.xpath('div[@class="hazardC_pro_con_box"]/div/span[@class="hazardC_pro_proDucts_sales"]/text()').extract()
			item['content'] = site.xpath('div[@class="hazardC_pro_con_box"]/div/ul/li/span/text()').extract()
			item['price'] = site.xpath('div[@class="hazardC_pro_con_footer"]/div[@class="hazardC_pro_products_btn"]/span/span/text()').extract()
			items.append(item)

		return items