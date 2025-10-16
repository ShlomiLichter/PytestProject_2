# PytestProject_2

A Python automation project using Pytest and Playwright for end-to-end and API testing of a sample e-commerce web application.


## Project Structure


```
PytestProject_2/
│
├── conftest.py                # Pytest fixtures and hooks (e.g., screenshot on failure)
├── pytest.ini                 # Pytest configuration
├── LICENSE                    # License file
├── README.md                  # Project documentation
│
├── data/                      # Test data files
│   └── credentials.json       # User credentials for tests
│
├── logs/                      # Log files generated during test runs
│   └── test.log
│
├── screenshots/               # Screenshots captured on test failures
│   └── ...png
│
├── pageObjects/               # Page Object Model and API utilities
│   ├── api_tests/             # API test cases
│   │   ├── test_030_order_api.py
│   │   ├── test_031_countProducts.py
│   │   └── test_032_priceMatch.py
│   ├── utlis/                 # API utility classes
│   │   └── apiBase.py
│   ├── cartPage.py
│   ├── checkout_complete_page.py
│   ├── checkout_step_one_page.py
│   ├── checkout_step_two_page.py
│   ├── inventoryItemPage.py
│   ├── inventoryPage.py
│   ├── loginPage.py
│   └── __init__.py
│
├── test_cart_checkout_swag.py # UI test: cart and checkout flow
├── test_inventory_swag.py     # UI test: inventory and product flow
├── test_login_swag.py         # UI test: login scenarios
└── ...                        # Other test files and cache folders
```

## List of Tests

### test_login_swag.py
- test_T001_loginValid(page)
- test_T002_errorlogin(page)
- test_T003_lockedlogin(page)
- test_T004_passwordlogin(page)
- test_T005_missinglogin(page)
- test_006_logoutflow(page)

### test_inventory_swag.py
- logged_in_page(page)  *(fixture)*
- test_010_inventoryCount(logged_in_page)
- test_011_add_to_cart(logged_in_page)
- test_012_addRemove(logged_in_page)
- test_013_sortPrice(logged_in_page)
- test_014_itemPage(logged_in_page)

### test_cart_checkout_swag.py
- logged_in_page(page)  *(fixture)*
- test_020_inventoryCount(logged_in_page)
- test_021_removeFromCart(logged_in_page)
- test_022_goCheckout(logged_in_page)
- test_023_missingCheckout(logged_in_page)
- test_024_fullFlow(logged_in_page)

### pageObjects/api_tests/test_030_order_api.py
- test_e2e_web_api(playwright)

### pageObjects/api_tests/test_031_countProducts.py
- test_countProducts(playwright)

### pageObjects/api_tests/test_032_priceMatch.py
- *(No test functions found)*

## Key Features
- UI automation with Playwright (Python)
- API testing with requests and Playwright APIRequestContext
- Page Object Model for maintainable test code
- Pytest fixtures for setup/teardown and utilities
- Automatic screenshot capture on test failure
- Logging to file for debugging

## Getting Started
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   playwright install
   ```
2. Configure your test data in `data/credentials.json`.
3. Run tests:
   ```sh
   pytest
   ```

## Author
Shlomi Lichter
