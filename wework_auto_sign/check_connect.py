# import ppadb
import time
from ppadb.client import Client as AdbClient
# from ppadb.device import Device
# from ppadb.connection import Connection



def Listen_on_connection(host, port):
    while 1:
        client = AdbClient()
        response = client.remote_connect(host, port)
        time.sleep(0.5)
        if response:
            break
    return True

# host = '192.168.11.195'
host = '10.0.10.53'
port = 5555
if Listen_on_connection(host, port):
    print('connect successful !!!')



# device = client.device("192.168.11.195:5555")
# result = device.shell("echo hello world !")
# result = device.shell("echo hello world !")
# print(result)



# cmd = "host:devices"
# result = client._execute_cmd(cmd)
# print(result)

# print(device)

# if not isinstance(device, Device):
#     print('失败')
# else:
#     print('成功')

# device.shell("echo hello world !")
# client.remote_connect(host="192.168.11.195", port=5555)
# Disconnect all devices
# client.remote_disconnect()

##Disconnect 172.20.0.1
# client.remote_disconnect("192.168.11.195")
##Or
# client.remote_disconnect("192.168.11.195", 5555)