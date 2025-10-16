
from playwright.sync_api import Playwright

from pageObjects.utlis.apiBase import APIUtils

def test_countProducts(playwright:Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Get product count from API

    api_Utils = APIUtils()
    countAPI = api_Utils.getProductCount(playwright)


    # Get product count from UI

    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("shlomi@aol.com")
    page.get_by_placeholder("enter your passsword").fill("Shlomi123")
    page.get_by_role("button",name = "Login").click()

    import re

    # Find the element by id
    text = page.locator('#res').text_content()

    # Extract the number using regex
    match = re.search(r'Showing (\d+) results', text)
    if match:
        number = int(match.group(1))
        print(number)  # Output: 3

    assert number == countAPI