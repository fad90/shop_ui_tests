from .base_page import BasePage
from .locators import CatalogPageLocators

class CatalogPage(BasePage):
    def go_to_product_page(self):
        product_link = self.browser.find_element(*CatalogPageLocators.FIRST_PRODUCT)
        product_link.click()
