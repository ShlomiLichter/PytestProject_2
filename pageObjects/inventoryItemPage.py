from playwright.sync_api import expect
import logging

class InventoryItemPage:

    def __init__(self, page):
        self.page = page

    def verifyItem(self):
         logging.info(self.page.locator('.inventory_details_name').text_content())
         return self.page.locator('.inventory_details_name').text_content()



    