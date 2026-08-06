import scrapy
from pydantic import BaseModel
from scrapy_spider_metadata import Args


class MyParams(BaseModel):
    pages: int


class BookSpider(Args[MyParams], scrapy.Spider):
    name = "bookspider"
    start_urls = ["http://books.toscrape.com/catalogue"]

    async def start(self):
        for start_url in self.start_urls:
            for index in range(1, self.args.pages + 1):
                yield scrapy.Request(f"{start_url}/page-{index}.html")

    def parse(self, response):
        book_links = response.css("article.product_pod h3 a::attr(href)").getall()
        for book_link in book_links:
            yield response.follow(book_link, self.parse_book)

    def parse_book(self, response):
        yield {
            "title": response.css("h1::text").get(),
            "price": response.css("p.price_color::text").get(),
        }