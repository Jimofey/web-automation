from operator import imod
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
#from selenium.webdriver import Chrome, ChromeOptions
import time
#from selenium.webdriver.support.ui import WebDriverWait #用于添加等待时间
#from selenium.common import exceptions #用于出错处理
#from selenium.webdriver.common.keys import Keys #用于按键输入

options = FirefoxOptions()
driver = webdriver.Firefox(options=options, executable_path=r"D:\Python3\geckodriver.exe",
    firefox_binary=r"C:\Program Files\Mozilla Firefox\firefox.exe")

"""用户信息配置："""
username = 'username'
password = 'password.'
url = r'http://xxx'

#打开页面
driver.get(url)

#后续可添加等待网页加载完成功能，防止find_element无法寻找到元素timeout报错。

#输入用户名
element_username = driver.find_element_by_id('password_name')
element_username.send_keys(username)

#输入密码
element_pswd = driver.find_element_by_id('password_pwd')
element_pswd.send_keys(password)

#点击提交
element_btn = driver.find_element_by_id('password_submitBtn').click()

#等待后关闭页面
time.sleep(6)
driver.close()
