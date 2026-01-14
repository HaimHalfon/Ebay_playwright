from playwright.sync_api import Page, Locator
import re


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_url = "https://cart.ebay.com/"

        self.selectors = {
            "subtotal": '[data-test-id="SUBTOTAL"]',
        }

        self.subtotal: Locator = self.page.locator(self.selectors["subtotal"])

    def open(self) -> None:
        self.page.goto(self.cart_url)

    def get_total_amount(self) -> float:
        self.subtotal.wait_for()

        subtotal_text = self.subtotal.inner_text()
        match = re.search(r"[\d,.]+", subtotal_text)

        return float(match.group(0).replace(",", ""))

    def take_screenshot(self, path: str) -> None:
        self.page.screenshot(path=path)
