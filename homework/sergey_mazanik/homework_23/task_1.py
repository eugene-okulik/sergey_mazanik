"""
Напишите программку, которая заходит на вот эту страницу: https://www.qa-practice.com/elements/input/simple,
вводит какой-то текст в поле, делает submit , а после этого находит элемент, в котором отображается
тот текст, который был введен и рапечатывает этот текст.
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pytest


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    chrome_driver.maximize_window()
    yield chrome_driver


def test_submit_text(driver):
    driver.get('https://www.qa-practice.com/elements/input/simple')
    input_data = 'Text_string'
    text_string_input = driver.find_element('xpath', '//*[@id="id_text_string"]')
    text_string_input.send_keys(input_data)
    text_string_input.send_keys(Keys.ENTER)
    result_text = driver.find_element('xpath', '//*[@id="result-text"]')
    assert result_text.text == input_data, f'{result_text.text} is not {input_data}'
    print(f'Result text is "{result_text.text}"')
