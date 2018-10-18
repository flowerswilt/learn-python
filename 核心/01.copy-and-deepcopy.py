import copy
"""
python的深浅拷贝
"""
will = ['will', 12, ['windows', 'linux', 'mac os']]

will_back = will

print(id(will))
print(id(will_back))
print(id(will[2]), id(will_back[2]))
print(will[0] is will_back[0])
print(will[2] is will_back[2])
print(will is will_back)

# 从上面输出结果可以看出，赋值操作实际是引用的传递，即传递的是变量的内存地址
# 使用浅拷贝试试
will_copy = copy.copy(will)
print(id(will))
print(id(will_copy))
print(id(will[0]), id(will_copy[0]))
print(id(will[2]), id(will_copy[2]))
print(will[0] is will_copy[0])
print(will[2] is will_copy[2])
print(will == will_copy)
print(will is will_copy)
"""
    输出结果:
        4457599176
        4458338376
        4507533920 4507533920
        4458338056 4458338056
        True
        True
        True
        False
"""
# 上面的输出结果显示，will 与 will_copy 的id已经不再相同，两个对象指向了不同的内存地址
# will 与 will_copy中的对象id不变
# will 与 will_copy 使用比较计算，返回True，两个对象的值相同
# will 与will_copy 使用is 计算，返回false ，两个对象是不同的对象

will_deepcopy = copy.deepcopy(will)
print(id(will))
print(id(will_deepcopy))
print(id(will[0]), id(will_deepcopy[0]))
will[0] = 'will_mod'
print(will[0], will_deepcopy[0])
print(id(will[2]), id(will_deepcopy[2]))
print(will[0] is will_deepcopy[0])
print(will[2] is will_deepcopy[2])
print(will == will_deepcopy)
print(will is will_deepcopy)

"""
    输出结果:
        4415869128
        4416607880
        4415472224 4415472224
        4416607816 4416641992
        True
        False
        True
        False
"""
# 在使用深拷贝时
# 两个对象的ID不同，说明是两个不同的内存地址的对象
# 两个对象内的不可变对象ID没变, 但是在修改了原对象后，深拷贝对象并不受影响，这是不可变对象的副作用

"""
    结论:
        1. 赋值操作符简单来说只是简单的将源对象地址的内存地址赋值给目标对象
        2. copy.copy()函数创建了一个新的目标对象接收源对象所有属性的内存地址
        3. copy.deepcopy()函数递归创建源对象的所有属性
"""