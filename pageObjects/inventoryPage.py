import time
from pageObjects import cartPage
from pageObjects.inventoryItemPage import InventoryItemPage
from pageObjects.cartPage import Cart

class InventoryPage:

    def __init__(self, page):
        self.page = page

    def is_loaded(self):
        return self.page.locator('span.title[data-test="title"]').is_visible()
    
    def count(self):
        return self.page.locator('.inventory_item').count()
    
    # def inventoryCount(self):
    #     inventory_page = InventoryPage(self.page)
    #     countItems = inventory_page.count()
    #     return countItems

    def basket(self):
        self.page.click('#add-to-cart-sauce-labs-bolt-t-shirt')
        badge_text = self.page.locator('span.shopping_cart_badge[data-test="shopping-cart-badge"]').text_content()
        badge_number = int(badge_text)
        print (badge_number)
        return badge_number
    
    def addAndRemove(self):
        self.page.click('#add-to-cart-sauce-labs-bolt-t-shirt')
        badge = self.page.locator('span.shopping_cart_badge[data-test="shopping-cart-badge"]')
        if badge.count() == 1:
            self.page.click('#remove-sauce-labs-bolt-t-shirt')
        badge = self.page.locator('span.shopping_cart_badge[data-test="shopping-cart-badge"]')
        if badge.count() == 0 or not badge.is_visible():
            return 0
       
    def sortPrice(self):
        self.page.select_option('select[data-test="product-sort-container"]', value="Price (low to high)")
        price_elements = self.page.locator('.inventory_item_price')
        prices = [float(price.replace('$', '')) for price in price_elements.all_text_contents()]
        return prices
        
    def item(self):
        self.page.locator('[data-test="inventory-item-name"]', has_text="Sauce Labs Backpack").click()
        time.sleep(3)
        selectedItem = InventoryItemPage.verifyItem(self)
        return selectedItem
    
    def add_items_20(self):
        self.page.click('#add-to-cart-sauce-labs-bolt-t-shirt')
        self.page.click('#add-to-cart-sauce-labs-onesie')
        self.page.click('#add-to-cart-sauce-labs-fleece-jacket')
        self.page.click('#add-to-cart-sauce-labs-bike-light')
        cart = Cart(self.page)
        cart.navigateCart()
        time.sleep(3)
        itemsInCart = Cart.checkItems(self)
        return itemsInCart

    def addAndRemove_21(self):
        self.page.click('#add-to-cart-sauce-labs-bolt-t-shirt')
        self.page.click('#add-to-cart-sauce-labs-fleece-jacket')
        cart = Cart(self.page)
        cart.navigateCart()
        time.sleep(3)
        finalItems = Cart.add_and_Remove(self)
        return finalItems
        
    def validateCheckout_22(self):
        self.page.click('#add-to-cart-sauce-labs-bolt-t-shirt')
        self.page.click('#add-to-cart-sauce-labs-fleece-jacket')
        self.page.locator('[data-test="shopping-cart-link"]').click()
        cart = Cart(self.page)
        cart.navigateCart()
        isCheckout = Cart.goCheckout(self)
        return isCheckout
    
    def failCheckout_23(self):
        self.page.click('#add-to-cart-sauce-labs-bolt-t-shirt')
        self.page.click('#add-to-cart-sauce-labs-fleece-jacket')
        self.page.locator('[data-test="shopping-cart-link"]').click()
        cart = Cart(self.page)
        cart.navigateCart()
        isCheckout = Cart.failCheckout(self)
        return isCheckout
    
    def fullCheckout_24(self):
        self.page.click('#add-to-cart-sauce-labs-bike-light')
        self.page.click('#add-to-cart-sauce-labs-backpack')
        self.page.locator('[data-test="shopping-cart-link"]').click()
        cart = Cart(self.page)
        cart.navigateCart()
        isCheckout = Cart.passCheckout(self)
        return isCheckout


        
