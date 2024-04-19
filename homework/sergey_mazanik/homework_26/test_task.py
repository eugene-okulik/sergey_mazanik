from playwright.sync_api import Page, expect
from faker import Faker
from random import randint
from time import sleep


test_first_name, test_last_name = Faker().name().split()
test_email = Faker().email()
test_mobile_number = str(randint(1000000000, 9999999999))
test_subject = 'Maths'
test_address = Faker().address()


def test_first_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_text('Form Authentication').click()
    page.get_by_label('Username').fill('test')
    page.get_by_label('Password').fill('test')
    page.get_by_role('button').click()


def test_second_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')
    page.get_by_placeholder('First name').fill(test_first_name)
    page.get_by_placeholder('Last name').fill(test_last_name)
    page.locator('#userEmail').fill(test_email)
    page.locator('//*[@for="gender-radio-1"]').check()
    page.get_by_placeholder('Mobile Number').fill(test_mobile_number)
    subjects_input = page.locator('#subjectsInput')
    subjects_input.fill(test_subject)
    subjects_input.press('Enter')
    page.wait_for_selector('//*[@for="hobbies-checkbox-1"]')
    page.locator('//*[@for="hobbies-checkbox-1"]').click()
    page.wait_for_selector('//*[@for="hobbies-checkbox-2"]')
    page.locator('//*[@for="hobbies-checkbox-2"]').click()
    page.wait_for_selector('//*[@id="currentAddress"]')
    page.locator('//*[@id="currentAddress"]').fill(test_address)
    page.locator('//*[@id="state"]').click()
    page.locator('//*[@id="react-select-3-option-0"]').click()
    page.locator('//*[@id="city"]').click()
    page.locator('//*[@id="react-select-4-option-0"]').click()
    page.get_by_role('button', name='Submit').click()
