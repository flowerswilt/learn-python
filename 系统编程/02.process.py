from multiprocessing import Process
import time
# os.fork()虽然能够开启子进程
# 但是它有个致命的缺点，无法跨平台
# 只能用于类unix系统中
# python中能够跨平台的开启子进程方式是使用Process类

# =====1=====
# 主进程等待子进程结束后，主进程才会结束
# 可以使用process实例的join()方法阻塞主进程代码
print('主进程开始')
def test():
    for i in range(5):
        print('-----test-----')
        time.sleep(1)

p = Process(target=test)

p.start()

p.join()

print('main')

# =====2=====
# 可以自定义类继承Process来完成新进程创建的需求
# 自定义类必须实现run方法
class My_Process(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        while True:
            print('------子进程开始------')
            time.sleep(1)

if __name__ == '__main__':

    p = My_Process()
    p.start()

