from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_id('treasure')
    Valuex = input1.get_attribute('valuex')
    x = 0
    y = calc(Valuex)
    input2 = browser.find_element_by_id('answer')
    input2.send_keys(y)
    input3 = browser.find_element_by_css_selector('#robotCheckbox')
    input3.click()
    input4 = browser.find_element_by_css_selector('#robotsRule')
    input4.click()

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