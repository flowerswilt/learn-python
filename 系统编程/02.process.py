from multiprocessing import Process, Lock
import time
import random
# os.fork()虽然能够开启子进程
# 但是它有个致命的缺点，无法跨平台
# 只能用于类unix系统中
# python中能够跨平台的开启子进程方式是使用Process类

# Process开启子进程的两种方式

# 第一种方式
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#     print('%s was done' %name)
#
#
# if __name__ == '__main__':
#
#     print('----main start----')
#
#     p = Process(target=task, args=('zhq',)) # 创建子进程 传递任务参数
#     p.start() # 启动子进程
#
#     print('----main end----')
"""
输出:
    ----main start----
    ----main end----
    zhq is running
    zhq was done
从输出可以看出来，主进程在子进程启动后，继续执行后续代码
子进程不会阻塞主进程，当子进程结束后，整个程序才会结束
"""

# 第二种方式
# class MyProcess(Process):
#     "自定义进程类，继承自标准库中的Process类，覆盖run方法"
#     def __init__(self, name):
#         Process.__init__(self)
#         self.name = name
#
#     def run(self):
#         print('%s is running' %self.name)
#         time.sleep(3)
#         print('%s was done' %self.name)
#
#
# if __name__ == '__main__':
#
#     print('----main start----')
#
#     p = MyProcess('zhq')
#     p.start()
#     p.join()
#
#     print('----main end----')

# 不添加join方法时，与第一种方式的输出一样
# 如果希望阻塞主线程，那么直接调用join()方法
"""
输出:
    ----main start----
    zhq is running
    zhq was done
    ----main end----
可以看到，主进程会被阻塞，等待子进程执行完毕
"""

# 注意: 进程之间的内存空间相互隔离
# x = 100
#
# def task():
#     "子进程修改全局变量"
#     print('----子进程开始----')
#     time.sleep(3)
#     global x
#     x = 0
#     print('子进程中全局变量的值变为%s' %x)
#     print('----子进程结束----')
#
# if __name__ == '__main__':
#     print('----主进程开始----')
#     print(x) # 先看一下全局变量x的值
#     p = Process(target=task) # 创建子进程
#     p.start() # 启动子进程，子进程内部会修改全局变量x的值
#     p.join() # 阻塞主进程，等待子进程结束
#     print('子进程结束后，全局变量x的值为%s' %x)
#     print('----主进程结束----')

"""
    输出：
        ----主进程开始----
        100
        ----子进程开始----
        子进程中全局变量的值变为0
        ----子进程结束----
        子进程结束后，全局变量x的值为100
        ----主进程结束----
    从上面输出可以看出，子进程修改了全局变量，但主进程的全局变量并不受影响
"""

# Process实例的其他属性

# 1. process.name 进程默认名字
# 2. process.terminate 终止子进程
# 3. process.is_alive 判断子进程是否还活着,注意有延时
# 4. process.pid 子进程的pid号

# 僵尸进程与孤儿进程
# 当主进程始终不结束，而子进程已经结束时，所有由主进程开启的进程都会成为僵尸进程，频繁开启此类进程，将会造成资源浪费
# 当主进程运行完毕，而子进程尚未结束，所有由主进程开启的进程都会成为孤儿进程，这些孤儿进程将由系统进程接收
# 解决孤儿进程的方法有一种叫做守护进程
# def task(name):
#     print('%s is running' %name)
#     time.sleep(3)
#
#
# if __name__ == '__main__':
#     print('----主进程start----')
#     process = Process(target=task, args=('zhq',))
#     process.daemon = True # 开启守护进程
#     process.start()
#     print('----主进程end----')


"""
    输出:
        ----主进程start----
        ----主进程end----
    从输出可以看到，子进程根本就没有来得及执行
    守护进程会在主进程结束的时候，不管子进程有没有执行完毕，都会被操作系统回收
"""

# 在不通过调用join()方法时，子进程的执行顺序是无法预测的
# join()方法会导致主进程阻塞，降低程序执行效率
# 子进程共同使用同一个系统资源时，会出现抢占错乱的问题
# 这就是互斥锁的用途
# multiprocessing 模块提供了Lock类，也就是互斥锁
mutex = Lock() # 实例化一个互斥锁

def task1(lock):
    "由于子进程是互不相同的全局环境，所以我们要在子进程中接收互斥锁,好让各个子进程拿到同一个锁"
    lock.acquire() # 上锁
    print('--task1 start----')
    time.sleep(random.randint(1, 3)) # 随机休息，模拟任务执行
    print('----task1 end----')
    lock.release() # 解锁 子进程一定要解锁，否则其他子进程无法重新上锁


def task2(lock):
    lock.acquire()
    print('----task2 start----')
    time.sleep(random.randint(1, 3))
    print('----task2 end----')
    lock.release()


def task3(lock):
    lock.acquire()
    print('----task3 start----')
    time.sleep(random.randint(1, 3))
    print('----task3 end----')
    lock.release()


if __name__ == '__main__':

    print('----main start ----')

    p1 = Process(target=task1, args=(mutex,)) # 将互斥锁传入子进程, 确保所有子进程共用一个互斥锁
    p2 = Process(target=task2, args=(mutex,)) # 将互斥锁传入子进程
    p3 = Process(target=task3, args=(mutex,)) # 将互斥锁传入子进程

    p1.start()
    p2.start()
    p3.start()

    print('----main end ----')
