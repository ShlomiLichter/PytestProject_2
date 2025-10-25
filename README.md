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

## Playwright MCP Generated Tests

### playwright_tests/test_saucedemo_login.py
Data-driven login test for https://www.saucedemo.com created using **Playwright MCP** (Model Context Protocol):

- **test_data_driven_login_all_users()** — Tests all available user accounts by:
  - Dynamically scraping usernames and password from the saucedemo main page
  - Attempting login for each username
  - Verifying successful redirect to inventory page
  - Handling expected failures (e.g., `locked_out_user` is intentionally locked)

**Test Results:** 5 successful logins + 1 expected block = ✅ PASSED

**Features:**
- Real-time browser visualization (non-headless mode)
- Detailed console logging showing each login attempt
- Automatic credential extraction from the application
- No hardcoded test data required

For details, see `playwright_tests/README.md`

### test_e2e_saucedemo_checkout.py
Complete end-to-end checkout flow test for SauceDemo created using **Playwright MCP**:

- **test_e2e_checkout_flow()** — Full e-commerce transaction test including:
  - Login with `standard_user` / `secret_sauce`
  - Add "Sauce Labs Backpack" to cart
  - Verify product in cart
  - Complete checkout with personal information (Shlomi Lichter, Zip: 70700)
  - Verify product on checkout review page
  - Confirm order completion with "Thank you for your order!" message

**Test Results:** ✅ PASSED in 15.29 seconds

**Features:**
- Complete user journey from login to order confirmation
- Step-by-step console logging with visual indicators (✅/❌)
- URL verification at each checkpoint
- Element visibility validation
- pytest fixtures for browser management

Run with:
```sh
pytest test_e2e_saucedemo_checkout.py -v -s
```

For details, see `E2E_CHECKOUT_TEST_SUMMARY.md`

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
   pytest -v --html=report.html
   ```

## Author
Shlomi Lichter
