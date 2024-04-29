"""
Напишите тест, который заходит на страницу https://www.apple.com/shop/buy-iphone, кликает по iPhone 15 Pro &
iPhone 15 Pro Max, в открывшемся попапе проверяет заголовок.

Перед открытием страницы включите отлавливание запроса в котором приходит информация о товарах и измените ответ
так так, чтобы iPhone 15 Pro в попапе назывался "яблокофон 15 про"
"""

from playwright.sync_api import Page, expect, Route
import re
import json

phone_name = 'iPhone 15 Pro'
expect_phone_name = 'яблокофон 15 про'
phone_locator = f'//h3[contains(text(), "{phone_name}")]'
modal_title = '[data-autom="DigitalMat-overlay-header-0-0"]'


def test_listen(page: Page):

    def handle_route(route: Route):
        response = route.fetch()
        body = response.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = expect_phone_name
        body = json.dumps(body)
        route.fulfill(
            response=response,
            body=body
        )

    page.route(re.compile('digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator(phone_locator).click()
    expect(page.locator(modal_title)).to_have_text(expect_phone_name)
