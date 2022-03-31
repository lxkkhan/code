import os

from selenium import webdriver


class Base(object):
    def setup(self):
        browser = os.getenv('browser')
        if browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == 'headless':
            self.driver = webdriver.phantomjs()
        else:
            self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
