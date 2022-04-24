from time import sleep

from test_project.page.add_mebmer_page import AddMemeberPage
from test_project.page.base_page import BasePage
from test_project.page.contact_page import ContactPage


class MainPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame#index"
    def go_to_contact(self):
        self.xpath('//*[@id="menu_contacts"]').click()
        sleep(2)
        return ContactPage(self.driver)

    def go_to_add_member(self):

        self.css("[node-type='addmember']").click()
        return AddMemeberPage(self.driver)