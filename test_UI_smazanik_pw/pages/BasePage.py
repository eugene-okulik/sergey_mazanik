from playwright.sync_api import Page, Locator, expect, Frame
from test_UI_smazanik_pw.pages.locators import locators as loc


class BasePage:
    base_url = 'https://magento.softwaretestingboard.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            self.page.goto(f'{self.base_url}')

    def find(self, locator: str) -> Locator:
        return self.page.locator(locator)

    def check_that_current_page_is_open(self, text):
        expect(self.find(loc.BaseLocators.PAGE_HEADER_TITLE_LOCATOR)).to_have_text(text)

    def check_that_adv_is_on_page(self):
        expect(self.find('#aswift_1_host')).to_be_in_viewport()
