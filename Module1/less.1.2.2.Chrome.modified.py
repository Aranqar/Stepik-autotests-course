import time
from selenium import webdriver

driver = webdriver.Chrome()

time.sleep(5)
driver.get('https://stepik.org/lesson/25969/step/12')
time.sleep(10)

submit_button = driver.find_element_by_css_selector('.navbar__auth')
submit_button.click()

s_username = driver.find_element_by_id('id_login_email')
s_username.send_keys('sharvadim@mail.ru')

s_password = driver.find_element_by_id('id_login_password')
s_password.send_keys('vL04mI4KJh&c')

button = driver.find_element_by_css_selector('.sign-form__btn')

button.click()

time.sleep(15)
again = driver.find_element_by_css_selector('.again-btn')
again.click()
time.sleep(5)
textarea = driver.find_element_by_css_selector('.textarea')
textarea.send_keys('get()')
time.sleep(5)
submit_button = driver.find_element_by_css_selector('.submit-submission')
submit_button.click()
time.sleep(5)
driver.quit()
