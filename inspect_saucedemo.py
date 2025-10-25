"""
Inspect the saucedemo page to find the correct selectors for usernames and password.
This script uses Playwright to load the page in headless mode and extract the HTML.
"""
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    page.goto("https://www.saucedemo.com", wait_until="load")
    
    # Wait a bit for any lazy-loaded content
    page.wait_for_timeout(2000)
    
    # Get the full page HTML
    html = page.content()
    
    # Print sections that might contain credentials
    if "accepted" in html.lower():
        print("✓ Found 'accepted' in page (likely usernames section)")
    if "username" in html.lower():
        print("✓ Found 'username' in page")
    if "password" in html.lower():
        print("✓ Found 'password' in page")
    
    # Try to find all text content that looks like usernames
    print("\n=== Looking for visible text content ===")
    
    # Get all text nodes
    text_content = page.evaluate("() => document.body.innerText")
    print(text_content[:2000])  # Print first 2000 chars
    
    print("\n=== Looking for elements with credentials ===")
    
    # Try different selectors
    selectors_to_try = [
        '.login_credentials',
        '.login_password',
        '[class*="credential"]',
        '[class*="password"]',
        'h4',
        'p',
        '.error-message-container',
    ]
    
    for selector in selectors_to_try:
        try:
            elements = page.locator(selector).all()
            if elements:
                print(f"\nSelector '{selector}' found {len(elements)} elements:")
                for elem in elements[:3]:  # Print first 3
                    try:
                        text = elem.inner_text()
                        if text.strip():
                            print(f"  - {text[:100]}")
                    except:
                        pass
        except:
            pass
    
    browser.close()
