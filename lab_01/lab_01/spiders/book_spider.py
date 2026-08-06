import scrapy


class BookSpider(scrapy.Spider):
    name = "bookspider"

    start_url = "http://books.toscrape.com/catalogue"

    async def start(self):
        # Crawl first 10 pages
        for page in range(1, 11):
            url = f"{self.start_url}/page-{page}.html"
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        #links to all books on the page
        book_links = response.css("article.product_pod h3 a::attr(href)").getall()

        for link in book_links:
            yield response.follow(link, callback=self.parse_book)

    def parse_book(self, response):

        rating = response.css("p.star-rating::attr(class)").get("").split()[-1]

        availability = response.xpath(
            'normalize-space(//p[contains(@class, "availability")])'
        ).get()

        yield {
            "title": response.css("h1::text").get(),

            "category": response.css(
                "ul.breadcrumb li:nth-child(3) a::text"
            ).get(),

            "price": response.css("p.price_color::text").get(),

            "rating": rating,

            "availability": availability,

            "product_description": response.css(
                "#product_description + p::text"
            ).get(default=""),

            "upc": response.xpath(
                '//th[text()="UPC"]/following-sibling::td/text()'
            ).get(),

            "number_of_reviews": response.xpath(
                '//th[text()="Number of reviews"]/following-sibling::td/text()'
            ).get(),

            "product_url": response.url,
        }