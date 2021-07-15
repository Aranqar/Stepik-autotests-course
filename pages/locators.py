from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    ADDED_TO_CART_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) .alertinner")