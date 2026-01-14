from playwright.sync_api import Page
from pages.home_page import HomePage
from pages.search_results_page import SearchResultsPage


def search_items_by_name_under_price(page: Page, query: str, max_price: float, limit: int = 5) -> list[str]:
    home = HomePage(page)
    home.open()
    home.search(query)

    results = SearchResultsPage(page)
    results.filter_max_price(max_price)
    return results.get_item_urls(limit)
