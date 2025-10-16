

from playwright.sync_api import Playwright

from pageObjects.utlis.apiBase import APIUtils

def test_e2e_web_api(playwright:Playwright):

    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order using api

    api_Utils = APIUtils()
    orderId = api_Utils.createOrder(playwright)


    # check order history if exist using  UI
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_placeholder("email@example.com").fill("shlomi@aol.com")
    page.get_by_placeholder("enter your passsword").fill("Shlomi123")
    page.get_by_role("button",name = "Login").click()

    page.get_by_role("button",name = "ORDERS").click()


    # check order history if exist in UI
    row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button",name="View").click()
    assert page.locator(".tagline").text_content() == "Thank you for Shopping With Us"
    context.close
