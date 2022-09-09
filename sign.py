# -*- coding: utf-8 -*-
# @Author : 艾登Aiden

import random
from appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

deviceName = '150fc297'

server = 'http://localhost:4723/wd/hub'

desired_caps = {
    'platformName': 'Android',
    'deviceName': '150fc297',
    'appPackage': 'com.tencent.wework',
    'appActivity': '.launch.LaunchSplashActivity', # # com.tencent.wework.launch.LaunchSplashActivity
    'noReset': True,
    'adbExecTimeout': 60000,
    # 'app': '/path/to/the/downloaded/ApiDemos-debug.apk',
    # 'unicodeKeyboard':True,
    # 'resetKeyboard':True,
    # 'newCommandTimeout':6000,
    # 'automationName':'UiAutomator2'
}

driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 1000)




def find_xpath_click(xpath):
    wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()

def find_xpath_send_keys(xpath, keys):
    wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(keys)

def find_id_click(id):
    wait.until(EC.presence_of_element_located((By.ID, id))).click()

def find_id_send_keys(id, keys):
    wait.until(EC.presence_of_element_located((By.ID, id))).send_keys(keys)


def wait_id(id):
    # 等待关注按钮显示, 即加载完成, 可滑动
    wait.until(EC.presence_of_element_located((By.ID, id)))

def wait_xpath(xpath):
    # 等待关注按钮显示, 即加载完成, 可滑动
    wait.until(EC.presence_of_element_located((By.XPATH, xpath)))


def video_to_swipe():
    """模拟人类向上滑动至下一个视频"""
    use_time = 1000
    # rand_start_X = random.randint(100, 110)
    # rand_start_Y = random.randint(630, 650)
    # rand_end_X = random.randint(100, 110)
    # rand_end_Y = random.randint(100, 110)
    # driver.swipe(rand_start_X, rand_start_Y, rand_end_X, rand_end_Y, use_time)
    # print(f"在 {use_time}毫秒内 由 ({rand_start_X}, {rand_start_Y}) 滑动到 ({rand_end_X} ,{rand_end_Y})")
    driver.swipe(100, 800, 100, 100, use_time)
    print('滑动至下一个视频...')
    return


def swipe(start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0):
    """ 从一个点滑动到另一个点，持续时间可选"""
    driver.swipe(start_x, start_y, end_x, end_y, duration=1)
    # driver.swipe(100, 800, 100, 100, 1)


def back_page():
    """ 页面后退一步 """
    driver.back()


def close_app():
    """ 关闭APP """
    driver.close_app()



if __name__ == '__main__':
    # is_load_complete()
    print('已进入APP主界面...')

    find_xpath_click('//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[4]/android.widget.RelativeLayout')
    print(1)
    find_xpath_click('//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout[1]')
    print(2)
    find_id_click('com.tencent.wework:id/bh6')
    print(3)

    input('任意键退出')
    input()
    print('程序结束')
