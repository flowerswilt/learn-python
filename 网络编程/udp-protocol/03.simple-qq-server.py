import socket
from threading import Thread
# 简单全双工udp聊天程序服务器端
# 多线程实现

def receive_data():
    "数据接收线程"
    while True:
        data = udp_socket.recvfrom(1024)
        global dest_address
        dest_address = data[1]
        print('from %s >>>' %(data[1][0]), end='')
        print(data[0].decode('utf-8'))
def send_data():
    "数据发送线程"
    while True:
        if dest_address:
            data = input('请输入消息: ').strip()
            udp_socket.sendto(data.encode('utf-8'), dest_address)

# 全局变量
udp_socket = None
dest_address = None # 接收方地址和端口

def main():
    "主线程"
    global udp_socket
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # 创建套接字
    udp_socket.bind(('127.0.0.1', 8080))
    # 开启线程
    receive_thread = Thread(target=receive_data)
    send_thread = Thread(target=send_data)

    receive_thread.start()
    send_thread.start()

    receive_thread.join()
    send_thread.join()


if __name__ == '__main__':
    main()