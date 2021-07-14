from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
import math

try:
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_id('num1').text
    input2 = browser.find_element_by_id('num2').text
    sum = (int(input1) + int(input2))
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(sum))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(2)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()