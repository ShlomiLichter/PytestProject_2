import time

from pageObjects.checkout_step_one_page import CheckoutItem
import logging
class Cart:

    def __init__(self, page):
        self.page = page

    def navigateCart(self):
        self.page.goto("https://www.saucedemo.com/cart.html")
    
    def checkItems(self):
        
        count = 0
        if self.page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Bolt T-Shirt").is_visible():
            logging.info("Sauce Labs Bolt T-Shirt is visiable")
            count +=1
        if self.page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Fleece Jacket").is_visible():
            logging.info("Sauce Labs Fleece Jacket is visiable")
            count +=1
        if self.page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Onesie").is_visible():
            logging.info("Sauce Labs Onesie is visiable")
            count +=1
        if self.page.locator('[data-test="inventory-item-name"]', has_text="Bike Light").is_visible():
            logging.info("Bike Light is visiable")
            count +=1
        return count

    def add_and_Remove(self):
       count = 0
       if (
        self.page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Fleece Jacket").is_visible()
        and self.page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Bolt T-Shirt").is_visible()
    ):
           logging.info("Two items are visiable")
           self.page.click('#remove-sauce-labs-fleece-jacket')
           time.sleep(3)
       if self.page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Bolt T-Shirt").is_visible():
           logging.info("One items are visiable")
           count +=1
       return count
           
    def goCheckout(self):
            self.page.click('[data-test="checkout"]')
            checkCheckout = CheckoutItem.isCheckout(self)
            # title_text = self.page.locator('span.title[data-test="title"]').text_content()
            return checkCheckout   

    def failCheckout(self):
            self.page.click('[data-test="checkout"]')
            checkCheckout = CheckoutItem.missingData(self)
            # title_text = self.page.locator('span.title[data-test="title"]').text_content()
            return checkCheckout  

    def passCheckout(self):
         self.page.click('[data-test="checkout"]')
         checkCheckout = CheckoutItem.final(self)
         return checkCheckout

