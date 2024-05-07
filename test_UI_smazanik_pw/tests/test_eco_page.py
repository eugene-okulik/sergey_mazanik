def test_header_title_is_correct(eco_page):
    eco_page.open_page()
    eco_page.check_that_current_page_is_open('Eco Friendly')


def test_compare_product(eco_page):
    eco_page.open_page()
    eco_page.move_to_product()
    eco_page.add_product_to_compare()
    eco_page.check_that_product_added_to_compare()


def test_add_product_to_cart_without_properties(eco_page):
    eco_page.open_page()
    eco_page.move_to_product()
    eco_page.add_product_to_cart()
    eco_page.check_that_page_has_alert('You need to choose options for your item.')
    eco_page.check_that_right_product_page_is_open()


def test_add_product_to_cart(eco_page):
    eco_page.open_page()
    eco_page.choose_product_size()
    eco_page.choose_product_color()
    eco_page.move_to_product()
    eco_page.add_product_to_cart()
    eco_page.check_that_product_added_to_cart()
