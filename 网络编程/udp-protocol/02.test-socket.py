import socket

udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udp_socket.sendto('hello from test.py'.encode('utf-8'), ('127.0.0.1', 8080))

recv_data = udp_socket.recvfrom(1024)
print(recv_data)
print(recv_data[0].decode('utf-8'))
print(recv_data[1])