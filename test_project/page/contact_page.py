from test_project.page.add_mebmer_page import AddMemeberPage
from test_project.page.base_page import BasePage


class ContactPage(BasePage):
    def go_to_add_merber(self):
        self.css(".js_add_member:nth-child(2)").click()
        return AddMemeberPage(self.driver)


    def get_member_list(self):
        name_list = self.csses()