
import time
import logging

from pageObjects.checkout_step_two_page import CheckoutFinalItem
class CheckoutItem:

    def __init__(self, page):
        self.page = page

    

    def isCheckout(self):
        time.sleep(3)
        title_text = self.page.locator('span.title[data-test="title"]').text_content()
        logging.info(title_text)
        return title_text
    
    def missingData(self):
        time.sleep(3)
        self.page.locator('[data-test="continue"]').click()
        logging.info(self.page.locator('h3[data-test="error"]').text_content())
        return self.page.locator('h3[data-test="error"]').text_content()

    def final(self):
        self.page.get_by_placeholder("First Name").fill("Shlomi")
        self.page.get_by_placeholder("Last Name").fill("Lichter")
        self.page.get_by_placeholder("Zip/Postal Code").fill("70700")
        self.page.locator('[data-test="continue"]').click()
        checkout_two = CheckoutFinalItem.overview(self)
        return checkout_two
        
