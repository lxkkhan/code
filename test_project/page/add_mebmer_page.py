from random import randint

from selenium import webdriver
from selenium.webdriver.common.by import By

from test_project.page.base_page import BasePage


class AddMemeberPage(BasePage):

    def add_member_page(self):
        a = randint(1000,9999)
        b = 1328782
        c = str(b) + str(a)
        self.id("username").send_keys('kkhan'+ str(a))
        self.id("memberAdd_acctid").send_keys('kkhan'+str(a))
        self.css("[id ='memberAdd_phone']").send_keys(c)
        self.css(".js_btn_save").click()
