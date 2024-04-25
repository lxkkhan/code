"""
-*- coding:utf-8 -*-
@File: Test_cv.py
@Author: kkhan
@DateTime: 2023/11/30 15:25
@Description:
"""
import time

import cv2 as cv

slider_img_path = 'D:/gitCode/code/test_suyuan/data/picture/ST.png'
bg_img_path = 'D:/gitCode/code/test_suyuan/data/picture/2023_11_30_15_14_14.png'

def Cest01(bg_img_path,slider_img_path):

    # bg_img = cv.imread(bg_img_path, 0)  # 读入灰度图
    bg_img_path = cv.imread(bg_img_path)
    bg_img = cv.cvtColor(bg_img_path,  cv.COLOR_BGR2GRAY)  # 读入灰度图

    # apply binary thresholding
    ret, thresh = cv.threshold(bg_img, 80, 255, cv.THRESH_BINARY_INV)
    # visualize the binary image
    cv.imshow('Binary image', thresh)
    cv.waitKey(0)
    cv.imwrite('image_thres1.jpg', thresh)
    cv.destroyAllWindows()

    print(thresh)
    # bg_img = np.array(bg_img)
    # bg_img = cv.imshow(bg_img,bg_img)
    time.sleep(2)
    if bg_img is None:
        print("图片文件损坏，加载资源失败！")
    else:
        print("图片正常！")

    bg_img = cv.GaussianBlur(bg_img, (3, 3), 0, 0, 0)  # 高斯模糊去噪
    bg_img = cv.Canny(bg_img, 80, 150)  # Canny算法进行边缘检测

    # 滑块做同样处理
    slider_img = cv.imread(slider_img_path, 0)
    # slider_img = np.array(slider_img)

    slider_img = cv.GaussianBlur(slider_img, (3, 3), 0, 0, 0)
    slider_img = cv.Canny(slider_img, 50, 150)
    print(bg_img.shape)
    cv.imshow('bg_img', bg_img)
    print(slider_img.shape)
    cv.imshow('slider_img', slider_img)

    cv.waitKey(0)
    cv.destroyAllWindows()
    # 寻找最佳匹配
    res = cv.matchTemplate(bg_img, slider_img, cv.TM_CCOEFF_NORMED)
    # 最小值，最大值，并得到最小值, 最大值的索引
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
    # 例如：(-0.05772797390818596, 0.30968162417411804, (0, 0), (196, 1))
    # top_left = max_loc[0]  # 横坐标
    print(cv.minMaxLoc(res))
    top_left = max_loc[0]  # 横坐标
    print(top_left)
    return top_left

def ces02(slider_img_path):
    image = cv.imread(slider_img_path)
    cv.imshow('image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()

    # 创建Haar级联分类器
    cascade = cv.CascadeClassifier('D:/001soft/opencv/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml')
    # cascade.load(r"D:/001soft/opencv/opencv/build/etc/haarcascades/haarcascade_frontalface_default.xml")

    # 使用分类器检测边界框
    bounding_boxes = cascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    print(bounding_boxes)

    for (x, y, w, h) in bounding_boxes:
        cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # cropped_image = image[y:y + h, x:x + w]
        #
        # cv.imshow('Cropped_Image', cropped_image)
        # cv.waitKey(0)
        # cv.destroyAllWindows()
    cv.imshow('image', image)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
    # Cest01(bg_img_path,slider_img_path)
    ces02(slider_img_path='D:/gitCode/code/test_suyuan/data/picture/R.jpg')