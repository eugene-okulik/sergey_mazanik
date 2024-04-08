"""
Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form и полностью заполнит
 форму (кроме загрузки файла) и нажмет Submit.

Небольшая особенность
Страничка эта немного кривая, иногда реклама перекрывает элементы и по ним невозможно кликнуть
(но сейчас, смотрю, вообще реклама пропала). Если бы это было приложение, которое мы тестируем, это был бы баг.
Но работаем с тем, что есть. И для нас это даже плюс, нужно найти как выкрутиться. Обойти это можно уменьшив
размер экрана браузера - тогда элементы перераспределяются и становятся доступны. Но если реклама так и не
появится, то ничего на странице не мешает.

После отправки вам будет отображено окошко с тем что вы ввели. Получите со страницы содержимое этого окошка и
распечатайте (выведите на экран).
"""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest
from faker import Faker
from random import randint


ADVERTISE_FROM_HEADER = (
    'xpath',
    '//*[@id="google_ads_iframe_/21849154601,22343295815/Ad.Plus-970x250-1_0__container__"]'
)
FIRST_NAME_INPUT = ('xpath', '//*[@id="firstName"]')
LAST_NAME_INPUT = ('xpath', '//*[@id="lastName"]')
EMAIL_INPUT = ('xpath', '//*[@id="userEmail"]')
GENDER_MALE_RADIOBUTTON = ('xpath', '//*[@for="gender-radio-1"]')
GENDER_FEMALE_RADIOBUTTON = ('xpath', '//*[@for="gender-radio-2"]')
GENDER_OTHER_RADIOBUTTON = ('xpath', '//*[@for="gender-radio-3"]')
MOBILE_NUMBER = ('xpath', '//*[@id="userNumber"]')
DATE_OF_BIRTH_INPUT = ('xpath', '//*[@id="dateOfBirthInput"]')
SUBJECTS_INPUT = ('xpath', '//*[@id="subjectsInput"]')
HOBBIES_SPORT_CHECKBOX = ('xpath', '//*[@for="hobbies-checkbox-1"]')
HOBBIES_READING_CHECKBOX = ('xpath', '//*[@for="hobbies-checkbox-2"]')
HOBBIES_MUSIC_CHECKBOX = ('xpath', '//*[@for="hobbies-checkbox-3"]')
CURRENT_ADDRESS_TEXTAREA = ('xpath', '//*[@id="currentAddress"]')
STATE_SELECT = ('xpath', '//*[@id="state"]')
STATE_SELECT_OPTION = ('xpath', '//*[@id="react-select-3-option-0"]')
CITY_SELECT = ('xpath', '//*[@id="city"]')
CITY_SELECT_OPTION = ('xpath', '//*[@id="react-select-4-option-0"]')
SUBMIT_BUTTON = ('xpath', '//*[@id="submit"]')
RESULT_LIST = ('xpath', '//tbody/tr')

test_first_name, test_last_name = Faker().name().split()
test_email = Faker().email()
test_mobile_number = str(randint(1000000000, 9999999999))
test_subject = 'Maths'
test_address = Faker().address()


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    chrome_driver = webdriver.Chrome(options=options)
    yield chrome_driver


def test_fill_form(driver):
    driver.get('https://demoqa.com/automation-practice-form')
    wait = WebDriverWait(driver, 5)
    wait.until(EC.visibility_of_element_located(ADVERTISE_FROM_HEADER))

    driver.execute_script('window.scrollTo(0, 500)')

    first_name_input = driver.find_element(*FIRST_NAME_INPUT)
    first_name_input.send_keys(test_first_name)
    last_name_input = driver.find_element(*LAST_NAME_INPUT)
    last_name_input.send_keys(test_last_name)
    email_input = driver.find_element(*EMAIL_INPUT)
    email_input.send_keys(test_email)
    gender_male_radio = driver.find_element(*GENDER_MALE_RADIOBUTTON)
    gender_male_radio.click()
    mobile_number = driver.find_element(*MOBILE_NUMBER)
    mobile_number.send_keys(test_mobile_number)
    subjects_input = driver.find_element(*SUBJECTS_INPUT)
    subjects_input.send_keys(test_subject)
    subjects_input.send_keys(Keys.ENTER)
    hobby_sport_checkbox = driver.find_element(*HOBBIES_SPORT_CHECKBOX)
    hobby_sport_checkbox.click()
    hobby_music_checkbox = driver.find_element(*HOBBIES_MUSIC_CHECKBOX)
    hobby_music_checkbox.click()
    current_address_textarea = driver.find_element(*CURRENT_ADDRESS_TEXTAREA)
    current_address_textarea.send_keys(test_address)
    state_select = driver.find_element(*STATE_SELECT)
    state_select.click()
    state_select_option = driver.find_element(*STATE_SELECT_OPTION)
    state_select_option.click()
    city_select = driver.find_element(*CITY_SELECT)
    city_select.click()
    city_select_option = driver.find_element(*CITY_SELECT_OPTION)
    city_select_option.click()
    submit_button = driver.find_element(*SUBMIT_BUTTON)
    submit_button.click()

    result_list = driver.find_elements(*RESULT_LIST)
    for result in result_list:
        print(result.text)
