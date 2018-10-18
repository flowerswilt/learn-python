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

# 可迭代对象不一定是迭代器对象，而迭代器对象一定是可迭代对象
print(isinstance([], Iterator)) # False
print(isinstance({}, Iterator)) # False
print(isinstance('zhq', Iterator)) # False

# 迭代器特征
f_iter = (x for x in range(1, 3))
print(f_iter) # <generator object <genexpr> at 0x104e95408>

