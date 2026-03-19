import scrapy
import json
import re


class ProductSpider(scrapy.Spider):
    name = "product"

    start_urls = [
        "https://www2.hm.com/bg_bg/productpage.1274171042.html"
    ]

    def parse(self, response):
        script_tag = response.xpath('//script[contains(., "productArticleDetails")]').get()
        print("First 2000 chars of HTML:")
        print(response.text[:2000])
        if not script_tag:
            self.logger.error("No script tag found containing productArticleDetails")
            return
        print("Script tag found:")
        print(script_tag[:1000])
        

        script_content = response.xpath('//script[contains(., "productArticleDetails")]/text()').get()
        if not script_content:
            self.logger.error("No script content found containing productArticleDetails")
            return
        print("Script content found:")
        print(script_content[:1000])
        match = re.search(r'(\{.*\})', script_content)
        if not match:
            self.logger.error("No JSON found in script content")
            return
        data = json.loads(match.group(1))
        product = data.get("productArticleDetails", {})
        name = product.get("name")
        price = product.get("price", {}).get("value")
        current_color = product.get("colorName")

        available_colors = [
            variant.get("colorName")
            for variant in product.get("variants", [])
            if variant.get("colorName")
        ]

        reviews_count = product.get("whitePrice", {}).get("priceType", 0)
        reviews_score = 0.0  

        yield {
            "name": name,
            "price": price,
            "current_color": current_color,
            "available_colors": list(set(available_colors)),
            "reviews_count": reviews_count,
            "reviews_score": reviews_score,
        }