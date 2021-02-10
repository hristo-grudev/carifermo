BOT_NAME = 'carifermo'

SPIDER_MODULES = ['carifermo.spiders']
NEWSPIDER_MODULE = 'carifermo.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'carifermo.pipelines.CarifermoPipeline': 100,

}