import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import CarifermoItem
from itemloaders.processors import TakeFirst


class CarifermoSpider(scrapy.Spider):
	name = 'carifermo'
	start_urls = ['https://www.carifermo.it/it/1602/d/0/']

	def parse(self, response):
		post_links = response.xpath('//a[@class="titolocf"]/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

		next_page = response.xpath('//a[@id="nextPag"]/@href').getall()
		yield from response.follow_all(next_page, self.parse)


	def parse_post(self, response):
		title = response.xpath('//div[@class="titolo"]/text()').get()
		description = response.xpath('//div[@class="NewsViewer"]//text()[normalize-space() and not(ancestor::div[@class="titolo"] | ancestor::div[@class="infoNotizia"])]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@class="news_dataPub"]/text()').get()

		item = ItemLoader(item=CarifermoItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
