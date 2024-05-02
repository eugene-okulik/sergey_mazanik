def test_header_title_is_correct(sale_page):
    sale_page.open_page()
    sale_page.check_that_current_page_is_open('Sale')


def test_adv_is_on_page(sale_page):
    sale_page.open_page()
    sale_page.check_that_adv_is_on_page()


def test_promo_button(sale_page):
    sale_page.open_page()
    sale_page.check_that_promo_button_is_clickable()
    sale_page.click_promo_button()
    sale_page.check_that_new_page_is_open()


def test_empty_minicart(sale_page):
    sale_page.open_page()
    sale_page.click_on_minicart_logo()
    sale_page.check_that_minicart_is_empty()
