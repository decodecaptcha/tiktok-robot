# -*- coding: utf-8 -*-
# @Author : 艾登Aiden
# @Email : aidenlen@163.com
# @Date : 2021-02-18

import random
from appium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


server = 'http://localhost:4723/wd/hub'
# vivoY51 真机
desired_caps = {
    'platformName': 'Android',
    # 'platformVersion': '5.1.1',
    'deviceName': 'c25e9c86',
    'appPackage': 'com.zhiliaoapp.musically', # com.zhiliaoapp.musically/com.ss.android.ugc.aweme.splash.SplashActivity
    'appActivity': 'com.ss.android.ugc.aweme.splash.SplashActivity', # 启动成功
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

USERID = 'anusharazdan'

def is_load_complete():
    # 等待关注按钮显示, 即加载完成, 可滑动
    follow_id = 'com.zhiliaoapp.musically:id/bdi'
    wait.until(EC.presence_of_element_located(
        (By.ID, follow_id)))
    return

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


def search_username():
    """通过搜索账号查找用户"""
    # 点击搜索入口
    search_xpath = '//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView[2]'
    wait.until(EC.presence_of_element_located(
        (By.XPATH, search_xpath))).click()

    # 显示输入框, 输入目标账号
    input_id = 'com.zhiliaoapp.musically:id/b4u'
    wait.until(EC.presence_of_element_located((By.ID, input_id))).send_keys(USERID)
    
    # 点击搜索按钮
    search_button_id = 'com.zhiliaoapp.musically:id/fm7'
    wait.until(EC.presence_of_element_located(
        (By.ID, search_button_id))).click()

    # 显示搜索结果, 点击第一个
    search_button_id = 'com.zhiliaoapp.musically:id/ce5'
    wait.until(EC.presence_of_element_located(
        (By.ID, search_button_id))).click()

    # 显示目标账号主页, 点击第一个视频
    video1_id = 'com.zhiliaoapp.musically:id/fy9' # 'com.zhiliaoapp.musically:id/aj1'
    wait.until(EC.presence_of_element_located(
        (By.ID, video1_id))).click()
    return


def follow_video():
    """发起关注"""
    # 点击关注
    follow_id = 'com.zhiliaoapp.musically:id/bdi'
    wait.until(EC.presence_of_element_located(
        (By.ID, follow_id))).click()
    return

def like_video():
    """发起喜欢"""
    # 点击喜欢
    like_id = 'com.zhiliaoapp.musically:id/as5'
    wait.until(EC.presence_of_element_located(
        (By.ID, like_id))).click()
    return

def comment_video():
    """发起评论"""
    # 点击评论
    comment_id = 'com.zhiliaoapp.musically:id/af1'
    wait.until(EC.presence_of_element_located(
        (By.ID, comment_id))).click()

    # 显示评论框, 输入评论内容
    # 遇到问题: 发现 send_keys 输入内容后不显示发送按钮, 需要额外点击 @按钮 才显示发送按钮
    input_content = 'hello world'

    # input_comment_id = 'com.zhiliaoapp.musically:id/aep'
    # wait.until(EC.presence_of_element_located((By.ID, input_comment_id))).send_keys(input_content)

    input_comment_xpath = '//android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.View/android.widget.EditText'
    wait.until(EC.presence_of_element_located((By.XPATH, input_comment_xpath))).send_keys(input_content)

    # 点击@按钮, 显示发送按钮
    aite_button_id = 'com.zhiliaoapp.musically:id/c32'
    wait.until(EC.presence_of_element_located((By.ID, aite_button_id))).click()
    wait.until(EC.presence_of_element_located((By.ID, aite_button_id))).click()

    # 点击发送评论
    send_button_id = 'com.zhiliaoapp.musically:id/afk'
    wait.until(EC.presence_of_element_located(
        (By.ID, send_button_id))).click()
    return

def forward_video():
    """点击转发"""
    # 点击转发入口
    forward_id = 'com.zhiliaoapp.musically:id/eeh'
    wait.until(EC.presence_of_element_located(
        (By.ID, forward_id))).click()

    # 显示转发框, 选择转发对象
    select_forward_id = 'com.zhiliaoapp.musically:id/tm'
    wait.until(EC.presence_of_element_located(
        (By.ID, select_forward_id))).click()

    # 点击转发
    send_forward_id = 'com.zhiliaoapp.musically:id/ebs'
    wait.until(EC.presence_of_element_located(
        (By.ID, send_forward_id))).click()
    return

def back_page():
    """页面后退一步"""
    driver.back()
    return


def close_app():
    """关闭APP"""
    driver.close_app()
    return


if __name__ == '__main__':
    is_load_complete()
    print('已进入 TikTok 主界面...')
    for _ in range(3):
        video_to_swipe()
        time.sleep(1)

    follow_video()
    like_video()
    comment_video()
    time.sleep(1)
    back_page() # 退出评论界面
    forward_video()
    print('一键四连成功...')
    back_page()

    time.sleep(1)
    close_app()
    print('程序结束')
