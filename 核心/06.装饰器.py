"""
装饰器
    在不修改已实现代码的情况下，如何为现存代码增强功能
"""
# 现在我们想要在支付前进行一次确权
# 我们可以让这个认证函数接收一个函数参数
def permission(fun):
    def inner(*args, **kwargs):
        print('权限认证')
        if '权限认证通过':
            # fun()
            # 当被装饰函数有返回值,调用被装饰函数并返回
            return fun(*args, **kwargs)
        else:
            print('什么都不做')
    # 返回这个闭包函数
    return inner
# 假设我们有一个实现支付功能的函数
@permission
def aliPay():
    print('支付')

# 让支付函数指向具备权限认证的函数
# aliPay = permission(aliPay)

aliPay()

# 上面的代码就是一个非常简单的装饰器，没有参数，没有返回值
# python提供了一个简单的语法糖 @装饰器
# 可以替代 aliPay = permission(aliPay) 这行代码

# 当被装饰的函数有返回结果呢？
# 一定要在inner函数内返回被装饰函数的返回值

# 当被装饰函数有参数呢？
# inner函数接收参数，在inner内部传递给被装饰函数

# 可以使用多个装饰器来装饰一个函数
# 装饰器执行顺序从最后一个装饰器开始
# 来看个栗子吧
def w1(func):
    print('----正在装饰1----')
    def inner():
        print('----正在验证权限1--')
        func()
    return inner

def w2(func):
    print('----正在装饰2----')
    def inner():
        print('----正在验证权限2----')
        func()
    return inner

@w1
@w2
def fn():
    print('----fn----')

fn()

