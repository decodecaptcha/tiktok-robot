import socket


def is_port_use(port, host='127.0.0.1'):
    """ 检查服务端口是否占用 """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, int(port)))
        s.shutdown(socket.SHUT_RDWR)
        return True
    except Exception as e:
        pass
    return False

print(is_port_use(5555, '192.168.11.195'))
# print(is_port_use(5555, '192.168.11.194'))
# print(is_port_use(5555))