# 变量
# python 属于弱类型语言
# 但是变量必须先定义(赋值)才能使用
# 否则触发NameError异常

# 字符串
# python中可以用''(单引号)或""(双引号)来声明一个字符串
# 但是必须前后匹配
# \ 是用来转义的，比如:
message = 'hello zhq\'s pet'
print(message) # 输出 hello zhq's pet

# 有一些特殊字符 如：\n 回车 \t 制表 需要保留字符原意时，可以在字符串前面加r
print('c:some\name') # 此处\n 被解释为换行符 输出: c:some
                                              # ame
print(r'c:\some\name') # 保留了字符原意 输出: c:\some\name

# 字符串是不可变对象
# 可以使用str()内置函数，将其他对象转换为字符串
# 具体转换形式根据被转换对象__str__()方法的返回值而不同
# 如果对象没有实现__str__()方法，那么采用object对象的__str__()
# 这些是面向对象方面的东西

# 其他字符串方法，参考手册吧