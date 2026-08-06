import scrapy


class BookSpider(scrapy.Spider):
    name = "bookspider"
    start_url = "http://books.toscrape.com/catalogue"

    async def start(self):
        # Crawl the first 10 pages
        for page in range(1, 11):
            url = f"{self.start_url}/page-{page}.html"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        # Extract links to individual book pages
        book_links = response.css("article.product_pod h3 a::attr(href)").getall()

        for book_link in book_links:
            yield response.follow(book_link, callback=self.parse_book)

    def parse_book(self, response):
        # Extract book details
        yield {
            "title": response.css("h1::text").get(),
            "price": response.css("p.price_color::text").get(),
        }