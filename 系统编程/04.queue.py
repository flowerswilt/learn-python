from multiprocessing import Queue, Process, Manager, Pool, JoinableQueue
import time
import random
# Queue 用于进程间通信
# 这是一个队列，具备先进先出的特性
# qsize() : 查看队列内的数据量
# put() : 将数据推入队列
# get() : 从队列中取出一条数据
# empty(): 判断队列是否为空
# full(): 判断队列是否已满

# q = Queue(3) # 初始化一个队列，参数表示该队列可以推入几条数据
# q.put('111')
# q.put('222')
# q.put('333')
# # q.put('4444') # 这条语句会阻塞程序，因为队列已满，除非有其他进程从队列取出了其他数据
#
# print(q.get()) # 111  先进先出
# print(q.get()) # 222  先进先出
# print(q.get()) # 333  先进先出
# print(q.get()) # 这条语句会阻塞进程，因为队列已空，除非有其他进程向此队列推入其他数据

# 两个进程间通信的小栗子
# def write(q):
#     """向队列写数据的函数，接收一个队列"""
#     for value in ['csq', 'pyy', 'zxmy', 'ykm']:
#         if q.full(): # 判断队列是否已满
#             break
#         else:
#             print('%s被推入队列' %value)
#             q.put(value)
#
# def read(q):
#     """从队列读取数据，接收一个队列"""
#     while True:
#         if q.empty(): # 判断队列是否为空
#             break # 条件成立，结束循环
#         else:
#             value = q.get()
#             print('%s from queue' %value)
#
# if __name__ == '__main__':
#
#     q = Queue(4)
#     w_process = Process(target=write, args=(q,))
#
#     w_process.start()
#     w_process.join()
#
#     r_process = Process(target=read, args=(q,))
#
#     r_process.start()
#     r_process.join()
#
# # 如果使用进程池Pool，需要使用Manager来创建队列
# if __name__ == '__main__':
#
#     print('----pool----进程通信开始')
#     queue = Manager().Queue(4) # 使用manager来初始化队列
#     pool = Pool(2)
#     pool.apply(write, (queue,)) # 阻塞式进程
#     pool.apply(read, (queue,))
#     pool.close()
#     pool.join()
#     print('----pool----进程通信结束')

# 生产者消费者模型
# 我们无法确保消费者是否真正完全取完了生产者所生产的数据
# 这个时候就要结合守护进程和JoinableQueue
# 消费者队列需要成为守护进程
# 这个队列可以确保共享队列中的所有数据全部被消费者消费完毕
# 这样当主进程结束时，就会结束消费者线程

def consumer(q):
    "接收一个共享队列"
    while True: # 无限循环，从共享队列取数据
        res = q.get() # 从队列取数据
        time.sleep(random.randint(1,3))
        print('消费者---> 消费了%s' %res)
        q.task_done()


def producer(q, name):
    "接收一个共享队列，所有生产出的数据全部放入共享队列"
    for i in range(1,4):
        time.sleep(random.randint(1, 2))
        q.put(name + str(i))
        print('生产者生产了%s' %((name + str(i))))


if __name__ == '__main__':

    q = JoinableQueue()

    p1 = Process(target=producer, args=(q, '米饭'))
    p2 = Process(target=producer, args=(q, '稀饭'))
    p3 = Process(target=producer, args=(q, '面条'))

    c1 = Process(target=consumer, args=(q,))
    c2 = Process(target=consumer, args=(q,))

    # 将消费者进程当作守护进程，主进程结束时，结束消费者进程
    c1.daemon = True
    c2.daemon = True

    p1.start()
    p2.start()
    p3.start()

    c1.start()
    c2.start()

    # 确保所有生产者进程执行完毕
    p1.join()
    p2.join()
    p3.join()

    # 确保队列所有数据被消费者取完
    q.join()

    print('---- main end ----')
