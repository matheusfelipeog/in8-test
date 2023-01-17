from typing import Dict, List, Union

from playwright.sync_api import Page, Locator

from scraper.consts import BASE_URL


def url_products(page: Page, brand: str = 'lenovo') -> List[str]:
    brand = brand.lower()

    cards = page.locator('.thumbnail').all()

    urls = []
    for card in cards:
        title = card.locator('.caption h4 a.title')
        title_text = str(title.text_content())

        if brand in title_text.lower():
            urls.append(title.get_attribute('href'))

    return urls


def product_card(page: Page) -> Locator:
    return page.locator('.thumbnail')


def product_id(page: Page) -> int:
    return int(page.url.split('/')[-1])


def product_name(card: Locator) -> str:
    return str(card.locator('.caption h4').nth(1).text_content())


def product_description(card: Locator) -> str:
    return str(card.locator('.description').text_content())


def product_price(card: Locator) -> float:
    raw_price = card.locator('.caption h4').nth(0).text_content()
    price = str(raw_price).lstrip('$')
    return float(price)


def product_hard_drives_price(
    card: Locator
) -> Dict[str, List[Union[int, float]]]:

    infos = {'prices': [], 'hard_drives': []}
    for hard_drive_size_btn in card.locator('.swatches button').all():
        hard_drive = str(hard_drive_size_btn.text_content())

        infos['hard_drives'].append(int(hard_drive))
        hard_drive_size_btn.click()
        infos['prices'].append(product_price(card))

    return infos


def product_url_image(card: Locator) -> str:
    src = card.locator('.img-responsive').get_attribute('src')
    return BASE_URL + str(src)


def product_reviews(card: Locator) -> int:
    raw_reviews = card.locator('.ratings p').text_content()
    reviews = str(raw_reviews).strip().split()[0]
    return int(reviews)


def product_rating(card: Locator) -> int:
    return card.locator('.ratings p span.glyphicon.glyphicon-star').count()
