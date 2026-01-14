from playwright.sync_api import Page, Locator


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.ebay.com"

        self.selectors = {
            "search_input": 'input[name="_nkw"]',
        }

        self.search_input: Locator = self.page.locator(self.selectors["search_input"])

    def open(self) -> None:
        self.page.goto(self.base_url)

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_input.press("Enter")
