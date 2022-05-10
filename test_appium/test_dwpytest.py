from time import sleep

import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from hamcrest import assert_that, is_in, equal_to


class TestDw():
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-5554'
        # com.android.settings/com.android.settings.Settings
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'common.MainActivity'
        # 后台运行
        desired_caps['dontStopAppOnReset'] = 'true'
        # 出现升级弹窗，点击取消后下次记住不会再弹出
        desired_caps['noReset'] = 'true'
        desired_caps['skipDeviceInitialization'] = 'true'
        # 输入中文设置参数
        desired_caps['unicodeKeyBoard'] = 'true'
        desired_caps['resetKeyBoard'] = 'true'
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()



    def test_search(self):
        print("搜索测试用例")
        '''
        1、打开需求app
        2、点击搜索输入框
        3、向搜索输入框中输入“阿里巴巴‘   # 输入中文需要在desir 中添加参数 unicodeKeyBoard   true
        4、在搜索结果中选择“阿里巴巴”，然后点击
        5、获取这只香港上市的阿里巴巴股价，并判断这只股价的价格 >200
        '''
        # self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/home_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')

    def test_get_current(self):
        '''
        1、打开需求app
        2、点击搜索输入框
        3、向搜索输入框中输入“阿里巴巴‘   # 输入中文需要在desir 中添加参数 unicodeKeyBoard   true
        4、在搜索结果中选择“阿里巴巴”，然后点击
        5、通过text 方式获取这只香港上市的阿里巴巴当前股价，并判断这只股价的价格 >200
        '''
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/tv_search").click()
        self.driver.find_element(MobileBy.ID, "com.xueqiu.android:id/search_input_text").send_keys('阿里巴巴')
        self.driver.find_element(MobileBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴-SW']").click()
        current_price = self.driver.find_element(MobileBy.XPATH, '//*[@text="09988"]/../../..//*[@resource-id="com.xueqiu.android:id/current_price"]').text
        print(f"港股中阿里巴巴当前股价为{current_price}！")
        assert float(current_price) < 100


    def test_mylogin(self):
        '''
        通过uiautomator 方式定位元素
        :return:
        '''
        self.driver.find_element_by_android_uiautomator('new UiSelector().text("我的")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().textContains("帐号密码")').click()
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_account")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/login_password")').send_keys('123456')
        self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/button_next")').click()
        toast_text = self.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("com.xueqiu.android:id/md_content")').text
        assert_that('手机号码填写错误', is_in(toast_text))

if __name__ == '__main__':
    pytest.main()
