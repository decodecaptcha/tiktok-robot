import datetime
import random
tokens = ['123456']
started_jobs = []


def get_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def sum_x_y(x, y):
    return x + y


def auto_sign(ip, port, token):
    # 检查令牌
    if token not in tokens:
        return {
            'status': '0',
            'msg': 'The token is invalid.',
            'ip': ip,
            'port': port,
            'token': token,
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    job_name = f'{ip}:{port}'
    print('目前正在运行的任务:', str(started_jobs))
    print(f'{job_name} 是否已在运行: {job_name in started_jobs}')

    # 检查重复任务
    if job_name in started_jobs:
        return {
            'status': '0',
            'msg': 'The device is already started.',
            'ip': ip,
            'port': port,
            'token': token,
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    print('创建新的进程, 执行任务')

    # 执行任务
    if not random.randint(0, 1):
        print('执行任务失败')
        return {
            'status': '0',
            'msg': 'The device is started fail.',
            'ip': ip,
            'port': port,
            'token': token,
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

    print('执行任务成功')
    started_jobs.append(job_name)

    return {
            'status': '1',
            'msg': 'The device is started successfully.',
            'ip': ip,
            'port': port,
            'token': token,
            'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }


# http://localhost:7777/wework/autosign?ip=192.168.11.195&port=5555&token=123456