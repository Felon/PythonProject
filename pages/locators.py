from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    LOGIN_EMAIL = (By.NAME, 'login-username')
    LOGIN_PSW = (By.NAME, 'login-password')
    REGISTRATION_FORM = (By.ID, 'register_form')
    REGISTRATION_EMAIL = (By.NAME, 'registration-email')
    REGISTRATION_PSW = (By.NAME, 'registration-password1')
    REGISTRATION_PSW_CONFIRM = (By.NAME, 'registration-password2')
    REGISTRATION_BUTTON = (By.NAME, 'registration_submit')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    BUTTON_VIEW_BASKET = (By.CSS_SELECTOR, '.btn-group > .btn')
    CLEAR_BASKET = (By.CSS_SELECTOR, '#content_inner p')
    BUTTON_CKECKOUT = (By.CLASS_NAME, 'btn-primary')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CSS_SELECTOR, '.product_main > .price_color')
    ALERT_MESSAGE = (By.CSS_SELECTOR, "div.alert:nth-child(1) strong")
    ALERT_BOOK_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    ADDED_BOOK_NAME = (By.CSS_SELECTOR, '.col-sm-4 a')
    ADDED_BOOK_PRICE = (By.CSS_SELECTOR, '.col-sm-1 p')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
