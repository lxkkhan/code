import shelve
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class Test_webchat():
    '''
    课后作业：
    使用cookie 登录企业微信，完成导入联系人，加入检查点

    '''

    def setup(self):
        # chrome_opts = webdriver.ChromeOptions()
        # chrome_opts.debugger_address = "127.0.0.1:9222"
        # self.driver = webdriver.Chrome(options=chrome_opts)
        #
        # self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        cookies = {
            'pgv_pvid' :'5223734872',
            'pac_uid' : "0_b51398c054c30",
            'tvfe_boss_uuid':'1da8a40cf3fbd6a4',
            'fqm_pvqid' :'5c10cce9-7469-4ac5-b1e0-afd424bc33de',
            'wwrtx.c_gdpr' :0,
            'Hm_lvt_9364e629af24cb52acc78b43e8c9f77d' : "1645885263",
            '_ga ':'GA1.2.2106617998.1645885264',
            'wwrtx.i18n_lan' :'zh',
            'wwrtx.ref' : 'direct',
            'wwrtx.refid': "01455159",
            'wwrtx.d2st':'a8566508',
            'wwrtx.sid':"Fg0Kq8bp6Ifl1A7gLcxMHGRITITz17uBLgLTbKHC8An521b9LEb_3Y9PrgC6KBkB",
            'wwrtx.ltype':1,
            'wwrtx.vst' :"SZN3PCJTdrRjy4PkLYtUOcTaC6_ETxRSreFvXLUu5AYoEFlVrmqWxTEAFHuGsXenubhE1_YKwzlesUUj4AJpEqXu10F19tORwYnw7L9KXyj_lw58p8yTuikmF3kra_girmBpJM5h5j3BW4zzWJmriX-3f-pRDN9PUxaqYHPt2wv0Me-jjHgV12TgvR35jquhUv3e0lC-Lqb6jOG70iVUQPdg8TPxjtmOSe9kg7hmL173uYwDWoyM8FueMYuQEGKr_TccRz1T4LUTpFfGEWeAfg",
            'wwrtx.vid ':1688856213326587,
            'wxpay.corpid' : 1970326031977888,
            'wxpay.vid' :1688856213326587,
            'wwrtx.cs_ind':"",
            'wwrtx.logined':"true",
        }
        # db = shelve.open('mydb/loginCookie.db')
        # db['cookies'] = cookies
        # db.close()
        # print(cookies)

        self.driver = webdriver.Chrome()

        # db1 = shelve.open('mydb/loginCookie.db')
        # cookies1 = db1['cookies']
        # db1.close()
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies.keys():
            print(cookie)
            if 'expiry' in cookie:
                cookie.pop('expiry')
            self.driver.add_cookie(cookies)

        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)

        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_add_contact(self):
        self.driver.find_element(By.ID, 'menu_contacts').click()
        # self.driver.find_element(By.CSS_SELECTOR, '#js_contacts105 > div > div.member_colRight > div > div.js_party_info > div.member_colRight_cnt_NoData.js_no_member > div.member_colRight_cnt_operation > div > a > div.ww_btn_PartDropdown_left').click()



