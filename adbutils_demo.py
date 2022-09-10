import adbutils

# adb = adbutils.AdbClient(host="192.168.11.195", port=5555)
# for info in adb.list():
#     print(info.serial, info.state)
#     # <serial> <device|offline>

# # only list state=device
# print(adb.device_list())

# Set socket timeout to 10 (default None)
adb = adbutils.AdbClient(host="192.168.11.195", port=5555, socket_timeout=5)
print(adb.device_list())