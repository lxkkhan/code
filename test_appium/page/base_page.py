import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage():
    _driver:WebDriver
    def __init__(self, diver:WebDriver=None):
        self._driver = diver
    def id(self, value):
        return self._driver.find_element(By.ID, value)

    def find(self, locator, value):
        return self._driver.find_element(locator, value)

    def steps(self,path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step['by'], step['locator'])
            if "action" in step.keys():
                action =step["action"]
                if action == "click":
                    element.click()
