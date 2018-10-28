# 函数
# 函数的定义：
#   函数是程序中可以复用的部件
#   它允许你为一个或者一些特定的语句起一个名字，通过这个名字，你可以随时随地调用这个语句块
# 函数的声明:
    # 关键字 def 声明一个函数
    # 小括号内可以传递给函数参数

def say_hello():
    # 属于该函数的语句块
    print('Hello World')

# 函数的调用
say_hello()
say_hello() # 再次调用

# 函数的参数:
    # 函数的参数就是你调用函数时提供给函数的值
    # 定义函数时括号内的参数叫做形参
    # 调用函数时括号内的参数叫做实参

def print_max(a, b):
    "接收两个数字，打印最大的那个数"
    if a > b:
        print(a, 'is maximum')
    elif a < b:
        print(b, 'is maximum')
    else:
        print(a, 'is equal to ', b)

print_max(3, 5)

# 局部变量
    # 当在函数内部声明变量时，这些变量只在函数内部有效。
    # 变量名对于函数而言，是局部的，我们称之为作用域
    # 从变量被定义的地方开始，所有的变量都具有作用域
    # 即声明变量时所处的语句块

x = 50 # 我们可以将变量x视为全局变量，它声明于这个模块的全局作用域

def func(x):
    print('x is ', x)
    x = 2 # 覆盖全局变量
    print('Changed local to ', x)

func(x)
print('x is still ', x)

# 函数修改全局变量
    # 在函数内部修改全局变量，必须使用global语句

def func_global():
    global x # 使用上面声明的全局变量x
    print('x is ', x)
    x = 2
    print('Changed global x to ', x)

func_global()
print('Value of x is ', x) # 2 可以看到全局变量已被修改

# 默认参数
    # 函数调用时所传递的参数必须与声明时的参数个数一致
    # 当某些参数期望是可选的话，可以在声明时使用默认参数值
    # 默认参数值必须是不可变类型的值
    # 同时，具备默认值的参数声明顺序永远位于普通参数后面
    # 意即声明形参时，应该先声明没有默认值的参数，然后才是有默认值参数

def say(message, times=1):
    print(message * times)

say('Hello') # 输出 Hello
say('World ', 5) # 输出 World World World World World

# 关键字参数
    # 如果一个函数需要多个参数，而你只想指定其中一部分
    # 那么可以通过为这些参数命名来为它们赋值
    # 这样做，可以不必担心参数位置

def func_keywords(a, b=5, c=10):
    print(a, 'is ', a, 'and ', b, 'is', b, 'and ', c, 'is ', c)

func_keywords(3)
func_keywords(b = 4, a = 1)
func_keywords(24, c = 25)

# 上面三种调用方式都不会报错

# 可变参数
    # 如果需要定义一个可以接收任意参数的函数，那么就需要用到可变参数

def total(a = 10, *number, **phone_book):
    print('a is ', a)

    for single_item in number:
        print('single item', single_item)

    for first_part, second_part in phone_book.items():
        print(first_part, second_part)

total(10, 1, 2, 3, jack = 1123, john = 2231, inge = 1560)

"""
    输出:
        a is  10
        single item 1
        single item 2
        single item 3
        jack 1123
        john 2231
        inge 1560
"""

# return 语句
    # return语句用于从一个函数返回(意即跳出这个函数)
    # return 可以返回一个值，也可以不返回值
    # 当一个函数没有任何return语句时，该函数执行完毕会默认返回一个None

def function_return(x, y):
    "接收两个数字，返回最大值"
    if x > y:
        return x
    elif x < y:
        return y
    else:
        return 'The numbers are equal!'

print(function_return(3, 4)) # 4
print(function_return(2, 2)) # The numbers are equal!

# DocString
    # 一个函数体的第一行字符串就是这个函数的docstring
    # 用于解释说明该函数功能
    # 比如查看function_return函数的docstring
print(function_return.__doc__) # 接收两个数字，返回最大值