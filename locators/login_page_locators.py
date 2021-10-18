from selenium.webdriver.common.by import By


class LoginPageLocators:

    # Locators
    ACCOUNT_TEXT_FIELD = (
        By.XPATH, "/html[@id='facebook']//div[@class='login_form_container']/form[@id='login_form']/div[@id='loginform']//input[@id='email']")
    PASSWORD_TEXT_FIELD = (
        By.XPATH, "/html[@id='facebook']//div[@class='login_form_container']/form[@id='login_form']/div[@id='loginform']//input[@id='pass']")
    LOGIN_BUTTON = (
        By.XPATH, "/html[@id='facebook']//div[@class='login_form_container']/form[@id='login_form']/div[@id='loginform']//button[@id='loginbutton']")
