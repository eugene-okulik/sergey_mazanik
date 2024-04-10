"""
https://magento.softwaretestingboard.com/gear/bags.html Навести мышку на первый товар -> кликнуть внизу карточки
товара на кнопку Add to compare -> Проверить, что товар появился слева на этой же странице в секции Compare Products
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver


def test_compare_product(driver):
    wait = WebDriverWait(driver, 5)
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')
    actions = ActionChains(driver)
    products_list = driver.find_elements('class name', 'product-item-info')
    product_name = products_list[0].text.split('\n')[0]
    actions.move_to_element(products_list[0])
    add_to_compare_button = driver.find_element('xpath', '//*[@title="Add to Compare"]')
    actions.click(add_to_compare_button)
    actions.perform()
    wait.until(EC.presence_of_element_located(('class name', 'odd')))
    compare_product = driver.find_element('class name', 'odd').text.split('\n')[0]
    assert product_name == compare_product, 'Wrong product added to compare'
