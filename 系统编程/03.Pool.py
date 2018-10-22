from multiprocessing import Pool
import time, random, os
# 进程池
# ====1====
def worker(msg): # 定义一个工作函数
    t_start = time.time()
    print('%s开始执行,进程号为%s' %(msg, os.getpid()))
    time.sleep(random.randint(1, 3)) # 进程随机休息一段时间
    t_stop = time.time()
    print('%s进程执行了%0.2f' %(os.getpid(), t_start - t_stop))

po = Pool(3)  # 初始化一个进程池，最大进程数为3，超过3个进程后，其他进程需要等待

for i in range(0, 10):
    po.apply_async(worker, (i,)) # 创建10个进程，依次放入进程池执行

print('-------start--------')
po.close() # 关闭进程池，进程池不再接收新的进程
po.join() # 等待子进程全部结束
print('-------end--------')
