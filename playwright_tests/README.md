# Playwright tests for saucedemo

**Created using:** Playwright MCP (Model Context Protocol)

This folder contains automated data-driven Playwright tests that:

- Scrape the visible usernames and password from https://www.saucedemo.com
- Attempt to log in with each username using the scraped password
- Display real-time login attempt logs and browser interaction
- Run on Chrome/Chromium in non-headless mode (visible browser window)

Setup & run instructions (Windows / PowerShell)

1) If PowerShell blocks running `npx` due to execution policy, you have several safe options:

- Use the npm wrapper command (recommended, avoids PowerShell script execution):

  ```powershell
  npx.cmd playwright install
  ```

- Or run the installer from cmd.exe (will not trigger PowerShell policy):

  ```powershell
  cmd.exe /c "npx playwright install"
  ```

- Or temporarily bypass PowerShell policy for the current process (less persistent):

  ```powershell
  powershell -ExecutionPolicy Bypass -Command "npx playwright install"
  ```

- If you prefer to permanently allow user-level script execution (requires admin consent):

  ```powershell
  Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force
  npx playwright install
  ```

2) Install Python deps (if not already installed)

   - This test uses Playwright's Python bindings. Install them:

  ```powershell
  pip install playwright pytest
  ```

3) Install Playwright browser binaries (required)

  ```powershell
  npx.cmd playwright install
  ```

4) Run the test

  ```powershell
  pytest -v playwright_tests/test_saucedemo_login.py::test_data_driven_login_all_users -s
  ```

  Or run with less verbose output:

  ```powershell
  pytest -q playwright_tests/test_saucedemo_login.py -k login
  ```

## Test Files

- **`test_saucedemo_login.py`** — Main data-driven test module
  - `fetch_credentials()` — Scrapes usernames and password from the saucedemo main page using CSS selectors
  - `login_and_check()` — Automates login attempt and verifies redirect to inventory page
  - `test_data_driven_login_all_users()` — Pytest test function that iterates through all scraped usernames

## Test Execution Details

When you run the test, you will see:

1. A Chrome browser window opening
2. Real-time console output showing each login attempt:
   - Username being tested
   - ✅ Success indicator with URL confirmation
   - ❌ Failed attempts (if any)
   - ℹ️ Expected blocks (e.g., `locked_out_user`)
3. Test summary with pass/fail results

## Expected Test Results

| Username | Expected Result | Notes |
|----------|-----------------|-------|
| standard_user | ✅ Success | Standard user account |
| locked_out_user | ❌ Blocked | Expected to fail (intentionally locked account) |
| problem_user | ✅ Success | User with UI issues but can log in |
| performance_glitch_user | ✅ Success | User with performance delays |
| error_user | ✅ Success | User that triggers errors in UI |
| visual_user | ✅ Success | User for visual regression testing |

Notes

- The test will scrape usernames and the password that are shown on the saucedemo main page so no separate data file is required.
- Tests run in **non-headless mode** by default (visible browser) for observability. To switch to headless, change `headless=False` to `headless=True` in `test_saucedemo_login.py`.
- Real-time logging shows each login attempt with success/failure indicators and URL verification.
- If you prefer Selenium instead of Playwright, tell me and I can create an alternative implementation.

## Technology Stack

- **Test Framework:** Pytest
- **Automation Tool:** Playwright (Python bindings)
- **Browser:** Chromium (Chrome-compatible)
- **Generation Method:** Playwright MCP (AI-assisted test generation)
