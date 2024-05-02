from playwright.sync_api import expect
from test_UI_smazanik_pw.pages.BasePage import BasePage
from test_UI_smazanik_pw.pages.locators.locators import CreatePageLocators as loc


class CreateAccountPage(BasePage):
    page_url = '/customer/account/create'

    def fill_creating_form(self, first_name, last_name, email, password):
        self.find(loc.FIRST_NAME_FIELD_LOCATOR).fill(first_name)
        self.find(loc.LAST_NAME_FIELD_LOCATOR).fill(last_name)
        self.find(loc.EMAIL_FIELD_LOCATOR).fill(email)
        self.find(loc.PASSWORD_FIELD_LOCATOR).fill(password)
        self.find(loc.CONFIRM_PASSWORD_FIELD_LOCATOR).fill(password)
        self.find(loc.SUBMIT_BUTTON_LOCATOR).click()

    def check_that_account_page_is_open(self):
        expect(self.find(loc.ACCOUNT_HEADER_TITLE_LOCATOR)).to_have_text('My Account')

    def check_that_congrats_notice_is_present(self):
        expect(self.find(loc.CONGRATS_NOTICE_LOCATOR)).to_have_text(
            'Thank you for registering with Main Website Store.'
        )

    def check_that_error_is_present(self):
        expect(self.find(loc.PASSWORD_ERROR_LOCATOR)).to_have_text('This is a required field.')
        expect(self.find(loc.CONFIRM_PASSWORD_ERROR_LOCATOR)).to_have_text('This is a required field.')
