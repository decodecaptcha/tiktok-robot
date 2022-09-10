# -*- coding: utf-8 -*-
import json
import datetime
import random
import string
import time
import time
from apscheduler.schedulers.blocking import BlockingScheduler
from loguru import logger

from ppadb.client import Client as AdbClient
from wework_sign import WeWorkSign

# --------------- 定时任务 (可修改) --------------- #
# 默认是每天的18：30 分执行任务(24小时制, 可选)
JOB_HOUR = 18
JOB_MINUTE = 30


print(r"""
 __      _______      _____  _ __| | __     __ _ _   _| |_ ___      ___(_) __ _ _ __  
 \ \ /\ / / _ \ \ /\ / / _ \| '__| |/ /    / _` | | | | __/ _ \    / __| |/ _` | '_ \ 
  \ V  V |  __/\ V  V | (_) | |  |   <    | (_| | |_| | || (_) |   \__ | | (_| | | | |
   \_/\_/ \___| \_/\_/ \___/|_|  |_|\_\    \__,_|\__,_|\__\___/    |___|_|\__, |_| |_|
                                                                          |___/                                  
author: aiden2048                                     
address: https://github.com/aiden2048
""")


def read_file(abspath):
    try:
        with open(abspath, 'r') as f:
            text = f.read()
            return text
    except Exception as e:
        logger.debug(e)
        return None


def write_file(abspath, data: str):
    try:
        with open(abspath, 'w') as f:
            f.write(data)
    except Exception as e:
        logger.debug(e)
        return None


def Listen_on_connection(host, port):
    while 1:
        client = AdbClient()
        response = client.remote_connect(host, port)
        time.sleep(0.5)
        if response:
            break
    return True


host = '192.168.11.195'
port = 5555
deviceName = f'{host}:{port}'
appPackage = 'com.tencent.wework'
appActivity = '.launch.LaunchSplashActivity'

def login():
    pass


def job():
    # 每日任务
    logger.debug("每日任务已开启...")


    # # 签到
    # logger.debug('"签到"任务已开启...')
    # try:
    #     pass
    #     logger.debug('"每日签到"任务已完成...')
    # except Exception as e:
    #     logger.debug('"签到"任务失败, 需要重新登录, Error：', e)
    #     input()

    try:
        if Listen_on_connection(host, port):
            logger.debug(f'Connect {host}:{port} is successful.')

            app = WeWorkSign(deviceName, appPackage, appActivity)
            app.main()
        else:
            raise ConnectionError(f'{deviceName} ConnectionError.')
    except Exception as e:
        logger.debug("执行任务失败，Error：", e)
        input()

    logger.debug("每日任务, 已完成.")
    # tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    # strtomorrow = tomorrow.strftime('%Y-%m-%d')
    # logger.debug(f"下次执行时间：{strtomorrow} {JOB_HOUR}:{JOB_MINUTE}")


if __name__ == '__main__':
    # job()
    logger.debug("程序启动...")
    # if not read_file(COOKIE_FILE_PATH):
    #     logger.debug("登录状态: 检测到未登录...")
    #     login()
    logger.debug("登录状态: 检测到已登录")
    logger.debug(f"定时任务: 已开启...")
    logger.debug(f"执行时间: 每日 {JOB_HOUR}:{JOB_MINUTE}")
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=JOB_HOUR, minute=JOB_MINUTE)
    scheduler.start()
