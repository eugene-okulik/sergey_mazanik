from playwright.sync_api import expect
import re
from test_UI_smazanik_pw.pages.BasePage import BasePage
from test_UI_smazanik_pw.pages.locators import locators as loc


class EcoFriendlyPage(BasePage):
    page_url = '/collections/eco-friendly.html'
    product_name = None

    def move_to_product(self):
        # self.find(loc.EcoLocators.PRODUCTS_LIST_LOCATOR)
        products_list = self.find(loc.EcoLocators.PRODUCTS_LIST_LOCATOR)
        self.product_name = products_list.inner_text().split('\n')[0]
        self.find(loc.EcoLocators.PRODUCTS_LIST_LOCATOR).hover()

    def add_product_to_compare(self):
        add_to_compare_button = self.find(loc.EcoLocators.ADD_TO_COMPARE_BUTTON_LOCATOR).first
        add_to_compare_button.click()

    def add_product_to_cart(self):
        add_to_cart_button = self.find(loc.EcoLocators.ADD_TO_CART_BUTTON_LOCATOR)
        add_to_cart_button.click()

    def check_that_product_added_to_compare(self):
        expect(self.find(loc.EcoLocators.COMPARE_SECTION_LOCATOR)).to_have_text(re.compile(f'{self.product_name}'))

    def check_that_page_has_alert(self, text):
        expect(self.find(loc.EcoLocators.NOTIFICATION_ALERT_LOCATOR)).to_have_text(text)

    def check_that_right_product_page_is_open(self):
        expect(self.find(loc.BaseLocators.PAGE_HEADER_TITLE_LOCATOR)).to_have_text(self.product_name)

    def choose_product_size(self):
        self.find(loc.EcoLocators.PRODUCT_SIZE_LOCATOR).click()

    def choose_product_color(self):
        self.find(loc.EcoLocators.PRODUCT_COLOR_LOCATOR).click()

    def check_that_product_added_to_cart(self):
        expect(self.find(loc.EcoLocators.COUNTER_NUMBER_LOCATOR)).to_have_text('1')
