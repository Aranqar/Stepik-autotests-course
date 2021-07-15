from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_no_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_IN_BASKET), "Should be no products in basket for guest"

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.BASKET_IS_EMPTY), "Should be message basket is empty for guests"
        empty_basket = self.browser.find_element(*BasketPageLocators.BASKET_IS_EMPTY).text
        assert empty_basket == "Your basket is empty. Continue shopping", \
            f"actual result '{empty_basket}' not Basket is empty"