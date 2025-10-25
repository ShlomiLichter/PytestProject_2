"""
End-to-End Test for SauceDemo E-Commerce Checkout Flow
Created using Playwright MCP

Test Flow:
1. Login with standard_user / secret_sauce
2. Add "Sauce Labs Backpack" to cart
3. Navigate to cart and verify product exists
4. Click Checkout
5. Fill checkout form:
   - First Name: Shlomi
   - Last Name: Lichter
   - Zip/Postal Code: 70700
6. Click Continue
7. Verify "Sauce Labs Backpack" exists on checkout step two
8. Click Finish
9. Validate "Thank you for your order!" message on completion page
"""

import pytest
from playwright.sync_api import sync_playwright, Page


@pytest.fixture
def browser():
    """Fixture to launch and manage Playwright browser."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        yield browser
        browser.close()


@pytest.fixture
def page(browser):
    """Fixture to create a new page for each test."""
    page = browser.new_page()
    yield page
    page.close()


def test_e2e_checkout_flow(page: Page):
    """Complete end-to-end test of the SauceDemo checkout flow."""
    
    print("\n" + "="*70)
    print("E2E TEST: SauceDemo Checkout Flow")
    print("="*70)
    
    # Step 1: Navigate to login page
    print("\n[Step 1] Navigating to SauceDemo login page...")
    page.goto("https://www.saucedemo.com", wait_until="load")
    
    # Step 2: Login with standard_user
    print("[Step 2] Logging in with standard_user / secret_sauce...")
    page.fill('#user-name', 'standard_user')
    page.fill('#password', 'secret_sauce')
    page.click('#login-button')
    page.wait_for_load_state('load')
    
    # Verify we're on inventory page
    assert 'inventory' in page.url, f"Expected inventory page, got: {page.url}"
    print("✅ Login successful - on inventory page")
    
    # Step 3: Add "Sauce Labs Backpack" to cart
    print("\n[Step 3] Adding 'Sauce Labs Backpack' to cart...")
    # Find the backpack product and click "Add to cart"
    backpack_button = page.locator('button:has-text("Add to cart")').first
    # More specific: find the button associated with the backpack
    page.click('button[id="add-to-cart-sauce-labs-backpack"]')
    print("✅ Product added to cart")
    
    # Step 4: Navigate to cart
    print("\n[Step 4] Navigating to shopping cart...")
    page.click('a.shopping_cart_link')
    page.wait_for_load_state('load')
    
    # Verify we're on cart page
    assert 'cart' in page.url, f"Expected cart page, got: {page.url}"
    print("✅ On cart page")
    
    # Step 5: Verify "Sauce Labs Backpack" exists in cart
    print("[Step 5] Verifying 'Sauce Labs Backpack' exists in cart...")
    backpack_in_cart = page.locator('text=Sauce Labs Backpack')
    assert backpack_in_cart.is_visible(), "Sauce Labs Backpack not found in cart"
    print("✅ 'Sauce Labs Backpack' found in cart")
    
    # Step 6: Click Checkout
    print("\n[Step 6] Clicking 'Checkout' button...")
    page.click('button:has-text("Checkout")')
    page.wait_for_load_state('load')
    
    # Verify we're on checkout step one
    assert 'checkout-step-one' in page.url, f"Expected checkout-step-one page, got: {page.url}"
    print("✅ On checkout step one page")
    
    # Step 7: Fill checkout form
    print("\n[Step 7] Filling checkout form...")
    print("  - First Name: Shlomi")
    page.fill('#first-name', 'Shlomi')
    
    print("  - Last Name: Lichter")
    page.fill('#last-name', 'Lichter')
    
    print("  - Zip/Postal Code: 70700")
    page.fill('#postal-code', '70700')
    print("✅ Checkout form filled")
    
    # Step 8: Click Continue
    print("\n[Step 8] Clicking 'Continue' button...")
    page.click('input[value="Continue"]')
    page.wait_for_load_state('load')
    
    # Verify we're on checkout step two
    assert 'checkout-step-two' in page.url, f"Expected checkout-step-two page, got: {page.url}"
    print("✅ On checkout step two page")
    
    # Step 9: Verify "Sauce Labs Backpack" exists on checkout step two
    print("\n[Step 9] Verifying 'Sauce Labs Backpack' exists on checkout step two...")
    backpack_in_checkout = page.locator('text=Sauce Labs Backpack')
    assert backpack_in_checkout.is_visible(), "Sauce Labs Backpack not found on checkout step two"
    print("✅ 'Sauce Labs Backpack' found on checkout step two")
    
    # Step 10: Click Finish
    print("\n[Step 10] Clicking 'Finish' button...")
    page.click('button:has-text("Finish")')
    page.wait_for_load_state('load')
    
    # Verify we're on checkout complete page
    assert 'checkout-complete' in page.url, f"Expected checkout-complete page, got: {page.url}"
    print("✅ On checkout complete page")
    
    # Step 11: Validate thank you message
    print("\n[Step 11] Validating completion message...")
    # The message contains "Thank you for your order!"
    thank_you_message = page.locator('text=/Thank you.*/i')
    assert thank_you_message.is_visible(), "Thank you message not found on completion page"
    
    # Get the exact message text
    message_text = thank_you_message.inner_text()
    print(f"✅ Message found: '{message_text}'")
    
    # Print completion summary
    print("\n" + "="*70)
    print("✅ E2E TEST COMPLETED SUCCESSFULLY")
    print("="*70)
    print("\nTest Summary:")
    print("  ✅ Successfully logged in with standard_user")
    print("  ✅ Added 'Sauce Labs Backpack' to cart")
    print("  ✅ Verified product in cart")
    print("  ✅ Completed checkout with personal info")
    print("  ✅ Verified product on checkout review")
    print(f"  ✅ Confirmed order with message: '{message_text}'")
    print("="*70 + "\n")


if __name__ == "__main__":
    # Run the test directly
    pytest.main([__file__, "-v", "-s"])
