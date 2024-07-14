import logging
import time

from infra.logging_basicConfig import LoggingSetup
from infra.base_page import BasePage
from infra.config_provider import ConfigProvider
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By


class LoginPage(BasePage):
    EMAIL_INPUT = '//input[@id="ap_email"]'
    PASSWORD_INPUT = '//input[@id="ap_password"]'
    SIGN_IN_BUTTON = '//input[@id="signInSubmit"]'
    SIGN_UP_BUTTON = '//a[@id="createAccountSubmit"]'
    SOLVE_THE_PUZZLE = '//span[contains(text(), "Solve this puzzle to protect your account")]'
    ALERT_MESSAGE_FOR_LOGIN = '//h4[@class="a-alert-heading"]'

    def __init__(self, driver):
        super().__init__(driver)
        logging.info("Attempting to find elements in LoginPage")
        try:
            self._email_input_field = self._driver.find_element(By.XPATH, self.EMAIL_INPUT)
            self._password_input_field = self._driver.find_element(By.XPATH, self.PASSWORD_INPUT)
            self._sign_in_button = self._driver.find_element(By.XPATH, self.SIGN_IN_BUTTON)
            self._sign_up_button = self._driver.find_element(By.XPATH, self.SIGN_UP_BUTTON)
        except NoSuchElementException:
            logging.error("Error in finding element in LoginPage")

    # this function is to write in Email input in login page.
    def write_in_email_input_field(self, user_email_input):
        self._email_input_field.click()
        self._email_input_field.send_keys(user_email_input)

    # this function is to write in password input in login page.
    def write_in_password_input_field(self, user_password_input):
        self._password_input_field.click()
        self._password_input_field.send_keys(user_password_input)

    # this function is to click on login after filling the inputs.
    def click_on_sign_in_button(self):
        self._sign_in_button.click()

    # this function to move to sign up page from sign in window.
    def click_on_sign_up_button_in_login_window(self):
        self._sign_up_button.click()

    # this function is used in most tests to sign in flow in setUps.
    def valid_login_flow(self):
        logging.info("Attempting to find elements for login flow function")
        try:
            self.config = ConfigProvider.load_from_file('../config.json')
            self.write_in_email_input_field(self.config["email"])
            self.write_in_password_input_field(self.config["password"])
        except NoSuchElementException:
            logging.error("Error in finding element for login flow function")
        self.click_on_sign_in_button()

    # this function to ensure error message when trying to invalid sign in.
    def alert_message_for_login(self):
        logging.info("Attempting to find elements for login function")
        try:
            self._alert_message_for_login = self._driver.find_element(By.XPATH, self.ALERT_MESSAGE_FOR_LOGIN)
        except NoSuchElementException:
            logging.error("Error in finding element for login function")
        logging.info("Attempting to find elements for alert message function")
        return self._alert_message_for_login.is_displayed()
