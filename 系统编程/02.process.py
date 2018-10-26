from multiprocessing import Process
import time
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