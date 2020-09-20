import socket
# tcp连接
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# AF_INET指定使用IPv4协议，如果要用更先进的IPv6，就指定为AF_INET6。SOCK_STREAM指定使用面向流的TCP协议
# 建立连接:
s.connect(('www.sina.com.cn', 80))
