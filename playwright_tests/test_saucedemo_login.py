import pytest
from playwright.sync_api import sync_playwright


def fetch_credentials():
    """Open the saucedemo main page and extract the visible usernames and the password.

    The site lists the accepted usernames in the element with class
    `login_credentials` and the password in the element with class
    `login_password`.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://www.saucedemo.com", wait_until="load")

        creds_text = page.locator('.login_credentials').inner_text()
        usernames = []
        for line in creds_text.splitlines():
            line = line.strip()
            if not line:
                continue
            # Skip heading text
            if any(word in line.lower() for word in ("accepted", "usernames", "are:")):
                continue
            # Any remaining non-empty line is a username
            usernames.append(line)

        password_text = page.locator('.login_password').inner_text()
        # Extract password from text like "Password for all users:\nsecret_sauce"
        password = password_text.split('\n')[-1].strip()
        
        browser.close()
        return usernames, password


def login_and_check(page, username, password):
    print(f"  → Attempting login with username: '{username}'")
    page.fill('#user-name', username)
    page.fill('#password', password)
    page.click('#login-button')

    # Wait for navigation
    page.wait_for_load_state('load')
    
    # successful login goes to /inventory.html
    success = page.url.endswith('/inventory.html')
    if success:
        print(f"    ✅ Login successful for '{username}'")
    else:
        print(f"    ❌ Login failed for '{username}' (URL: {page.url})")
    return success


def test_data_driven_login_all_users():
    users, password = fetch_credentials()
    assert users, "No usernames were scraped from the saucedemo page"

    print(f"\n{'='*60}")
    print(f"Starting Data-Driven Login Test")
    print(f"{'='*60}")
    print(f"Scraped Usernames: {users}")
    print(f"Password: {'*' * len(password)}")
    print(f"{'='*60}\n")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        failures = []
        successes = []
        for user in users:
            print(f"\n[Test {len(successes) + len(failures) + 1}/{len(users)}]")
            page.goto('https://www.saucedemo.com', wait_until='load')
            ok = login_and_check(page, user, password)
            if ok:
                successes.append(user)
            else:
                # locked_out_user is expected to fail as per the test setup
                if user == 'locked_out_user':
                    print(f"    ℹ️  {user} correctly blocked (expected behavior)")
                    successes.append(f"{user} (expected block)")
                else:
                    failures.append(user)

        browser.close()

    print(f"\n{'='*60}")
    print(f"Test Summary")
    print(f"{'='*60}")
    print(f"✅ Successful/Expected: {len([s for s in successes if 'expected' not in s])} + {len([s for s in successes if 'expected' in s])} (expected blocks)")
    print(f"❌ Failed: {len(failures)}")
    print(f"{'='*60}\n")
    
    assert not failures, f"Login failed for users: {failures}"
