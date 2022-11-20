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
