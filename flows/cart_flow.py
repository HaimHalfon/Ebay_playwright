import allure
from playwright.sync_api import Page
from pages.cart_page import CartPage


def assert_cart_total_not_exceeds(page: Page, budget_per_item: float, items_count: int) -> None:
    cart = CartPage(page)
    cart.open()

    total = cart.get_total_amount()

    allure.attach(page.screenshot(full_page=True), name="cart_summary", attachment_type=allure.attachment_type.PNG)

    assert total <= budget_per_item * items_count, f"Cart total {total} exceeds limit {budget_per_item * items_count}"

    print("#### DONE ####")
