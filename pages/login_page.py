from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators


class LoginPage(BasePage):

    login_locators = LoginPageLocators

    def is_able_to_login(self):
        return self.is_element_present(self.login_locators.LOGIN_BUTTON)

    def input_account(self, account):
        self.find_element(
            self.login_locators.ACCOUNT_TEXT_FIELD).send_keys(account)

    def input_password(self, password):
        self.find_element(
            self.login_locators.PASSWORD_TEXT_FIELD).send_keys(password)

    def click_login_button(self):
        self.find_element(self.login_locators.LOGIN_BUTTON).click()
        self.wait_page_until_loading()
