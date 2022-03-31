from selenium.webdriver.common.by import By
from time import sleep
from Base import Base


class TestBaidu(Base):
    """
    1、打开百度搜索
    2、输入关键字
    3、点击搜索跳转到搜索页
    4、滑动到底部，点击下一页
    """

    def test_baidu(self):
        self.driver.get("http://www.baidu.com")
        self.driver.find_element(By.ID, 'kw').send_keys('selenium')
        # js定位百度一下  id=‘su'  注意通过js 获取的元素一定加上return
        self.driver.execute_script('return document.getElementById("su")').click()
        # 通过滑动js到页面底部
        self.driver.execute_script('return document.documentElement.scrollTop=10000')
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        sleep(3)
        # 批量执行 js
        for code in [
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        # 方式二
        print(self.driver.execute_script('return document.title;return JSON.stringify(performance.timing'))

    def test_datatime(self):
        self.driver.get("")

        self.driver.execute_script(
            'a = return document.getElementById("train_date"); a.removeAttribute("readOnly");a.value')
