# -*- coding: utf-8 -*-
# @Author : 艾登Aiden

import random
from zlib import DEF_BUF_SIZE
from appium import webdriver
import time
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import WebDriverException

class WeWorkSign(object):

    def __init__(self, deviceName, appPackage, appActivity):

        # deviceName = '150fc297'
        # # com.tencent.wework.launch.LaunchSplashActivity
        # appPackage = 'com.tencent.wework'
        # appActivity = '.launch.LaunchSplashActivity'

        server = 'http://localhost:4723/wd/hub'

        desired_caps = {
            'platformName': 'Android',
            'deviceName': deviceName,
            'appPackage': appPackage,
            'appActivity': appActivity,
            'noReset': True,
            'adbExecTimeout': 60000,
            # 'app': '/path/to/the/downloaded/ApiDemos-debug.apk',
            # 'unicodeKeyboard':True,
            # 'resetKeyboard':True,
            # 'newCommandTimeout':6000,
            # 'automationName':'UiAutomator2'
        }

        self.driver = webdriver.Remote(server, desired_caps)
        self.timeout = 10 # second
        self.wait = WebDriverWait(self.driver, self.timeout)

    def find_element_click(self, by: str = AppiumBy.ID, value: str = None):
        """ 单击某元素 """
        self.wait.until(EC.presence_of_element_located((by, value))).click()


    def find_element_keys(self, by: str = AppiumBy.ID, value: str = None, keys: str = None):
        """ 在某元素中输入 """
        self.wait.until(EC.presence_of_element_located(
            (by, value))).send_keys(keys)


    def is_element_exist(self, by: str = AppiumBy.ID, value: str = None):
        """ 元素是否存在 """
        try:
            self.wait.until(EC.presence_of_element_located((by, value)))
            return True
        except WebDriverException:
            pass
        return False


    def wait_element(self, by: str = AppiumBy.ID, value: str = None):
        """ 等待某元素出现 """
        self.wait.until(EC.presence_of_element_located((by, value)))


    def video_to_swipe(self):
        """ 模拟单个手势滑动 """
        use_time = 1000
        start_X = 100
        start_Y = 800
        end_X = 100
        end_Y = 100
        self.driver.swipe(start_X, start_Y, end_X, end_Y, use_time)
        # print(f"在 {use_time}毫秒内 由 ({start_X}, {start_Y}) 滑动到 ({end_X} ,{end_Y})")
        return


    def swipe(self, start_x: int, start_y: int, end_x: int, end_y: int, duration: int = 0):
        """ 从一个点滑动到另一个点，持续时间可选"""
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=duration)
        # driver.swipe(100, 800, 100, 100, 1)


    def back_page(self):
        """ 页面后退一步 """
        self.driver.back()


    def close_app(self):
        """ 关闭APP """
        self.driver.close_app()


    def main(self):
        print('正在启动app...')

        # 工作台
        self.find_element_click(AppiumBy.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.RelativeLayout[4]/android.widget.RelativeLayout')
        print('工作台')

        # 打卡区域
        self.find_element_click(AppiumBy.XPATH, '//hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.FrameLayout[2]/android.widget.RelativeLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.RelativeLayout[1]')
        print('打卡区域')

        # 检查是否具备打卡条件
        # 检查当前手机定位
        # 检查按钮颜色是否为绿
        # if self.is_element_exist(AppiumBy.ID, 'xxxx'):
        #     print('执行打卡操作')
        # else:
        #     print('报错, 不具备打卡条件, 请检查手机状态')

        time.sleep(4)
        # 打卡按钮
        self.find_element_click(AppiumBy.ID, 'com.tencent.wework:id/bh6')
        print('打卡按钮')

        # 检查打卡结果
        # 有无弹窗
        # 有无显示打卡成功界面
        # if self.is_element_exist(AppiumBy.ID,AppiumBy.ID, 'xxxx'):
        #     print('打卡成功')
        # else:
        #     print('报错, 已执行打卡操作, 但好像没有打卡成功, 请检查手机状态')

        # print(is_element_exist(AppiumBy.ID, 'com.tencent.wework:id/bh6'))
        # print(is_element_exist(AppiumBy.ID, 'com.tencent.wework:id/bh777'))
        # print(is_element_exist(AppiumBy.ID, 'com.tencent.wework:id/bh888'))

        # 完成界面截屏

        # 任务完成后退出app
        self.close_app()

        # input('任意键退出')
        # input()
        print('程序结束')


if __name__ == '__main__':
    # com.tencent.wework.launch.LaunchSplashActivity# com.tencent.wework.launch.LaunchSplashActivity
    # deviceName = '150fc297'
    # deviceName = '192.168.11.195:5555'
    deviceName = '10.0.10.53:5555'
    appPackage = 'com.tencent.wework'
    appActivity = '.launch.LaunchSplashActivity'
    app = WeWorkSign(deviceName, appPackage, appActivity)
    app.main()