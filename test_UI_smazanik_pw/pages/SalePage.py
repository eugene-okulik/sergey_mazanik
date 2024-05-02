from playwright.sync_api import expect
from test_UI_smazanik_pw.pages.BasePage import BasePage
from test_UI_smazanik_pw.pages.locators.locators import SaleLocators as loc


class SalePage(BasePage):
    page_url = '/sale.html'

    def check_that_promo_button_is_clickable(self):
        promo_button = self.find(loc.SHOP_DEALS_BUTTON_LOCATOR)
        expect(promo_button).to_be_enabled()

    def click_promo_button(self):
        self.find(loc.SHOP_DEALS_BUTTON_LOCATOR).click()

    def check_that_new_page_is_open(self):
        assert f'{self.base_url}{self.page_url}' != self.page.url

    def click_on_minicart_logo(self):
        self.find(loc.MINICART_LOGO_LOCATOR).click()

    def check_that_minicart_is_empty(self):
        expect(self.find(loc.MINICART_CONTENT_LOCATOR)).to_have_text(
            'You have no items in your shopping cart.'
        )
