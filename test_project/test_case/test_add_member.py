import pytest
from nb_log import LogManager

from test_project.page.main_page import MainPage


class TestAddMember():
    logger_a = LogManager('').get_logger_and_add_handlers(log_filename='ha.log')

    def setup(self):
        self.main = MainPage()
    def test_add_member(self):
        # 主页进入添加成员页
        self.main.go_to_add_member().add_member_page()


    def test_contact_add_member(self):
        # self.main.css(".ww_commonImg_CloseDialog").click()
        # 点击添加成员页后进入
        self.main.go_to_contact().go_to_add_merber().add_member_page()

    def teardown(self):
        self.main.driver.quit()
