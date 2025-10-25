# Data-Driven Login Test for SauceDemo — Summary

## Overview
A successful **data-driven Playwright test** has been created that tests the login functionality for http://www.saucedemo.com using all available usernames scraped from the main page.

## Test Results ✅

**Status:** PASSED

**Test Run Output:**
```
Successful logins: ['standard_user', 'problem_user', 'performance_glitch_user', 'error_user', 'visual_user']
Failed logins: []
locked_out_user correctly blocked (expected behavior)
```

## How It Works

1. **Credential Scraping:** The test dynamically scrapes usernames and password from the saucedemo main page (`.login_credentials` and `.login_password` elements).
2. **Data-Driven Testing:** Each scraped username is used in a separate login attempt using the common password (`secret_sauce`).
3. **Browser:** Tests run on Chrome/Chromium in headless mode via Playwright.
4. **Test Data:**
   - **Usernames extracted:** `standard_user`, `locked_out_user`, `problem_user`, `performance_glitch_user`, `error_user`, `visual_user`
   - **Password extracted:** `secret_sauce`

## Files Created/Modified

- **`playwright_tests/test_saucedemo_login.py`** — Main data-driven test file
  - `fetch_credentials()` — Scrapes usernames and password from the main page
  - `login_and_check()` — Attempts login and verifies success by checking for inventory page redirect
  - `test_data_driven_login_all_users()` — Main pytest test function

- **`playwright_tests/README.md`** — Setup and run instructions with PowerShell fixes

- **`inspect_saucedemo.py`** — Helper script used to debug and find the correct CSS selectors

## Run Instructions

From the project root, run:

```powershell
# Install Playwright browsers (if not already done)
npx.cmd playwright install

# Run the data-driven test
pytest -v playwright_tests/test_saucedemo_login.py::test_data_driven_login_all_users -s
```

## Key Features

✅ **Dynamic Data Extraction:** No hardcoded credentials; test scrapes them from the page  
✅ **Chrome/Chromium:** Uses Playwright with Chromium browser (Chrome-compatible)  
✅ **Data-Driven:** Tests all available user accounts in a single test iteration  
✅ **Smart Handling:** Correctly handles `locked_out_user` which intentionally fails  
✅ **Headless Mode:** Runs without UI, suitable for CI/CD pipelines  
✅ **Pytest Integration:** Integrates with pytest framework for easy reporting and integration

## Expected Test Behavior

| Username | Expected Result | Notes |
|----------|-----------------|-------|
| standard_user | ✅ Login Success | Standard user account |
| locked_out_user | ❌ Login Blocked | Expected to fail (test account is locked) |
| problem_user | ✅ Login Success | User with UI issues (can still log in) |
| performance_glitch_user | ✅ Login Success | User with performance delays |
| error_user | ✅ Login Success | User that triggers errors in UI |
| visual_user | ✅ Login Success | User for visual regression testing |

---

**Test Framework:** Pytest + Playwright  
**Browser:** Chromium (Chrome-compatible)  
**Test Mode:** Headless  
**Date:** October 25, 2025
