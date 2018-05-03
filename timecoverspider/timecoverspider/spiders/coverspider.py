# import the necessary packages
from timecoverspider.items import MagazineCover
from datetime import datetime
import scrapy

class CoverSpider(scrapy.Spider):
	name = "time_spider"
	start_urls = ["http://content.time.com/time/covers/0,16641,19230303,00.html"]


	def parse(self, response):
		# loop over all cover link elements that link off to the large
		# cover of the magazine and yield a request to grab the cove
		# data and image
		#for href in response.xpath("//a[contains(@href, 'View Large Cover')]"):


#yield scrapy.Request(brickset.xpath('//article[@class="art-cover-photo"]//img/@src').extract_first(),
#				self.parse_covers)

		SET_SELECTOR = '.art-cover-photo'
		for brickset in response.css(SET_SELECTOR):
			
			img = brickset.xpath('//article[@class="art-cover-photo"]//img/@src')
			#yield {
			#	'title': brickset.xpath('//article[@class="art-cover-photo"]//img/@src'),			
			#}
			imageURL = img.extract_first()

			# grab the title and publication date of the current issue
			title = response.css(".content-main-aside h1::text").extract_first()
			year = response.css(".content-main-aside h1 time a::text").extract_first()
			month = response.css(".content-main-aside h1 time::text").extract_first()[:-2]
			
			# parse the date
			date = "{} {}".format(month, year).replace(".", "")
				
			DATE_FORMATS = ['%b %d %Y','%B %d %Y']
			test_date = 'June 4 1923'

			for date_format in DATE_FORMATS:
			    try:
				d = datetime.strptime(date, date_format)
			    except ValueError:
				pass
			    else:
			      break
			else:
			  d = None

			#print d # 2012-01-01 12:32:11
			#print type(d) # <type 'datetime.datetime'>			
			

			print("File Downloadeddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd",imageURL)
			pub = "{}-{}-{}".format(d.year, str(d.month).zfill(2), str(d.day).zfill(2))
				   # yield the result
		        yield MagazineCover(title=title, pubDate=pub, file_urls=[imageURL])
			
						
			
		# extract the 'Next' link from the pagination, load it, and
		# parse it
		NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
	    	next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
	    	if next_page:
			yield scrapy.Request(
			    response.urljoin(next_page),
			    callback=self.parse
			)

	#def parse_covers(self, response):


			#for fmt in ('%b %d %Y', '%B %d %Y'):
			#	try:
				   
				  
			#	except ValueError:
			#	    pass
			#       raise ValueError('no valid date format found')

			#print("Hhehehehehehehehehhehehehehehehehehehhehehheheheehhehehehehehehehhehehhehehehehehe",date)
				







	










#	def parse_page(self, response):	 
#	 for content in response.css('ul.ul-showcase-related'):
#	    	yield scrapy.Request(href.content.css('li a::attr("href")').extract_first(),self.parse_covers)
#
#	 next = response.css('span.next a::attr("href")')
#	 yield scrapy.Request(next.xpath("@href").extract_first(),self.parse_page)
#
	
		 
	 




				


