from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://yinxiang.com/webclipper/install/chrome/")
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.find_element(By.XPATH,
                                 '//*[@id="wrap"]/div/div/section[2]/div/div/div[1]/div/div/section/div/div/div[3]/div/div/div[2]/div/div/p[1]/a').click()
        # # 方式一
        # # 此处逻辑是通过获取得元素数量大于等于1
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,
        #                                     '//*[@id="main"]/div/div/div/section[6]/div/div/div[2]/div/div/div['
        #                                     '1]/div/div/p')) >= 1
        # #  注意此处的wait   是直接传入不是引用wait()
        # WebDriverWait(self.driver, 10).until(wait)

        # 方式二：
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div/div/div/section[6]/div/div/div[2]/div/div/div[1]/div/div/p')))
        self.driver.find_element(By.XPATH,
                                 '//*[@id="wrap"]/div/div/section[2]/div/div/div[1]/div/div/section/div/div/div['
                                 '4]/div/div/div[2]/div/div/p[3]/a').click()
        self.driver.save_screenshot("qu.png")