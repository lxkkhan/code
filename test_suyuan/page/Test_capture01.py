"""
-*- coding:utf-8 -*-
@File: Test_capture.py
@Author: kkhan
@DateTime: 2023/11/21 10:55
@Description:
"""
import os
import random
import time


# import ConfigUtil
import cv2
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from selenium.webdriver import ActionChains

from page.base_page import BasePage


class Tet_capture01(BasePage):
    # 存放截图路径
    location_file1 = os.path.dirname(os.getcwd())
    location_file = location_file1.replace("\\","/") + "/data/picture/"
    # 文件名称
    name = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = f'{name}.png'
    filename = location_file + file
    St = location_file + 'ST.png'
    bg_img_path = filename
    slider_img_path = St
    print(filename)
    print(St)
    def test01(self):

        self.id('userCode').send_keys('gygadmin')
        self.id('pwd').send_keys('tcm2020@')
        self.xpath('//*[@id="formLogin"]/div[3]/div/div/span/button').click()
        time.sleep(3)
        el = self.class_name('slide-verify-block')
        print(el.rect)

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

        time.sleep(2)
        # 进行滑动验证，最多尝试5次重新验证
        if self.slide_verify():
            print('登陆成功')
            self.save_cookie()
            self.driver.close()
        else:
            print('第1次登陆失败')
            for i in range(4):
                print('正在尝试第%d次登陆' % (i + 2))
                if self.slide_verify():
                    print('第%d次登陆成功' % (i + 2))
                    self.save_cookie()
                    self.driver.close()
                    return
                print('第%d次登陆失败' % (i + 2))
            print('登陆失败5次，停止登陆')
            self.driver.close()

    def cv2_match_template(self):
        """
        滑动验证码匹配
        :param bg_path:
        :param tp_path:
        :return:
        """
        filename = cv2.imread(self.filename)
        St = cv2.imread(self.St)

        # 边缘检测
        img_canny1 = cv2.Canny(filename, 200.0, 300.0)
        img_canny2 = cv2.Canny(St, 200, 300)

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
        return x_offset

    def test02(self):
        # 创建 ActionChains 对象
        actions = ActionChains(self.driver)
        self.test01()
        cmt = self.cv2_match_template()

        # 拖动滑块
        slider = self.p_text('向右滑动完成拼图')
        actions.click_and_hold(slider).move_by_offset(cmt.x_offset, 0).release().perform()

    def slide_verify(self):
        '''滑动验证'''

        slider_button = self.waitX('//*[@id="slideVerify"]/div[3]/div/div/button')
        # self.bg_img_url = self.wait.until(EC.presence_of_element_located((By.XPATH, '//img[@class="yidun_bg-img"]'))).get_attribute('src')  # 获取验证码背景图url
        # self.slider_img_url = self.wait.until(EC.presence_of_element_located((By.XPATH, '//img[@class="yidun_jigsaw"]'))).get_attribute('src')  # 获取验证码滑块图url
        # urlretrieve(self.bg_img_url, self.bg_img_path)
        # urlretrieve(self.slider_img_url, self.slider_img_path)
        # print(self.slider_img_path)
        distance = self.get_distance(self.bg_img_path, self.slider_img_path)
        distance += 20  # 实际移动距离需要向右偏移10px
        tracks = self.get_tracks(distance)
        self.mouse_move(slider_button, tracks)
        try:
            element = self.waitX('//*[@id="Content0_0"]/div/div/div/div[2]/div/h1/span')
        except:
            return False
        else:
            return True

    def save_cookie(self):
        cookie = {}
        for item in self.driver.get_cookies():
            cookie[item['name']] = item['value']
        print(cookie)
        print('成功获取登cookie信息')

    def mouse_move(self, slide, tracks):
        '''鼠标滑动'''

        # 鼠标点击滑块并按照不放
        ActionChains(self.driver).click_and_hold(slide).perform()
        # 按照轨迹进行滑动，
        for track in tracks:
            ActionChains(self.driver).move_by_offset(track, 0).perform()
        ActionChains(self.driver).release(slide).perform()

    def get_distance(self, bg_img_path, slider_img_path):
        """获取滑块移动距离"""

        # 背景图片处理
        time.sleep(2)
        bg_img = cv.imread(bg_img_path,-1)  # 读入灰度图
        bg_img = cv.cvtColor(bg_img, cv.COLOR_BGR2GRAY)  # 读入灰度图

        # apply binary thresholding  图形二值化
        ret, thresh = cv.threshold(bg_img, 100, 255, cv.THRESH_BINARY)



        # visualize the binary image
        # cv.imshow('Binary image', thresh)
        # cv.waitKey(0)
        # cv.imwrite('image_thres1.jpg', thresh)
        # cv.destroyAllWindows()
        time.sleep(2)
        if thresh is None:
            print("图片文件损坏，加载资源失败！")
        else:
            print("图片正常！")

        # bg_img = cv.GaussianBlur(bg_img, (3, 3), 0,0,0)  # 高斯模糊去噪
        # bg_img = cv.Canny(bg_img, 80, 150)  # Canny算法进行边缘检测

        # 滑块做同样处理
        slider_img = cv.imread(slider_img_path, 0)
        # slider_img = np.array(slider_img)

        # detect the contours on the binary image using cv2.CHAIN_APPROX_NONE
        contours, hierarchy = cv2.findContours(image=slider_img, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_NONE)
        # draw contours on the original image
        image_copy = slider_img.copy()
        cv2.drawContours(image=image_copy, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2,
                         lineType=cv2.LINE_AA)

        # see the results
        cv2.imshow('None approximation', image_copy)

        cv2.imwrite('contours_none_image1.jpg', image_copy)


        # slider_img = cv.GaussianBlur(slider_img, (3, 3), 0,0,0)
        # slider_img = cv.Canny(slider_img, 50, 150)
        print(thresh.shape)
        cv2.imshow('thresh', bg_img)
        print(slider_img.shape)
        cv2.imshow('slider_img', slider_img)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        # 寻找最佳匹配
        res = cv.matchTemplate(thresh, slider_img, cv.TM_CCOEFF_NORMED)
        print(res)
        # 最小值，最大值，并得到最小值, 最大值的索引
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # 例如：(-0.05772797390818596, 0.30968162417411804, (0, 0), (196, 1))
        # top_left = max_loc[0]  # 横坐标
        print(cv.minMaxLoc(res))
        top_left = max_loc[0]  # 横坐标
        print(top_left)
        return top_left

    def get_tracks(self, distance=300):
        '''滑动轨迹 '''

        tracks = []
        v = 2
        t = 0.2  # 单位时间
        current = 0  # 滑块当前位移
        distance += 10  # 多移动10px,然后回退
        while current < distance:
            if current < distance * 5 / 8:
                a = random.randint(1, 5)
            else:
                a = -random.randint(2, 4)
            v0 = v  # 初速度
            track = v0 * t + 0.5 * a * (t ** 2)  # 单位时间（0.2s）的滑动距离
            tracks.append(round(track))  # 加入轨迹
            current += round(track)
            v = v0 + a * t

        # 回退到大致位置
        for i in range(5):
            tracks.append(-random.randint(1, 3))
        print(current)
        return tracks


if __name__ == '__main__':
    ca = Tet_capture01()
    ca.test01()
