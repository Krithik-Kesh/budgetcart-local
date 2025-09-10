from pathlib import Path

import scrapy

class Grab_Eggs(scrapy.Spider):
    name = "data"

    async def start(self):
        urls = [
            "https://api.pcexpress.ca/pcx-bff/api/v2/products/search",
            "https://cdn.contentful.com/spaces/0dlg9rxz8nvy/environments/master/entries?content_type=pageReact&locale=en-CA&include=10&fields.slug=pdp"
            #second link is not really needed right now but will be for future features
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.json()
        yield {
            "item": data["name"],
            "brand name": data["brand"],
            "price": data["price"]["reg"]
        }#Parsing the data we need (we can just put more stuff later right now im just getting the price and brand name)