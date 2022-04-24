import shelve

from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestWeChat():
    def setup(self):
        option = Options()
        option.debugger_address('localhost:9222')
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_demo0(self):
        self.driver.get("https://ceshiren.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, '所有分类').click()
        # 断言
        myclass = self.driver.find_element(By.LINK_TEXT, "所有分类").get_attribute('class')
        assert "active" == myclass
        sleep(3)

    def test_cookie(self):
        '''
        cookies  通过内置数据库shelve持久化保存

        步骤：
        1、通过get_cookies() 获取登录后的cookie
        2、通过新建shelve  cookies 保存到数据库
        3、通过获取数据库中保存的cookie  来做到使用
        :return:
        '''
        # 获取登录后的cookie 并保存，讲cookies 加入到其他操作中
        # 注意：需要添加cookies 前后登录两次
        cookies = [__tea__ug__uid=7073450658967750185; _ga=GA1.2.880842462.1646916082; passport_web_did=7073450737790910466; locale=zh-CN; trust_browser_id=f388c70d-ba5b-4baa-892a-e35c3442eca8; fid=ac5d41c3-6083-41f9-a738-4a25f148ec92; session=XN0YXJ0-b55tb1ec-606d-4bf4-a5da-55c9d7a5a13d-WVuZA; session_list=XN0YXJ0-b55tb1ec-606d-4bf4-a5da-55c9d7a5a13d-WVuZA_XN0YXJ0-56ao19c2-15f2-4842-b4a3-b6865d9f642c-WVuZA; is_anonymous_session=; _csrf_token=f0c48f6b592f2c8e98d3c7b5adb2612a9e99e5f1-1646916125; MONITOR_WEB_ID=6900515699807027203; lang=zh; garr_base_template_branch=master; garr_version_list={}; et=e17fde9c46ece722541876a7089bba47; ot=e17fde9c46ece722541876a7089bba47; vt=1; slardar_delay_type=a; _uuid_hera_ab_path_1=7080898572970934274; landing_url=https://www.feishu.cn/; Hm_lvt_e78c0cb1b97ef970304b53d2097845fd=1648650187; _gid=GA1.2.1675387985.1648650189; template-branch-list=; garr_master_versions={"garrMasterDocx":"20220317","garrMasterBitable":"20220317","garrMaster":"20210315","garrMasterBottomTemplate":"20220317","garrMasterTemplateCenter":"20220317","garrMasterSheet":"20220317"}; last_access_scm_version=1.0.6.547; swp_csrf_token=5db3db4a-0159-4d42-b723-a44bac657495; t_beda37=6a927a7b752df24425a759962e292217298022b5ec38aa11fc5401dc642e8bee]
        self.driver.get("url")
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.get("url")

        # 获取cookies 并保存到数据库
        cookies = self.driver.get_cookies()
        db = shelve.open('mydb/logincookies')
        db['cookies'] = cookies
        db.close()

        # 查询数据库中的cookies
        # 注意：需要添加cookies 前后登录两次
        db1 = shelve.open('mydb/logincoookies')
        cookies1 = db1['cookies']
        db1.close()
        self.driver.get("url")

        for cookie in cookies1:
            self.driver.add_cookie(cookie)

        self.driver.get("url")

