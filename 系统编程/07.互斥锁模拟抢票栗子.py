from multiprocessing import Process, Lock
import time, os, json, random

# 剩余票数存储于当前目录db.json 文件
def search():
    "查询剩余票数函数"
    time.sleep(random.randint(1, 3))  # 进程休息，模拟网络访问延迟
    with open('db.json', mode='r', encoding='utf-8') as f:
        dic = json.load(f) # 加载数据
        if dic['count'] > 0:
            print('%s >>> 剩余票数为%s' %(os.getpid(), dic['count']))
        else:
            print('%s >>> 剩余票数为0' %(os.getpid()))


def get():
    "购票函数"
    with open('db.json', mode='r', encoding='utf-8') as f:
        dic = json.load(f)
        if dic['count'] > 0:
            dic['count'] -= 1
            time.sleep(random.randint(1, 3))
            with open('db.json', mode='w', encoding='utf-8') as f:
                json.dump(dic, f)
                print('%s 购票成功' %os.getpid())


def task(lock):
    search()
    lock.acquire()
    get()
    lock.release()


if __name__ == '__main__':

    mutex = Lock() # 实例化互斥锁

    for i in range(0, 10):
        p = Process(target=task, args=(mutex, ))
        p.start()

