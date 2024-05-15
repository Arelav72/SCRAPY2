import scrapy


class LightscrabingSpider(scrapy.Spider):
    name = "lightscrabing"
    allowed_domains = ["https://www.mirlustr.ru/"]
    start_urls = ["https://www.mirlustr.ru/category/lyustry/"]

    def parse(self, response):
       lustras = response.css('div.products-thumbs__item')

       for lustra in lustras:
           yield {
               'name': lustra.css('div.product-thumb__main a.product-thumb__name::text').get(),
               'price': lustra.css('div.product-thumb__prices span.price::text').get(),
               'image_urls': lustra.css('div.product-thumb__main a.product-thumb__name::attr(href)').get(),

           }

