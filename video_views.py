# -*- coding: utf-8 -*-
# @Author : 艾登Aiden
# @Email : aiden2048@qq.com
# @Date : 2022-02-18

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
    # 'adbExecTimeout': 60000,
    # 'app': '/path/to/the/downloaded/ApiDemos-debug.apk',
    # 'unicodeKeyboard':True,
    # 'resetKeyboard':True,
    # 'newCommandTimeout':6000,
    # 'automationName':'UiAutomator2'
}

driver = webdriver.Remote(server, desired_caps)
wait = WebDriverWait(driver, 1000)
width = driver.get_window_size().get('width')
height = driver.get_window_size().get('height')
print('设备分辨率: ', width, height)


def is_load_complete():
    """等待关注按钮显示, 即加载完成, 可滑动"""
    follow_id = 'com.zhiliaoapp.musically:id/bdi'
    wait.until(EC.presence_of_element_located(
        (By.ID, follow_id)))
    return

# def is_video_playing():
#     """判断视频是否开始播放"""
#     video_playing_id = 'com.zhiliaoapp.musically:id/dxc'
#     try:
#         driver.find_element(by=By.ID, value=video_playing_id)
#         return True
#     except:
#         return False

def click_pause():
    """在播放页, 点击暂停"""
    time.sleep(0.5)
    x = width / 2
    y = height / 2
    try:
        driver.tap([(x, y)], 100)
        return
    except Exception as e:
        # print(e)
        return click_pause() # 重试

def is_video_pause():
    """判断是否出现暂停按钮"""
    time.sleep(0.5)
    video_pause_xpath = '//android.widget.FrameLayout[@resource-id="com.zhiliaoapp.musically:id/cs5"]/android.widget.ImageView'
    try:
        return driver.find_element(by=By.XPATH, value=video_pause_xpath).is_enabled()
    except Exception as e:
        return False


def video_scroll_down():
    """向下滑动"""
    x = width / 2
    starty = height * 0.75
    endy = height * 0.20
    driver.swipe(x, starty, x, endy, 500)
    print('Video_scroll_down...')
    return

def search_username(username):
    """
    通过搜索账号查找用户
    刷播放量逻辑
    param username: 目标账号
    param total: 刷量次数
    """
    # 点击搜索入口
    search_xpath = '//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ImageView[2]'
    wait.until(EC.presence_of_element_located(
        (By.XPATH, search_xpath))).click()

    # 显示输入框, 输入目标账号
    input_id = 'com.zhiliaoapp.musically:id/b4u'
    wait.until(EC.presence_of_element_located((By.ID, input_id))).send_keys(username)
    
    # 点击搜索按钮
    search_button_id = 'com.zhiliaoapp.musically:id/fm7'
    wait.until(EC.presence_of_element_located(
        (By.ID, search_button_id))).click()

    # 显示搜索结果, 点击第一个
    search_button_id = 'com.zhiliaoapp.musically:id/ce5'
    wait.until(EC.presence_of_element_located(
        (By.ID, search_button_id))).click()
    return

def click_index_video():
    """点击主页第一个视频"""
    video1_id = 'com.zhiliaoapp.musically:id/fy9'
    wait.until(EC.presence_of_element_located(
        (By.ID, video1_id))).click()

def follow_video():
    """关注模块"""
    follow_id = 'com.zhiliaoapp.musically:id/bdi'
    wait.until(EC.presence_of_element_located(
        (By.ID, follow_id))).click()
    return

def like_video():
    """喜欢模块"""
    # 点击喜欢
    like_id = 'com.zhiliaoapp.musically:id/as5'
    wait.until(EC.presence_of_element_located(
        (By.ID, like_id))).click()
    return

def comment_video():
    """评论模块"""
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
    """转发模块"""
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

def run_count_views(username:str, total:int):
    """
    刷播放量逻辑
    param username: 目标账号
    param total: 刷量次数
    """
    print('已进入 TikTok 主界面...')
    # total = 10
    # 暂停的尝试次数, 一直点击, 直到出现暂停按钮为止
    retry_time = 100
    search_username(username)
    for i in range(1, total + 1):
        click_index_video()
        print("显示目标账号主页, 点击第一个视频...")

        for _ in range(retry_time):
            click_pause()
            if is_video_pause():
                print(f"第 {i} 次播放, 暂停成功")
                break
            else:
                print(f"第 {i} 次播放, 视频加载中...")

        back_page()
        # video_scroll_down()

    time.sleep(10)
    close_app()


if __name__ == '__main__':

    st = time.time()

    total = 50
    # 首次搜索的用户名
    username = 'naturewildly'
    run_count_views(total)

    use_time = int(time.time() - st)
    print(f"程序结束, 总用时: {use_time}s, 平均每次: {use_time / total}s")