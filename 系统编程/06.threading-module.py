from threading import Thread, Lock
import time
"""
threading 模块

"""
# 创建线程的两种方式一: 自定义继承自Thread的类
# class MyThread(Thread):
#     def run(self):
#         for i in range(3):
#            time.sleep(1)
#            msg = "I'm " + self.name + "@" + str(i) # name 属性中保存的是当前线程的名字
#            print(msg)
#
#
# if __name__ == '__main__':
#     t1 = MyThread()
#     t2 = MyThread()
#     t1.start()
#     t2.start()

# 创建线程的两种方式二：实例化Thread类
#
# def task():
#     print('-----')
#     time.sleep(1)
#
# for i in range(3):
#     # 实例化三个线程
#     p = Thread(target=task)
#     p.start()

# 多线程共享全局变量
g_num = 0

# def task1():
#     global g_num
#     for i in range(1000000): # 循环100万次
#         g_num += 1
#
# def task2():
#     global  g_num
#     for i in range(1000000):
#         g_num += 1
#
# p1 = Thread(target=task1)
# p1.start()
# p2 = Thread(target=task2)
# p2.start()
#
# time.sleep(3) # 等待线程结束
#
# print(g_num)  # 数据发生了非预期的改变，由于两个线程同时修改全局变量，导致运算结果不是预期结果

# 互斥锁解决多线程全局变量修改问题
mutex = Lock() # 创建一个互斥锁

def task1():
    global g_num
    for i in range(1000000):
        mutex.acquire() # 锁定全局变量修改语句
        g_num += 1
        mutex.release() # 释放锁

def task2():
    global  g_num
    for i in range(1000000):
        mutex.acquire() # 锁定全局变量修改语句
        g_num += 1
        mutex.release() # 释放锁

p1 = Thread(target=task1)
p2 = Thread(target=task2)

p1.start()
p2.start()

time.sleep(5) # 等待线程结束

print('最终结果%s' %g_num) # 2000000 最终结果符合预期

