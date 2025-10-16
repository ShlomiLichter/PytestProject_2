from playwright.sync_api import Playwright
from pageObjects import inventoryPage
from pageObjects.loginPage import loginPage

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

def test_010_inventoryCount(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    countItems = inventory_page.count()
    assert countItems == 6

def test_011_add_to_cart(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    countBasket = inventory_page.basket()
    assert countBasket == 1

def test_012_addRemove(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    countBasket = inventory_page.addAndRemove()
    assert countBasket == 0

def test_013_sortPrice(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    prices = inventory_page.sortPrice()
    assert prices == sorted(prices)

def test_014_itemPage(logged_in_page):
    inventory_page = inventoryPage.InventoryPage(logged_in_page)
    item = inventory_page.item()
    assert item == 'Sauce Labs Backpack'
    


