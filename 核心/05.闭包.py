# 函数引用
def foo():
    print('我也不知道谁来调用我')

temp = foo # temp 引用了函数foo 的内存地址
print(temp) # 函数指针
temp() # temp 可以作为一个函数来调用

# 函数内部也可以定义函数

def bar():
    print('--外部函数--')
    def test():
        print('--内部函数--')

    test()

bar() # 输出: --外部函数-- --内部函数--

# 我们可以将内部函数作为返回值返回
# 我们知道一个函数执行后，函数内部的标识符会被解释器回收，当我们在一个函数内返回另一个函数时
# 一切都变得不同
def outer(number):
    def inner(numInner):
        print(number)
        print(numInner)

    return inner

f = outer(1)
f(2) # 输出 1 2
# 快看！！这就是闭包
# 闭包延长了外部函数标识符的生命周期
# 柯里化就是闭包的一种应用
