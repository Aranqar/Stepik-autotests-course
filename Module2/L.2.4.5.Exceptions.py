from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()

    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/cats.html")

    button = browser.find_element_by_id("button")


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()