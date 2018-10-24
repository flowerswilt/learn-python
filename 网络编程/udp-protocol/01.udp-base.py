import socket
"""
套接字编程: UDP篇
"""
# 创建UDP套接字
udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 创建套接字时的参数:
# 1. 参数一 用来确认地址族 AF_INET 表示ipv4 比较常用
# 2. 参数二 用来确认连接协议 SOCK_STREAM 代表tcp协议， SOCK_DGRAM 代表udp协议
udp_socket.bind(('127。0。0。1',8080)) # 绑定套接字到主机 参数为主机IP和端口组成的元组
print('----start 等待连接-----')
recv_data = udp_socket.recvfrom(1024) # 接收消息 此方法会阻塞程序，直至接收到消息，程序才会继续执行
# 参数说明:
# 接收一个数字类型的参数，此参数指示本次接收数据的大小为1024个字节
# 返回值说明:
# 接收到消息后，函数返回一个元组类型(bytes,address)
# bytes 是发送方传过来的数据
# address 是发送方的ip地址及端口号 类型为元组
print(recv_data)
print(recv_data[0].decode('utf-8'))
print(recv_data[1])
udp_socket.sendto("hello".encode('utf8'), recv_data[1]) # 回复消息


udp_socket.close() # 关闭套接字以释放资源
