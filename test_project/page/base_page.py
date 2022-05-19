from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():
    url = ""

    def __init__(self, driver_base=None):

        if driver_base is None:
            option = Options()
            option.debugger_address = "127.0.0.1:9292"
            self.driver = webdriver.Chrome(options=option)
            self.driver.maximize_window()

        else:
            self.driver:WebDriver = driver_base
        if self.url != "":
            self.driver.get(self.url)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def id(self, element):
        return self.driver.find_element(By.ID, element)

    def name(self, element):
        return self.driver.find_element(By.NAME, element)

    def xpath(self, element):
        return self.driver.find_element(By.XPATH, element)

    def class_name(self, element):
        return self.driver.find_element(By.CLASS_NAME, element)

    def css(self, element):
        return self.driver.find_element(By.CSS_SELECTOR, element)

    def p_text(self, element):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, element)

    def ids(self, element):
        return self.driver.find_elements(By.ID, element)

    def names(self, element):
        return self.driver.find_elements(By.NAME, element)

    def xpaths(self, element):
        return self.driver.find_elements(By.XPATH, element)

    def class_names(self, element):
        return self.driver.find_elements(By.CLASS_NAME, element)

    def csses(self, element):
        return self.driver.find_elements(By.CSS_SELECTOR, element)

    def p_texts(self, element):
        return self.driver.find_elements(By.PARTIAL_LINK_TEXT, element)
