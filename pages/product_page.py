from playwright.sync_api import Page, Locator
import random


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        self.selectors = {
            "add_to_cart_button": "#atcBtn_btn_1",
            "options_container": 'div[data-testid="x-msku-evo"]',
            "option_groups": "div.x-sku",
            "open_options_button": "button.listbox-button__control",
            "clickable_option": 'div[role="option"][data-sku-value-name]:not([aria-disabled="true"])',
            "added_success": '.lightbox-dialog__window span.ux-textspans:has-text("Added to cart")',
        }

        self.add_to_cart_button: Locator = self.page.locator(self.selectors["add_to_cart_button"])
        self.options_container: Locator = self.page.locator(self.selectors["options_container"])
        self.option_groups: Locator = self.options_container.locator(self.selectors["option_groups"])
        self.added_success: Locator = self.page.locator(self.selectors["added_success"])

    def open(self, url: str) -> None:
        self.page.goto(url)

    def _select_variants(self) -> None:
        if self.options_container.count() == 0:
            return

        self.option_groups.first.wait_for()

        for group_index in range(self.option_groups.count()):
            group = self.option_groups.nth(group_index)

            group.locator(self.selectors["open_options_button"]).first.click()

            available_options = group.locator(self.selectors["clickable_option"])
            available_count = available_options.count()

            if available_count == 0:
                raise RuntimeError("Unable to select a variant")

            rnd_index = random.randrange(available_count)
            available_options.nth(rnd_index).click()

    def add_to_cart_with_random_variants(self) -> None:
        self._select_variants()
        self.add_to_cart_button.click()
        self.added_success.wait_for()

    def take_screenshot(self, path: str) -> None:
        self.page.screenshot(path=path)
