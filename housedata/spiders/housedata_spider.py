from scrapy.spiders import SitemapSpider


class HousedataSpider(SitemapSpider):
    custom_settings = {
            'FEED_FORMAT': 'csv',
            'FEED_URI': 'test.csv'
    }
    name = "housedata"
    allowed_domains = ['ikman.lk']
    sitemap_urls = [
        'https://ikman.lk/sitemap-ads1.xml',
        'https://ikman.lk/sitemap-ads2.xml',
        'https://ikman.lk/sitemap-ads3.xml',
        'https://ikman.lk/sitemap-ads4.xml',
        'https://ikman.lk/sitemap-ads5.xml',
        'https://ikman.lk/sitemap-ads6.xml',
        'https://ikman.lk/sitemap-ads7.xml',
        'https://ikman.lk/sitemap-ads8.xml',
        'https://ikman.lk/sitemap-ads9.xml',
        'https://ikman.lk/sitemap-ads10.xml',
        'https://ikman.lk/sitemap-ads11.xml',
        'https://ikman.lk/sitemap-ads12.xml',
        'https://ikman.lk/sitemap-ads13.xml',
        'https://ikman.lk/sitemap-ads14.xml'
    ]
     ## crawls links which does not contain artist. But this outputs some links like submit page etc
    sitemap_rules = [('^(.*house-for-sale).*$', 'parse')]

     # sitemap_follow = ['^((?!artist).)*$']
    def parse(self, response):
       bedrooms = '-'
       bathrooms = '-'
       house_size = '-'
       land_size = '-'
       location = '-'
       price = '-'
       title = '-'
       date_posted = '-'
       entryFound = 0

       div_title = response.xpath("//div[starts-with(@class,'title-container')]")
       title = div_title.xpath('.//div//h1//text()').extract()
       date_posted = div_title.xpath('.//div//span//text()').extract()
       town = div_title.xpath('.//div//span//a//span//text()').extract()
       try:
            title = div_title.xpath('.//div//h1//text()').extract()[0]
       except IndexError:
            title = '-'
       try:
            date_posted = div_title.xpath('.//div//span//text()').extract()[2]
       except IndexError:
            date_posted = '-'
       try:
            town = div_title.xpath('.//div//span//a//span//text()').extract()[0]
       except IndexError:
            town = '-'
       divs_details = response.xpath("//div[starts-with(@class,'ad-meta')]")
       extractedData = divs_details.xpath('.//div/text()').extract()
       try:
           price = response.xpath("//div[starts-with(@class,'amount')]//text()").extract()[0].split("Rs")[1].strip()
           price = float(price.replace(',',''))
       except IndexError:
           price = '-'
       extractedData = divs_details.xpath('.//div/text()').extract()
       if ("Beds: " in extractedData):
            try:
                bedrooms = extractedData[extractedData.index('Beds: ')+1]
                entryFound = 1
            except IndexError:
                bedrooms = '-'
       if ("Baths: " in extractedData):
            try:
                bathrooms = extractedData[extractedData.index('Baths: ')+1]
                entryFound = 1
            except IndexError:
                bathrooms = '-'
       if ("House size: " in extractedData):
            try:
                house_size = extractedData[extractedData.index('House size: ')+1].split(" ")[0]
                house_size = float(house_size.replace(',',''))
                entryFound = 1
            except IndexError:
                house_size = '-'
       if ("Land size: " in extractedData):
            try:
                land_size = extractedData[extractedData.index('Land size: ')+1].split(" ")[0]
                land_size = float(land_size.replace(',',''))
                entryFound = 1
            except IndexError:
                land_size = '-'
       if ("Address: " in extractedData):
            try:
                location = extractedData[extractedData.index('Address: ')+1]
                entryFound = 1
            except IndexError:
                location = '-'
       description_div_details = response.xpath("//div[starts-with(@class,'description-section')]")
       try:
           description_data = description_div_details.xpath('.//div/p').extract()
           description_elements = []
           for element in description_data :
                element = element.replace("<p>", "").replace("</p>", "").strip()
                if (len(element) > 0) :
                    description_elements.append(element)
           if (len(description_elements) == 0) :
                description_elements = '-'
       except IndexError:
           description_elements = '-'
       if (entryFound > 0):
           yield {
                'house_size' : house_size,
                'land_size' : land_size,
                'bedrooms' : bedrooms,
                'bathrooms' : bathrooms,
                'town': town,
                'date_posted': date_posted,
                'title' : title,
                'location' : location,
                'description' : description_elements,
                'price' : price
           }
