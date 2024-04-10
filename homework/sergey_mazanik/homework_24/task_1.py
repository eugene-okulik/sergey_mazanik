"""
https://www.demoblaze.com/index.html
1. Откройте товар в новой вкладке
2. Перейдите на вкладку с товаром
3. Добавьте товар в корзину
4. Закройте вкладку с товаром
5. На начальной вкладке откройте корзину
6. Убедитесь, что в корзине тот товар, который вы добавляли
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
import pytest


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver


def test_add_to_cart(driver):
    wait = WebDriverWait(driver, 5)
    driver.get('https://www.demoblaze.com/index.html')
    wait.until(EC.presence_of_all_elements_located(('class name', 'hrefch')))
    products_list = driver.find_elements('class name', 'hrefch')
    product_name = products_list[0].text
    actions = ActionChains(driver)
    actions.key_down(Keys.COMMAND).click(products_list[0]).key_up(Keys.COMMAND).perform()
    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])
    wait.until(EC.element_to_be_clickable(('class name', 'btn-success')))
    add_to_cart_button = driver.find_element('class name', 'btn-success')
    add_to_cart_button.click()
    wait.until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()
    driver.close()
    driver.switch_to.window(tabs[0])
    go_to_cart_button = driver.find_element('id', 'cartur')
    go_to_cart_button.click()
    wait.until(EC.presence_of_all_elements_located(('class name', 'success')))
    cart_list = driver.find_elements('class name', 'success')
    assert len(cart_list) == 1, 'More than one item in cart'
    assert product_name in cart_list[0].text, 'Wrong product in cart'
