from appium import webdriver

from test_appium.page.base_page import BasePage
from test_appium.page.main import Main


class App(BasePage):
    _package ="com.xueqiu.android"
    _activity = "common.MainActivity"
    def start(self):
        if self._driver is None:
            desired_caps = {}
            desired_caps['platformName'] = 'Android'
            desired_caps['platformVersion'] = '6.0'
            desired_caps['deviceName'] = 'emulator-5554'
            # com.android.settings/com.android.settings.Settings
            desired_caps['appPackage'] = self._package
            desired_caps['appActivity'] = self._activity
            # 后台运行
            desired_caps['dontStopAppOnReset'] = 'true'
            # 出现升级弹窗，点击取消后下次记住不会再弹出,不会重新设置
            desired_caps['noReset'] = 'true'
            desired_caps['skipDeviceInitialization'] = 'true'
            # 输入中文设置参数
            desired_caps['unicodeKeyBoard'] = 'true'
            desired_caps['resetKeyBoard'] = 'true'
            self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        else:
            self._driver.start_activity(self._package,self._activity)
        self._driver.implicitly_wait(3)
        return self

    def main(self) -> Main():
        return Main(self._driver)

