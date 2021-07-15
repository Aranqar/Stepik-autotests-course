from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    CART_PRICE = (By.CSS_SELECTOR, "div.basket-mini")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main .price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main h1")
    ADDED_TO_CART_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages div:nth-child(1) strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    LOOK_IN_BASKET = (By.CSS_SELECTOR, "span a.btn-default")

class BasketPageLocators:
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket-items .row")
    BASKET_IS_EMPTY = (By.CSS_SELECTOR, "#content_inner p")
