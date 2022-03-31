import webbrowser

from selenium.webdriver.chrome.options import Options


class TestWeChat():
    def setup(self):
        option = Options()
        option.debugger_address('localhost:9222')
        self.driver = webbrowser.Chrome(options=option)

    def teardown(self):
        self.driver.quit()

    def test_demo0(self):
        selenium
