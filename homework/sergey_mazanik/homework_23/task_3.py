"""
№ 1
Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select,
выбирает какой-нибудь вариант из Choose language, кликает Submit и проверяет, что в окошке с результатом
отображается тот вариант, который был выбран.

№ 2
Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2, нажмет Start,
и проверит, что на странице появляется текст "Hello World!"
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver


def test_choose_language(driver):
    test_language = 'Python'
    driver.get('https://www.qa-practice.com/elements/select/single_select')
    select = driver.find_element('id', 'id_choose_language')
    dropdown = Select(select)
    dropdown.select_by_visible_text(test_language)
    driver.find_element('id', 'submit-id-submit').click()
    result_text = driver.find_element('id', 'result-text')
    assert result_text.text == test_language, 'Language is not correct'


def test_click_start_button(driver):
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
    start_button = driver.find_element('xpath', '//*[@id="start"]/button')
    start_button.click()
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(('xpath', '//*[@id="finish"]/h4')))
    assert driver.find_element('xpath', '//*[@id="finish"]/h4').text == 'Hello World!'
