# subprocess
## 目的: 开始与其他进程交互

import subprocess

# 1. 运行外部命令
completed = subprocess.run(['ls', '-l']) # 返回Completed实例

print(type(completed), completed.returncode)

## returncode是程序退出码，0为命令执行成功，其他非0表示有错误产生
## 调用者应该检查退出码来判断程序是否出错
## 如果希望在程序出错时抛出异常，可以在调用run方法时，设置check为true

try:
    subprocess.run(['false'],check=True)
except subprocess.CalledProcessError as error:
    print(error) # Command '['false']' returned non-zero exit status 1.


# 2. 捕获输出
## 由run方法启动的进程，标准输出被绑定在了父进程上
## 这意味着run方法的输出只能打印在控制台，而无法捕获进行后续处理
## 可以通过设置stdout、stderror来捕获输出

completed = subprocess.run(['ls', '-l'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print('退出码: {}'.format(completed.returncode))
print('总计 {} 字节被输出'.format(len(completed.stdout)))
print('Error: '.format(completed.stderr))



