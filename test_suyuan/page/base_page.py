import json
import os
import time
from pprint import pprint

from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage():
    # url = "https://login.zgzykg.com.cn/#/user/login?sysCode=gygBasic"
    url = "https://workorder.zgzykg.com.cn/#/user/login?sysCode=gygBasic"
    # 启动proxy
    server = Server('D:\\001soft\\browsermob-proxy-2.1.4-bin\\browsermob-proxy-2.1.4\\bin\\browsermob-proxy.bat')
    server.start()
    proxy = server.create_proxy()
    # driver 实例化之前添加，表示我要监听请求头和响应内容
    proxy.new_har("GYG", options={'captureHeaders': True, 'captureContent': True})

    def __init__(self, driver_base=None):

        if driver_base is None:
            options = webdriver.ChromeOptions()

            # 默认下载地址,去掉登陆后提示的保存账号密码弹窗
            prefs = {
                'download.default_directory': os.getenv('OS_LOG_PATH'),
                "safebrowsing.enabled": True,
                "credentials_enable_service": False,
                "profile.password_manager_enabled": False
            }
            options.add_experimental_option('prefs',prefs)
            # 防止被系统监控，反爬虫
            options.add_experimental_option('useAutomationExtension', False)
            options.add_experimental_option('excludeSwitches', ['enable-automation'])
            # 打开F12
            # options.add_argument("--auto-open-devtools-for-tabs")
            # 打开代理监听
            options.add_argument('--proxy-server={0}'.format(self.proxy.proxy))
            options.add_argument('--use-littleproxy=false')

            self.driver = webdriver.Chrome(options=options)
            self.driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                  get: () => undefined
                })
              """
            })

            capabilities = webdriver.DesiredCapabilities().CHROME
            capabilities['acceptSslCerts'] = True
            self.driver.maximize_window()

        else:
            self.driver:WebDriver = driver_base
        if self.url != "":
            self.driver.get(self.url)
        # 隐式等待
        self.driver.implicitly_wait(5)

    def get_Base64pic(self):
        '''
        通过 browse_proxy设置监听
        监听对应接口，如果有请求就获取相应的内容  response
        :return:
        '''
        result = self.proxy.har
        for entry in result['log']['entries']:
            _url = entry['request']['url']
            # 根据URL找到数据接口
            if "/ssoServer/sysmp/graphVerifyCtrl/getImgVerify" in _url:
                _response = entry['response']
                content = _response['content']['text']

                return content

    def q_se(self):
        return self.server.stop()


    def id(self, element):
        return self.driver.find_element(By.ID, element)

    def name(self, element):
        return self.driver.find_element(By.NAME, element)

    def xpath(self, element):
        return self.driver.find_element(By.XPATH, element)

    def class_name(self, element):
        return self.driver.find_element(By.CLASS_NAME, element)

    def css(self, element):
        return self.driver.find_element(By.CSS_SELECTOR, element)

    def p_text(self, element):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, element)

    def ids(self, element):
        return self.driver.find_elements(By.ID, element)

    def names(self, element):
        return self.driver.find_elements(By.NAME, element)

    def xpaths(self, element):
        return self.driver.find_elements(By.XPATH, element)

    def class_names(self, element):
        return self.driver.find_elements(By.CLASS_NAME, element)

    def csses(self, element):
        return self.driver.find_elements(By.CSS_SELECTOR, element)

    def p_texts(self, element):
        return self.driver.find_elements(By.PARTIAL_LINK_TEXT, element)

    def waitByX(self, element):
        wait = WebDriverWait(self.driver,5,0.5)
        return wait.until(EC.element_to_be_clickable((By.XPATH, element)))

    def waitByD(self, element):
        wait = WebDriverWait(self.driver,5,0.5)
        return wait.until(EC.element_to_be_clickable((By.ID, element)))

    def js(self,element):
        return self.driver.execute_script(element)

    def js_asy(self,element):
        return self.driver.execute_async_script(element)



