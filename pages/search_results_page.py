from playwright.sync_api import Page, Locator


class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page

        self.selectors = {
            "price_inputs": ".price-range input",
            "container": "ul.srp-results",
            "cards": "li.s-card",
            "card_link": "a.s-card__link",
            "next_btn": "a.pagination__next",
        }

        self.price_inputs: Locator = self.page.locator(self.selectors["price_inputs"])
        self.container: Locator = self.page.locator(self.selectors["container"])
        self.cards: Locator = self.container.locator(self.selectors["cards"])
        self.next_btn: Locator = self.page.locator(self.selectors["next_btn"])

    def filter_max_price(self, max_price: float) -> None:
        if self.price_inputs.count() < 2:
            return
        self.price_inputs.nth(1).fill(str(max_price))
        self.price_inputs.nth(1).press("Enter")
        self.page.wait_for_url(f"**_udhi={max_price}**")

    def get_item_urls(self, limit: int = 5) -> list[str]:
        self.container.wait_for()

        urls: list[str] = []

        while True:
            for i in range(self.cards.count()):
                if len(urls) >= limit:
                    break

                href = self.cards.nth(i).locator(self.selectors["card_link"]).first.get_attribute("href")

                if href and href not in urls:
                    urls.append(href)

            if len(urls) >= limit:
                break

            if self.next_btn.count() == 0 or not self.next_btn.first.is_visible():
                break

            self.next_btn.first.click()
            self.container.wait_for()

        return urls
