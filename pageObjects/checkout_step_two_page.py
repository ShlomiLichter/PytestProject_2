import time
import logging

from pageObjects.checkout_complete_page import CheckoutComplete
class CheckoutFinalItem:

    def __init__(self, page):
        self.page = page

    def overview(self):
        self.page.locator('[data-test="finish"]').click()
        finish = CheckoutComplete.validate(self)
        return finish
