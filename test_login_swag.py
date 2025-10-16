import json
import time
from playwright.sync_api import Playwright
import pytest
from pageObjects.loginPage import loginPage
from pageObjects.inventoryPage import InventoryPage

with open (r'data/credentials.json') as f:
    login_data = json.load(f)

#login Page tests

def test_T001_loginValid(page):
    login_page = loginPage(page)
    login_page.navigate()
    loginValid = login_data['user_credentials'][0]
    user = loginValid['userName']
    password = loginValid['userPassword']
    login_page.valid_login(user,password)
    assert InventoryPage is not None

def test_T002_errorlogin(page):
    login_page = loginPage(page)
    login_page.navigate()
    error_login = login_data['user_credentials'][1]
    user = error_login['userName']
    password = error_login['userPassword']
    result = login_page.error_login(user,password)
    assert result == "Epic sadface: Username and password do not match any user in this service"

def test_T003_lockedlogin(page):
    login_page = loginPage(page)
    login_page.navigate()
    locked_login = login_data['user_credentials'][2]
    user = locked_login['userName']
    password = locked_login['userPassword']
    result = login_page.locked_login(user,password)
    assert result == "Epic sadface: Sorry, this user has been locked out."    

def test_T004_passwordlogin(page):
    login_page = loginPage(page)
    login_page.navigate()
    password_login = login_data['user_credentials'][3]
    user = password_login['userName']
    password = password_login['userPassword']
    result = login_page.password_login(user,password)
    assert result == "Epic sadface: Password is required"  

def test_T005_missinglogin(page):
    login_page = loginPage(page)
    login_page.navigate()
    missing_login = login_data['user_credentials'][4]
    user = missing_login['userName']
    password = missing_login['userPassword']
    result = login_page.missing_login(user,password)
    assert result == "Epic sadface: Username is required"  

def test_006_logoutflow(page):
    login_page = loginPage(page)
    login_page.navigate()
    loginValid = login_data['user_credentials'][0]
    user = loginValid['userName']
    password = loginValid['userPassword']
    result = login_page.logoutflow(user,password)
    assert result