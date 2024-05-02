class BaseLocators:
    PAGE_HEADER_TITLE_LOCATOR = '//*[@data-ui-id="page-title-wrapper"]'
    IFRAME_LOCATOR = 'iframe'
    ADV_LOCATOR = '#google_image_div'


class CreatePageLocators:
    FIRST_NAME_FIELD_LOCATOR = '#firstname'
    LAST_NAME_FIELD_LOCATOR = '#lastname'
    EMAIL_FIELD_LOCATOR = '#email_address'
    PASSWORD_FIELD_LOCATOR = '#password'
    CONFIRM_PASSWORD_FIELD_LOCATOR = '#password-confirmation'
    SUBMIT_BUTTON_LOCATOR = '.submit'
    FIRST_NAME_ERROR_LOCATOR = '#firstname-error'
    LAST_NAME_ERROR_LOCATOR = '#lastname-error'
    EMAIL_ERROR_LOCATOR = '#email_address-error'
    PASSWORD_ERROR_LOCATOR = '#password-error'
    CONFIRM_PASSWORD_ERROR_LOCATOR = '#password-confirmation-error'
    ACCOUNT_HEADER_TITLE_LOCATOR = '//*[@data-ui-id="page-title-wrapper"]'
    CONGRATS_NOTICE_LOCATOR = '//*[@data-ui-id="message-success"]/div'


class EcoLocators:
    PRODUCTS_LIST_LOCATOR = '(//*[@class="product-item-info"])[1]'
    ADD_TO_COMPARE_BUTTON_LOCATOR = '//*[@title="Add to Compare"]'
    COMPARE_SECTION_LOCATOR = '.odd'
    ADD_TO_CART_BUTTON_LOCATOR = '(//*[@title="Add to Cart"])[1]'
    NOTIFICATION_ALERT_LOCATOR = '//*[@data-ui-id="message-notice"]/div'
    PRODUCT_SIZE_LOCATOR = '(//*[@id="option-label-size-143-item-171"])[1]'
    PRODUCT_COLOR_LOCATOR = '(//*[@id="option-label-color-93-item-49"])[1]'
    COUNTER_NUMBER_LOCATOR = '.counter-number'


class SaleLocators:
    SHOP_DEALS_BUTTON_LOCATOR = '//*[@class="more button"]'
    MINICART_LOGO_LOCATOR = '.showcart'
    MINICART_CONTENT_LOCATOR = '.subtitle.empty'
