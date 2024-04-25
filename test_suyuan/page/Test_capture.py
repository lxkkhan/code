"""
-*- coding:utf-8 -*-
@File: Test_capture.py
@Author: kkhan
@DateTime: 2023/11/21 10:55
@Description:
"""
import base64
import json
import os
import time
from pprint import pprint

# import ConfigUtil
import cv2
from selenium.webdriver import ActionChains

from page.base_page import BasePage


class Dest_capture(BasePage):
    # 存放截图路径
    location_file = os.path.dirname(os.getcwd()) + "\data\picture\\"
    # 文件名称
    name = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = f'{name}.png'
    filename = location_file + file
    St = location_file + 'p.png'

    def Dest01(self):
        self.id('userCode').send_keys('gygadmin')
        self.id('pwd').send_keys('tcm2020@')
        self.xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()
        el = self.class_name('slide-verify-block')
        # 滑动大图
        el.screenshot(self.filename)
        # 滑动小图
        action = ActionChains(self.driver).move_to_element(el)  # 移动到该元素
        action.context_click(el)  # 右键点击该元素
        action.perform()  # 执行
        # pyautogui.typewrite(['v'])  # 敲击V进行保存

        os.system('D:\gitCode\code\/test_suyuan\data\/test.exe')
        # 单击图片另存之后等1s敲回车
        # time.sleep(1)
        # pyautogui.typewrite(['enter'])

    def Dest02(self):
        '''
        通过调用监听方法，获取接口返回值并且转json
        :return: 返回加密的背景图和滑块图
        '''
        print(os.path.dirname(os.getcwd()))
        # self.id('userCode').send_keys('gygadmin')
        # self.id('pwd').send_keys('tcm2020@')
        self.id('userCode').send_keys('admin')
        self.id('pwd').send_keys('tcm@2020')
        self.xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()
        time.sleep(3)
        el = self.class_name('slide-verify-block')
        time.sleep(3)
        # js_p = self.js(js01)
        # 获取滑块的打开
        # print(el.rect)
        pic_base64 = self.get_Base64pic()
        pic_base64_j = json.loads(pic_base64)
        back_pic_base64 = pic_base64_j['targetImage']
        p_pic_base64 = pic_base64_j['cutImage']
        self.q_se()
        return back_pic_base64, p_pic_base64

    def base_to_pic(self, b_base, p_base):
        """
        :param b_base: base64加密的 背景图 string
        :param p_base: base64加密的 滑块 string
        :return:
        """
        b_imagedata = base64.b64decode(bytes(b_base, encoding="utf-8"))
        p_imagedata = base64.b64decode(bytes(p_base, encoding='utf-8'))
        with open(self.filename, 'wb') as f:
            f.write(b_imagedata)
        with open(self.St, 'wb') as f:
            f.write(p_imagedata)

    def cv2_match_template(self):
        """
        滑动验证码匹配
        :param bg_path:filename base64解析出来的背景图片
        :param tp_path:St base64解析出来的滑块
        :return: 由于识别的图片中心位置，所以返回的时候需要增加10  半个滑块的距离
        """
        filename = cv2.imread(self.filename)
        St = cv2.imread(self.St)

        # 边缘检测
        img_canny1 = cv2.Canny(filename, 100.0, 200.0)
        img_canny2 = cv2.Canny(St, 100, 200)
        # 转换图片格式
        bg_pic = cv2.cvtColor(img_canny1, cv2.COLOR_GRAY2RGB)
        tp_pic = cv2.cvtColor(img_canny2, cv2.COLOR_GRAY2RGB)

        # 缺口匹配
        res = cv2.matchTemplate(bg_pic, tp_pic, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)  # 寻找最优匹配
        # tl = max_loc  # 左上角点的坐标
        x_offset = int(max_loc[0])
        # x_offset = int(tl[0])
        # 15 是滑动验证码凸起的距离
        # x_offset = (x_offset / ConfigUtil.RENDERED_RATIO) + 17
        print(x_offset)
        return x_offset + 10

    def Dest03(self, cmt):
        # 创建 ActionChains 对象
        actions = ActionChains(self.driver)
        slider = self.waitByX('//*[@id="slideVerify"]/div[3]/div/div/button')
        actions.click_and_hold(slider).move_by_offset(cmt, 0).release().perform()

        time.sleep(5)

    def Dest04(self):
        '''
        进入系统后初始化
        选择数字医馆
        切换到南海馆
        :return:
        '''
        actions = ActionChains(self.driver)
        # actions.click_and_hold('').click().perform()
        actions.move_to_element(self.class_name('org-wrapper')).perform()
        self.xpath('/html/body/div[3]/div/div/div/ul/li[2]/span').click()

    def logIn(self):
        # self.ca = Test_capture()
        data = self.Dest02()
        b_base, p_base = data

        self.base_to_pic(b_base, p_base)
        pprint('图片转换成功')

        cmt = self.cv2_match_template()
        pprint('匹配成功')

        self.Dest03(cmt=cmt)
        pprint('滑动验证成功！')

        self.Dest04()

if __name__ == '__main__':
    ca = Dest_capture()
    ca.logIn()
    data = ca.Dest02()
    b_base, p_base = data

    ca.base_to_pic(b_base, p_base)
    pprint('图片转换成功')

    cmt = ca.cv2_match_template()
    pprint('匹配成功')

    ca.Dest03(cmt=cmt)
    pprint('滑动验证成功！')

    # ca.test04()
