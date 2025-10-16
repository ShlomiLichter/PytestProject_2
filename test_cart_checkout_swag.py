from playwright.sync_api import Playwright
from pageObjects import inventoryPage
from pageObjects.loginPage import loginPage
from pageObjects.checkout_step_one_page import CheckoutItem

import json
import time
import pytest

with open (r'data/credentials.json') as f:
    login_data = json.load(f)

@pytest.fixture
def logged_in_page(page):
    login_page = loginPage(page)
    login_page.navigate()
    loginValid = login_data['user_credentials'][0]
    user = loginValid['userName']
    password = loginValid['userPassword']
    login_page.valid_login(user,password)
    yield page
    page.close()

def test_020_inventoryCount(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    addItems = inventory_page.add_items_20()
    assert addItems == 4

def test_021_removeFromCart(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    countItems = inventory_page.addAndRemove_21()
    assert countItems == 1

def test_022_goCheckout(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    isCheckout = inventory_page.validateCheckout_22()
    assert isCheckout == "Checkout: Your Information"
    
def test_023_missingCheckout(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    isCheckout = inventory_page.failCheckout_23()
    assert isCheckout == "Error: First Name is required"

def test_024_fullFlow(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    fullCheckout = inventory_page.fullCheckout_24()
    assert fullCheckout == "Thank you for your order!"