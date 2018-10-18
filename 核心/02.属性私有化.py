"""
python中并没有其他面向对象中的public与private等概念
想要实现属性私有化，需要在属性💰添加__标识符
"""
class Test(object):
    def __init__(self):
        self.__num = 100

    """
    def getNum(self):
        return self.__num

    def setNum(self, newNum):
        self.__num = newNum

    num = property(getNum, setNum)
    """
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, newNum):
        self.__num = newNum


# t = Test()
# print(t.__num) # 解释器抛出 AttributeError 对象没有__num属性

# 在类的实例中，我们无法访问__修饰的属性，可以通过getter和setter方法访问
# t = Test()
# print(t.getNum()) # 输出100
# t.setNum(50) # 修改 __num的值
# print(t.getNum()) # 输出50 修改成功

# __双下划线修饰的属性，就类似于其他面向对象语言中的private
# python中不存在protected的概念

# 如果一直使用getter和setter的函数方式，好像有点儿麻烦，python提供了property函数来简化操作
# 在类中增加了property后，现在再来看
# 也可以使用property装饰器
t = Test()
print(t.num) # 100
t.num = 50 # 修改 __num 属性为50
print(t.num) # 50 修改成功