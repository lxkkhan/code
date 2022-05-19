from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage():
    _driver:WebDriver
    def __init__(self, diver:WebDriver=None):
        self._driver = diver
    def id(self, value):
        return self._driver.find_element(MobileBy.ID, value)
    