"""
-*- coding:utf-8 -*-
@File: TEST_proxy.py
@Author: kkhan
@DateTime: 2023/12/14 9:52
@Description:
"""
# -*- coding: utf-8 -*-
# 导入相应的库
from browsermobproxy import Server
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from pprint import pprint

base_url = 'https://item.jd.com/7670969.html'

# browsermob-proxy.bat就是刚才下载的文件解压得来，路径根据自己实际的进行修改，我这里是解压放到了Dp盘；port为端口，根据自己情况进行修改，我这里顺便写入了8739
server = Server(r'D:\001soft\browsermob-proxy-2.1.4-bin\browsermob-proxy-2.1.4\bin\browsermob-proxy.bat', {'port': 8739})
server.start()
proxy = server.create_proxy()

chrome_options = Options()
# 无浏览器界面，根据自己实际情况是否使用，我这里使用浏览器界面，故注释了这行代码
# chrome_options.add_argument('--headless')

# 不加载图片，提升运行速度
# chrome_options.add_argument('blink-settings=imagesEnabled=false')

chrome_options.add_argument(
    'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36')
# 需要加上这句代码，否则有些网页会被浏览器拦截了。实际如何，看大家在用的过程的情况
chrome_options.add_argument('--ignore-certificate-errors')

# 设置代理
chrome_options.add_argument('--proxy-server={0}'.format(proxy.proxy))

driver = webdriver.Chrome(options=chrome_options)

proxy.new_har('html_list', options={'captureContent': True})
# 也可以以目标URL配置一个新的HAR并获取HAR内容
# proxy.new_har(base_url)

driver.get(base_url)

# 暂停几秒等待页面加载完成，防止拿不到结果
proxy.wait_for_traffic_to_stop(1, 30)
result = proxy.har

# pprint(result)

'''
open(filename[, mode[, buffering]])函数参数的说明：
name : 一个包含了你要访问的文件名称的字符串值。
mode : mode 决定了打开文件的模式：只读，写入，追加等。所有可取值见如下的完全列表。这个参数是非强制的，默认文件访问模式为只读(r)。
buffering : 如果 buffering 的值被设为 0，就不会有寄存。如果 buffering 的值取 1，访问文件时会寄存行。如果将 buffering 的值设为大于 1 的整数，表明了这就是的寄存区的缓冲大小。如果取负值，寄存区的缓冲大小则为系统默认。

不同模式打开文件的参照：
    r：以只读方式打开文件。文件的指针将会放在文件的开头。这是默认模式。
    r+：打开一个文件用于读写。文件指针将会放在文件的开头。

    b：二进制模式，多用于图片读写。
    +：打开一个文件进行更新(可读可写)。

    w：打开一个文件只用于写入。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。
    w+：打开一个文件用于读写。如果该文件已存在则打开文件，并从开头开始编辑，即原有内容会被删除。如果该文件不存在，创建新文件。

    a：打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    a+：打开一个文件用于读写。如果该文件已存在，文件指针将会放在文件的结尾。文件打开时会是追加模式。如果该文件不存在，创建新文件用于读写。
    ……
'''
with open('./file/proxy.har', 'w') as f:
    json.dump(result, f)

# 把 包即url地址 存到txt文件中
with open('./file/request_url.txt', 'a') as u:
    for ent in result['log']['entries']:
        url = ent['request']['url']
        # json.dump(url, u)#这种方式保存的内容会放在双引号中，即格式为：“写入的内容”
        u.write(url + '\n')  # 这种方式内容不会放在双引号中，使用那种方式存储内容看大家喜欢。

server.stop()
driver.quit()
