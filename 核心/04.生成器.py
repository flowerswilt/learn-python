"""
生成器
"""

# 第一种生成器创建方式 将列表生成式的[]括号改为()小括号
a_gen = (x*2 for x in range(10))
print(a_gen)

# 使用内置函数next取出生成器中的值
print(next(a_gen))
print(dir(a_gen)) # 内置函数next()其实调用的是生成器对象的__next__()方法

# 当取出最后一个生成器的值后，再次调用next会得到一个异常 StopIteration
# for循环可以优雅的处理边界情况
for a in a_gen:
    print(a)

# 第二种生成器创建方式：
# 一个函数内部出现yield关键字， 一个斐波那契序列的函数
def createNum():
    print('------start------')
    a, b = 0, 1
    for i in range(10):
        yield b
        a, b = b, a + b
    print('------stop------')

f_gen = createNum() # 返回一个生成器

for x in f_gen: # 用for循环来处理生成器取值
    print(x)

# 可以通过生成器的send()方法与生成器对象交互
def sendTest():
    i = 0
    while i < 5:
        temp = yield i
        print(temp)
        i += 1

send_gen = sendTest()
print(next(send_gen)) # 0
print(send_gen.send('temp接收这个信息')) # 输出: temp接收这个信息 1

# 需要注意的是，一个刚刚启动的生成器对象，在第一次next取值前，不应该send()消息，否则会得到一个TypeError异常
# 或者对于一个刚启动的生成器对象，使用send(None)方法

