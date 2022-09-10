import subprocess


def check_adb_status(device_id="xxxxx"):
    out, err = subprocess.getstatusoutput("adb -s " + device_id + " get-state")

    if err == 0:
        if 'device' in out:
            print("[INFO] ADB is on")
            return True
        elif 'offline' in out:
            print("[WARNING] ADB device is dumb")
            return False
        else:
            print("[WARNING] ADB is abnormal: " + out)
    else:
        print("[WARNING] ADB is bad: " + err)
    return False


if __name__ == '__main__':
    check_adb_status(device_id="192.168.11.195:5555")
    check_adb_status(device_id="150fc297")
    
