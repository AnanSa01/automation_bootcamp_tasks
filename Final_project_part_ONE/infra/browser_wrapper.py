import logging

from infra.logging_basicConfig import LoggingSetup
from selenium import webdriver
from infra.config_provider import ConfigProvider
from selenium.common.exceptions import *


class BrowserWrapper:

    def __init__(self):
        self._driver = None
        logging.info("Attempting to find elements in BrowserWrapper")
        try:
            self.config = ConfigProvider.load_from_file('../config.json')
        except NoSuchElementException:
            logging.error("Error in finding element in BrowserWrapper")
        print("\nTest Start")

    # this function takes instructions from the config file about the browser driver and the url site.
    def get_driver(self, url):
        try:
            if self.config["browser"] == "Chrome":
                self._driver = webdriver.Chrome()
            elif self.config["browser"] == "FireFox":
                self._driver = webdriver.Firefox()
            elif self.config["browser"] == "Edge":
                self._driver = webdriver.Edge()

            self._driver.get(url)
            self._driver.maximize_window()
            return self._driver
        except WebDriverException:
            logging.error("There is an error while opening the browser")
