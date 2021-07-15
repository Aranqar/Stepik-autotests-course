from pages.product_page import ProductPage
import pytest

xfile = 7
product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
links = [product_base_link + str(i) for i in range(10) if i != xfile]
xlink = pytest.param(product_base_link + str(xfile), marks=pytest.mark.xfail(reason="Error on page"))
links.insert(xfile, xlink)


@pytest.mark.parametrize('promo_offers', links)
def test_guest_can_add_product_to_basket(browser, promo_offers):
    page = ProductPage(browser, promo_offers)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.prices_should_be_same()
    page.added_product_names_should_be_same()
