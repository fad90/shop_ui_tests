from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_product_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_LINK), "Product is presented, but should not be"

    def should_be_empty_basket_message(self):
        empty_text =  self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MASSAGE).text
        assert empty_text == "Ваша корзина пуста Продолжить покупки"