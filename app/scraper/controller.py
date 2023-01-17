from playwright.sync_api import Page
from playwright.sync_api import sync_playwright

from app.scraper.config import setup_playwright, teardown_playwright
from app.scraper.parser import (
    url_products,
    product_card,
    product_id,
    product_name,
    product_description,
    product_hard_drives_price,
    product_url_image,
    product_reviews,
    product_rating
)
from app.scraper.utils import order_products, Products


def scraper(page: Page) -> Products:

    page.goto('test-sites/e-commerce/allinone/computers/laptops')

    urls = url_products(page)

    products = []
    for url in urls:
        page.goto(url)
        card = product_card(page)

        infos = product_hard_drives_price(card)
        desc = product_description(card)

        products.append({
            'id': product_id(page),
            'name': product_name(card),
            'description': desc,
            'prices': infos['prices'],
            'hard_drives': infos['hard_drives'],
            'url_image': product_url_image(card),
            'reviews': product_reviews(card),
            'rating': product_rating(card),
        })

    products = order_products(products)
    return products


def run() -> Products:
    data = []
    with sync_playwright() as playwright:

        browser, context, page = setup_playwright(playwright)

        data = scraper(page)

        teardown_playwright(browser, context, page)
    return data
