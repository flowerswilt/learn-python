import socket
from threading import Thread

def receive_thread():
    "接收数据处理线程"
    while True:
        data = udp_socket.recvfrom(1024)
        print(data)
        print('from server %s :' %(str(data[1])), end=' ')
        print(data[0].decode('utf-8'))

def send_thread():
    "发送数据处理线程"
    while True:
        data = input('请输入消息内容：>>>')
        udp_socket.sendto(data.encode('utf-8'), (address, int(port)))

# udp全局变量
udp_socket = None
address = "" # 全局接收方ip地址
port = 0 # 全局接收方端口

def main():
    "主线程"
    global udp_socket
    global address
    global port

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    address = input('请输入接收方地址: ').strip()
    port = input('请输入接收方端口号: ').strip()

    tr = Thread(target=receive_thread)
    ts = Thread(target=send_thread)

    tr.start()
    ts.start()

    tr.join()
    ts.join()

if __name__ == '__main__':
    main()