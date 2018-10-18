"""
迭代器:
    1. 可迭代对象
    2. 迭代器对象
"""

from collections.abc import Iterable, Iterator

print(isinstance([], Iterable)) # True
print(isinstance({}, Iterable)) # True
print(isinstance('zhq', Iterable)) # True
print(isinstance(100, Iterable)) # False

# 可迭代对象不一定是迭代器对象
print(isinstance([], Iterator)) # False
print(isinstance({}, Iterator)) # False
print(isinstance('zhq', Iterator)) # False

# 生成器一定是一个迭代器对象，它可以使用next()方法取值
print('__next__' in dir([])) # False
num_gen = (x for x in range(3))
print('__next__' in dir(num_gen)) # True

