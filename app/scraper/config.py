from typing import Tuple

from playwright.sync_api import Browser, BrowserContext, Page, Playwright

from app.scraper.consts import BASE_URL


def setup_playwright(
    playwright: Playwright
) -> Tuple[Browser, BrowserContext, Page]:

    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context(base_url=BASE_URL)
    page = context.new_page()

    return (browser, context, page)


def teardown_playwright(
    browser: Browser,
    context: BrowserContext,
    page: Page
) -> None:

    page.close()
    context.close()
    browser.close()
