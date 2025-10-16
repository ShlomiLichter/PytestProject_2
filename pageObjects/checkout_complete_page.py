import logging
class CheckoutComplete:

    def __init__(self, page):
        self.page = page

    def validate(self):
        title_text = self.page.locator('.complete-header').text_content()
        logging.info(title_text)
        return title_text
