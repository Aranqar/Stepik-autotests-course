from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/file_input.html")
    elements = browser.find_elements_by_css_selector('.form-group input')
    for element in elements:
        element.send_keys("Ho-ho")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, '1.txt')  # добавляем к этому пути имя файла
    attach = browser.find_element_by_css_selector("#file")
    attach.send_keys(file_path)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
