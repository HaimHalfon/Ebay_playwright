# Ebay Playwright Automation Project

## Overview

This project demonstrates an end-to-end (E2E) automation flow on the eBay website using Playwright with Python.
The scenario includes searching products, filtering by price, adding items to the cart, and validating the cart total.

The project is built using:

- Playwright (Python)
- Pytest
- Page Object Model (POM)
- Data-Driven approach
- Allure Reports for test reporting

---

## Prerequisites

Before running the project, make sure you have:

- Python 3.10 or higher
- Google Chrome / Chromium installed
- Allure CLI installed
- Internet connection

---

## How to Run Locally

```bash
# 1) Clone the repository
git clone https://github.com/HaimHalfon/Ebay_playwright.git

# 2) Navigate into the project folder
cd Ebay_playwright

# 3) Install requirements
pip install -r requirements.txt

# 4) Install Playwright browsers
playwright install

# 5) Run tests and generate Allure results
pytest --alluredir=allure-results

# 6) Open the Allure report
allure serve allure-results
```

---

## Test Data (Data-Driven)

Test inputs are configured in:

- data/test_data.json

You can change values like:

- query
- max_price
- limit

---

## Architecture

The project follows the Page Object Model (POM) pattern:

- `pages/`
  Contains page classes (HomePage, ProductPage, CartPage)
  Each class is responsible for a single page and its actions.

- `tests/`
  Contains test scenarios written with pytest.

- `utils/`
  Shared helpers such as data loading and parsing.

- `data/`
  External test data files (JSON).

This structure improves readability, maintainability, and scalability.

---

## Assumptions and Limitations

- No user login is performed (Guest checkout only).
- Prices are validated based on the displayed currency on the site.
- Product availability and prices may change over time.
- The test assumes standard eBay UI.

---

## Notes

- Screenshots and reports are generated during runtime and are excluded from version control.
- All screenshots are attached directly to the Allure report.
