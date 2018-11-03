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

# tcp 注意事项
## 1. 服务器端一般需要绑定IP和端口
## 2. socket.listen()方法可将套接字从主动变为被动模式，这是客户端和服务端的最大区别
## 3. 客户端需要socket.connect()方法才能链接到服务端，先链接后发送，是udp和tcp的最大区别
## 4. 当一个客户端链接到服务端时，服务端会返回一个新的套接字，这个套接字标识链接的客户端，通过这个标识服务端可以与客户端通信
## 5. 当客户端的套接字调用close()方法后，服务端的recv()方法会解阻塞，并收到一个0的返回值，可以通过这个返回值来识别客户端是否已经下线

