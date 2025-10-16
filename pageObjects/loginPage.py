from .inventoryPage import InventoryPage
import time

class loginPage:
    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/")

    def valid_login(self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.get_by_placeholder("Password").fill(userPassword)
        self.page.click('#login-button')
        self.page.locator('span.title[data-test="title"]').is_visible()
        inventoryPage = InventoryPage(self.page)
        if inventoryPage.is_loaded():
            return 
        
    def error_login(self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.get_by_placeholder("Password").fill(userPassword)
        self.page.click('#login-button')
        return self.page.locator('h3[data-test="error"]').text_content()
                
    def locked_login (self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.get_by_placeholder("Password").fill(userPassword)
        self.page.click('#login-button')
        return self.page.locator('h3[data-test="error"]').text_content()
       
    def password_login (self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.get_by_placeholder("Password").fill(userPassword)
        self.page.click('#login-button')
        return self.page.locator('h3[data-test="error"]').text_content()
                
    def missing_login (self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.get_by_placeholder("Password").fill(userPassword)
        self.page.click('#login-button')
        return self.page.locator('h3[data-test="error"]').text_content() 
             
    def logoutflow (self, userName, userPassword):
        self.page.get_by_placeholder("Username").fill(userName)
        self.page.get_by_placeholder("Password").fill(userPassword)
        self.page.click('#login-button')
        self.page.click('#react-burger-menu-btn')
        self.page.click('#logout_sidebar_link')
        return self.page.locator('input[placeholder="Username"]').is_visible()

        


