import time

from pages.product_page import ProductPage
import pytest

xfile = 7
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [product_base_link + str(i) for i in range(1) if i != xfile]
xlink = pytest.param(product_base_link + str(xfile), marks=pytest.mark.xfail(reason="Error on page"))
links.insert(xfile, xlink)


# @pytest.mark.parametrize('promo_offers', links)
# def test_guest_can_add_product_to_basket(browser, promo_offers):
#     page = ProductPage(browser, promo_offers)
#     page.open()
#     page.should_not_be_success_message()
#     page.add_product_to_basket()
#     page.solve_quiz_and_get_code()
#     page.prices_should_be_same()
#     page.added_product_names_should_be_same()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.success_message_should_not_dissapeared()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()