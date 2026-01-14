import allure
from playwright.sync_api import Page
from pages.product_page import ProductPage


def add_items_to_cart(page: Page, urls: list[str]) -> None:
    product = ProductPage(page)

    for index, url in enumerate(urls, start=1):
        product.open(url)
        product.add_to_cart_with_random_variants()

        allure.attach(page.screenshot(), name=f"item_{index}_added_to_cart", attachment_type=allure.attachment_type.PNG)
