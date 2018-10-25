import sys
"""
基础部分依据畅销书<<python编程: 从入门到实践>>内容添加
可以把它当成一个简单的python笔记吧
"""
# 首先python是跨平台的，它可以运行在绝大多数的主流机器上
# 它的执行依靠一个名称为interpreter（解释器）的程序
# 目前主要版本是 python2.x 和python3 两者不兼容
# Linux 及 Mac OS 系统自带python解释器

def print_info():
    print(sys.version) # 输出当前python版本
    print(sys.platform) # 输出当前系统环境

print_info()

# 命令行启动python解释器
# python3 name.py args
# 退出解释器
# quit() # python2无效
# exit() # python2

# 传递参数给解释器
# import sys
# 在调用python解释器时，脚本名和附加参数会存入sys.args
# 这是一个列表sys.args[0] 存储脚本名称
# sys.args[1] 及以后，存储实际存储的参数
