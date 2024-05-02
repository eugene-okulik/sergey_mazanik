from playwright.sync_api import BrowserContext
from test_UI_smazanik_pw.pages.EcoFriendlyPage import EcoFriendlyPage
from test_UI_smazanik_pw.pages.SalePage import SalePage
from test_UI_smazanik_pw.pages.CreateAccauntPage import CreateAccountPage
import pytest


@pytest.fixture()
def page(context: BrowserContext):
    page = context.new_page()
    return page


@pytest.fixture()
def eco_page(page):
    return EcoFriendlyPage(page)


@pytest.fixture()
def sale_page(page):
    return SalePage(page)


@pytest.fixture()
def create_account_page(page):
    return CreateAccountPage(page)
