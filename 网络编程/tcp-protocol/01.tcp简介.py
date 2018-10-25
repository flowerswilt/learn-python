# TCP协议是有连接的传输协议
# 相对于UDP而言，它的传输更安全，因为具备数据校验
# 但是速度会比UDP慢
# 基本步骤:
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # sock.stream 表示tcp协议

server_socket.bind(('127.0.0.1', 8080)) # 绑定IP地址和端口号，客户端根据这个信息连接

server_socket.listen(5) # 启动tcp服务器，监听8080端口

client_socket,client_address = server_socket.accept() # 阻塞服务器代码,接收客户请求，返回一个元组，
                                                      # 包含新的socket连接和客户IP地址，用于处理本此请求

client_socket.recv(1024) # 接收来自客户端的数据， 同样会阻塞程序运行

client_socket.send() # 回复本次连接的客户端

client_socket.close() # 关闭本次连接

# 上面基本上就是tcp服务器的常用方法
# 可以看出，server_socket专门用于接收客户端请求
# client_socket专门用于处理客户端请求
# 或者这也可以看做是生产消费者模式？
