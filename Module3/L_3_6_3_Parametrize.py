import pytest
from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

final = ''

@pytest.fixture(scope="session")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class Test_links:
    urls = ["https://stepik.org/lesson/236895/step/1",
            "https://stepik.org/lesson/236896/step/1",
            "https://stepik.org/lesson/236897/step/1",
            "https://stepik.org/lesson/236898/step/1",
            "https://stepik.org/lesson/236899/step/1",
            "https://stepik.org/lesson/236903/step/1",
            "https://stepik.org/lesson/236904/step/1",
            "https://stepik.org/lesson/236905/step/1",
            ]

    @pytest.mark.parametrize('links', urls)
    def test_all_links(self, browser, links):
        browser.get(links)
        global final
        browser.implicitly_wait(10)
        answer = math.log(int(time.time()))
        textarea = browser.find_element_by_css_selector(".ember-text-area")
        textarea.send_keys(str(answer))
        button = WebDriverWait(browser, 12).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))).click()
        text1 = WebDriverWait(browser, 12).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint"))).text # Находим текст в опциональном фидбеке
        try:
            assert text1 == "Correct!"
        except AssertionError:
            final += text1
            raise AssertionError(final) #Собираем ответ про сов и не пропускаем упавшие тесты
