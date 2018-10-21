import os
import time

# 可以通过os 模块的fork方法来创建一个新的进程
# fork()的返回值为非0（主进程）和0（子进程）
# 通过判断返回值来交替执行父子进程
# 此方法适用于Linux、Mac OS 等类unix系统
# 通过os.getpid()及getppid()方法可以明显的看到
# ret == 0 的进程，父进程为ret != 0 的进程

ret = os.fork()

if ret == 0:
    while True:
        print('-----1-----', os.getpid(), os.getppid())
        time.sleep(1)
else:
    while True:
        print('-----2-----', os.getpid(), os.getppid())
        time.sleep(1)