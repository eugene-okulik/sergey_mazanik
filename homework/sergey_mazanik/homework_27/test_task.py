"""
Задание 1
Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/alert/confirm, кликает на кнопку,
чтобы появился алерт, жмет Ok и проверяет, что на страние в секции "You selected" написано "Ok"

Задание 2
Напишите тест, который зайдет на страницу https://www.qa-practice.com/elements/new_tab/button, нажмет на кнопку Click,
в открывшемся табе проверит, что в результате написано "I am a new page in a new tab" и проверит, что на изначальной
вкладке кнопка Click - активна (enabled)

Задание 3
Напишите тест, который зайдет на страницу https://demoqa.com/dynamic-properties, нажмет на кнопку Color change только
после того как она станет красной.
"""

from playwright.sync_api import Page, expect, BrowserContext


def test_first_alert(page: Page):
    page.on('dialog', lambda alert: alert.accept())
    page.goto('https://www.qa-practice.com/elements/alert/confirm')
    page.locator('.a-button').click()
    you_selected_area = page.locator('#result-text')
    expect(you_selected_area).to_have_text('Ok')


def test_second_tabs(page: Page, context: BrowserContext):
    text = 'I am a new page in a new tab'
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    link = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    result_text = new_page.locator('#result-text')
    expect(result_text).to_have_text(text)
    expect(link).to_be_enabled()


def test_third_change_color(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#colorChange')
    expect(button).to_have_css('color', 'rgb(220, 53, 69)')
    button.click()
