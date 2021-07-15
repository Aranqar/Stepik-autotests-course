from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.ADD_TO_BASKET), "Add to basket is not presented"  # Проверка что кнопка добавить в
        # корзину присутствует
        add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket.click()

    def prices_should_be_same(self):
        assert self.is_element_present(*ProductPageLocators.CART_PRICE), "Cart price is not presented"
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), "Product price is not presented"
        cart_price = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price in cart_price, f"expected price '{product_price}' not in '{cart_price}'"

    def added_product_names_should_be_same(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), "Product price is not presented"
        assert self.is_element_present(
            *ProductPageLocators.ADDED_TO_CART_PRODUCT_NAME), "Added to cart product name is not presented"
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        added_to_cart_prod_name = self.browser.find_element(*ProductPageLocators.ADDED_TO_CART_PRODUCT_NAME).text
        assert product_name == added_to_cart_prod_name, \
            f"expected name '{product_name}' not as '{added_to_cart_prod_name}'"
