import unittest
from selenium import webdriver
import time

class Testreg(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.get(link)

            # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input.form-control.first[required]")
        input1.send_keys('Ivan')
        input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
        input2.send_keys('Petrov')
        input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
        input3.send_keys("Smolensk")

            # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()



            # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "registration went wrong")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(4)
        browser.get(link)

            # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector("input.form-control.first[required]")
        input1.send_keys('Ivan')
        input2 = browser.find_element_by_css_selector('input.form-control.second[required]')
        input2.send_keys('Petrov')
        input3 = browser.find_element_by_css_selector('input.form-control.third[required]')
        input3.send_keys("Smolensk")

            # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()


            # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                             "registration went wrong")


if __name__ == "__main__":
    unittest.main()