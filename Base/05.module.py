# 模块
## 对于代码的重用，我们用function解决
## 那么，如何重用function呢？
## python使用模块解决
## 可以把单一的一个以py结尾的文件看做是一个模块，这个文件内可以声明多个函数以供程序使用

# 模块的查找
import sys

print(sys.path)

## 类似于sys这种模块，属于python内置模块
## 所有非内置模块，那么python就会按照sys.path中列出的目录来查找模块
## 模块只会被python解释器初始化一次

print(__name__)
## 每个模块都有一个名字
## 当一个模块作为执行入口时，模块名字为main
## 当一个模块作为导入执行时，模块名字默认为文件名
if __name__ == '__main__':
    print('此文件作为独立文件运行')
else:
    print('此文件被导入执行')

## 内置的dir函数可以列出模块内部的所有函数、类和变量
## 不传参数的dir函数可以列出当前模块的所有标识符
print(dir())
print(dir(sys))