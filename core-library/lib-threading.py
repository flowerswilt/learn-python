import threading
import time, random

# threading模块用于管理单个进程中的多个线程

# 1.Thread对象
## 最简单的线程是使用目标函数实例化一个Thread对象，然后调用实例的start()方法


# def worker(num):
#     """thread worker function"""
#     print('Worker: %s' %num)
#
#
# threads = []
# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()

# 2.确定当前线程的名字
## 每个线程都有默认名字，也可以在实例化线程时为其设置name参数


def my_service():
    print('{} is starting'.format(threading.current_thread().getName()))
    time.sleep(random.randint(1, 3))
    print('{} is Exiting '.format(threading.current_thread().getName()))


def my_worker():
    print('{} is Starting'.format(threading.current_thread().getName()))
    time.sleep(random.randint(1, 3))
    print('{} is Exiting'.format(threading.current_thread().getName()))


def current_name():
    t_service = threading.Thread(name='my-service', target=my_service)
    t_worker = threading.Thread(name='my-worker', target=my_worker)
    t_temp = threading.Thread(target=my_service) # 线程具有默认名字

    t_service.start()
    t_worker.start()
    t_temp.start()


# 3.守护和非守护
## 默认情况下，程序需要等待所有线程全部执行完毕后，才会退出
## 在实例化线程时，如果设置参数daemon为true，那么程序就不会继续等待线程执行完毕


def daemon():
    """ 主进程不会等待这个线程执行完毕就会退出 """
    print('{} is Starting'.format(threading.current_thread().getName()))
    time.sleep(random.randint(1, 3))
    # 下面这句退出的语句根本就没有机会被执行
    print('{} is Exiting '.format(threading.current_thread().getName()))



def none_daemon():
    print('{} is Starting'.format(threading.current_thread().getName()))
    # time.sleep(random.randint(1, 3))
    print('{} is Exiting '.format(threading.current_thread().getName()))


def daemon_func():
    """主进程不会等待标记为daemon的线程结束就会退出"""
    t_daemon = threading.Thread(name='daemon', target=daemon, daemon=True)
    t_none_daemon = threading.Thread(name='none-daemon', target=none_daemon)

    t_daemon.start()
    t_none_daemon.start()

    # 如果非要等待标记为daemon的线程结束，可以使用join方法
    # t_daemon.join()


# 4.枚举所有线程
## threading 模块提供一个enumerate方法，枚举当前全部线程，包括主线程在内
def enum_worker():
    """ thread worker function """
    pause = random.randint(1, 5) / 10
    print('Sleeping %.2f' %pause)
    time.sleep(pause)
    print('end')


def enum_func():
    """ 枚举所有执行中的线程 """
    for i in range(3):
        t = threading.Thread(target=enum_worker)
        t.start()

    main_thread = threading.main_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        else:
            print('{} joining'.format(t.getName()))
            t.join()


# 5. 继承Thread
## 在启动的时候，Thread做了一些基本的初始化工作，然后调用了run方法，然后它调用了传入构造器的目标函数
## 可以创建一个子类，然后重写run方法，以达到创建子线程的目的
class MyThread(threading.Thread):
    def run(self):
        print('{} is running'.format(self.name))


def class_thread_func():
    for i in range(3):
        t = MyThread()
        t.start()


# 6.线程锁
## 线程间共享同一个全局变量环境
## 当多个线程同时修改一个全局变量时，就会造成全局变量污染
## 这种情况下，标准库提供了线程锁机制
g_num = 0


def thread_none_lock():
    global g_num
    for i in range(1000000):
        g_num += 1
    print('{} g_num = {}'.format(threading.current_thread().getName(), g_num))



def thread_with_lock(lock):
    global g_num
    for i in range(1000000):
        # 加锁
        lock.acquire()
        g_num += 1
        lock.release()
    print('{} g_num = {}'.format(threading.current_thread().getName(), g_num))


def thread_lock_func():
    # 实例化进程锁
    mutex = threading.Lock()
    t1 = threading.Thread(target=thread_with_lock, args=(mutex,))
    t2 = threading.Thread(target=thread_with_lock, args=(mutex,))
    t1.start()
    t2.start()

    time.sleep(3)
    global g_num
    # 在不使用线程锁的情况下，期望全局变量最终为200万，最终结果缺不固定
    # 增加线程锁后，最终结果成为了期望的200万
    print('----main---- g_num = {}'.format(g_num))


if __name__ == '__main__':

    # 确定线程名字demo
    # current_name()

    # 守护线程与非守护线程
    # daemon_func()

    # 枚举所有线程
    # enum_func()
    # class_thread_func()
    thread_lock_func()