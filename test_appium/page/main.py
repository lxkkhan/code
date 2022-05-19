from test_appium.page.base_page import BasePage


class Main(BasePage):
    def go_to_search(self):
        # self.id("tv_search").click()
        self.steps("../page/main.yaml")