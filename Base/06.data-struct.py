# 数据结构 -- 用来存储相关数据的集合
## python 有四种内置的数据结构 list、dictionary、set、tuple

# List类
temp_list = list()
print(temp_list) # 输出 []空的list集合
## 也可以使用简单的语法来初始化一个空的list
temp_list = []
print(temp_list) # 输出 []

# 当我们为一个变量赋值时，其实可以理解为实例化了一个类
# 比如 i = 5 我们可以认为我们实例化了一个int类，实例名称为i
# 列表也是一样的道理，同时列表属于可变数据类型,而int属于不可变数据类型
shop_list = ['apple', 'mango', 'carrot', 'banana'] # 实例化一个list类，标识符为shop_list

# 使用内置函数len 来获取元素个数
print('I have ', len(shop_list), 'items to purchase')
## 输出 I have  4 items to purchase

# 使用for语句来迭代一个list
print('These items are', end=' ')
for item in shop_list:
    print(item, end=' ')
## 输出: These items are apple mango carrot banana

# 添加一个新元素到列表末尾
print('\nI also have to buy rice')
shop_list.append('rice')
print('My shop_list is now ', shop_list)
## 输出: My shop_list is now  ['apple', 'mango', 'carrot', 'banana', 'rice']

# 为列表排序
print('I will sort my shop_list now ')
shop_list.sort()
print('Sorted shopping list is ', shop_list)
## 输出: Sorted shopping list is  ['apple', 'banana', 'carrot', 'mango', 'rice']

# 通过下标从列表中取元素
print('The first item I want to buy is ', shop_list[0])
## 输出: The first item I want to buy is  apple

# 从列表删除一个元素
old_item = shop_list[0]
del shop_list[0]
print('I bought the', old_item)
print('My shopping list is now ', shop_list)
## 输出: I bought the apple
##      My shopping list is now  ['banana', 'carrot', 'mango', 'rice']

# tuple
## 元组用于将多个对象组合在一起，它与str对象一样，都是不可变对象
## 定义一个元组
zoo = ('python', 'elephant', 'penguin')
## 同样可以使用内置函数len()来获取元素个数
print('Number of animals in the zoo is ', len(zoo)) # 输出3
## 元组可以嵌套，前面忘记说了list也可以嵌套
new_zoo = ('monkey', 'camel', zoo)
print('Number of cages in the new zoo is ', len(new_zoo))
# 输出: Number of cages in the new zoo is  3
print('All animals in the new zoo are ', new_zoo)
# 输出: All animals in the new zoo are  ('monkey', 'camel', ('python', 'elephant', 'penguin'))
print('Animals brought from old zoo are ', new_zoo[2])
# 输出: Animals brought from old zoo are  ('python', 'elephant', 'penguin')
print('Last animal brought from old zoo is ', new_zoo[2][2])
# 输出: Last animal brought from old zoo is  penguin
print('Number of animals in the new zoo is ',
      len(new_zoo) - 1 + len(new_zoo[2]))
# 输出: Number of animals in the new zoo is 5
## 上面的几个输出分别演示了tuple的取值方式，包括嵌套取值在内
## list 的取值方式大致一样，包括后面的dict 在内，这也是python始终推崇的一致性的体现

# dict(字典)
## 字典就像一个地址薄，我们将键与值相关联
## 字典中的键，必须是唯一的，且不可变的对象(比如：int、str、tuple)
## 字典中的键值对不以任何方式排序

# 定义一个字典
ab = {
    'swaroop' : 'swaroop@swaroopch.com',
    'larry' : 'larry@wall.org',
    'Matsumoto' : 'matsumoto@ruby-lang.org',
    'Spammer' : 'spammer@hotmail.com'
}
## 从字典中取值
print("Swaroop's address is ", ab['swaroop'])
## 输出: Swaroop's address is  swaroop@swaroopch.com
## 可以看到，与list、tuple略微不同的是，dict使用键来取值，这是很自然的事情

## 删除一个键值对, 并用内置函数len来对dict再次求值
del ab['Spammer']
print('\nThere are {} contacts in the address-book', len(ab))
## 输出: There are {} contacts in the address-book 3

## 遍历一个dict
for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))
## 输出:
## Contact swaroop at swaroop@swaroopch.com
## Contact larry at larry@wall.org
## Contact Matsumoto at matsumoto@ruby-lang.org

## 为列表添加一个键值对
ab['Guido'] = 'guido@python.org'

## 判断一个键是否存在于一个dict中
if 'Guido' in ab:
    print("Guido's address is ", ab['Guido'])
    ## 输出: Guido's address is  guido@python.org

# 序列
## list、str、tuple 都是序列
## 序列的主要特征是: 成员测试(in 或者 not in 表达式)、索引操作(list[0]取值)、切片操作
## 切片操作可以让我们获得序列的一部分
shop_list = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
## 索引操作
print('Item 0 is ', shop_list[0])
print('Item 1 is ', shop_list[1])
print('Item 2 is ', shop_list[2])
print('Item 3 is ', shop_list[3])
print('Item -1 is ', shop_list[-1])
print('Item -2 is ', shop_list[-2])
print('Character 0 is ', name[0])
"""
输出:
    Item 0 is  apple
    Item 1 is  mango
    Item 2 is  carrot
    Item 3 is  banana
    Item -1 is  banana
    Item -2 is  carrot
    Character 0 is  s
"""
## 比较有趣的部分是负数索引，给定一个负数索引的时候，序列会从末尾取值

## 列表切片
print('Item 1 to 3 is ', shop_list[1:3])
print('Item 2 to end is ', shop_list[2:])
print('Item 1 to -1 is ', shop_list[1:-1])
print('Item start to end is ', shop_list[:])
"""            
输出:
    Item 1 to 3 is  ['mango', 'carrot']
    Item 2 to end is  ['carrot', 'banana']
    Item 1 to -1 is  ['mango', 'carrot']
    Item start to end is  ['apple', 'mango', 'carrot', 'banana']
"""
## 从输出可以看的出来 切片操作计算方式基本上是 顾头不顾尾
## 比如 shop_list[1:3] 取shop_list[1]、shop_list[2] 两个元素
## 如果方括号的数字留空，分别代表序列的起始和结束

# 引用初探
## 当你创建了一个对象，并把它赋值给一个变量时，这个变量只是引用了这个对象
## 如果有c++经验，可以把变量存储的值当作一个对象的内存地址看待，事实上，内置函数id()的返回值，的确看起来像是内存地址
print(id(shop_list)) # 4417298312 这个数字不是固定的
my_list = shop_list # my_list 与 shop_list 指向了同一个对象地址
print(id(my_list), id(shop_list)) # 4409409416 4409409416
## 当我们修改shop_list时，my_list也会被修改，因为原则上讲，shop_list 与 my_list 是同一个对象
del shop_list[0]
print('shop list is ', shop_list)
print('my list is ', my_list)
"""
输出:
    shop list is  ['mango', 'carrot', 'banana']
    my list is  ['mango', 'carrot', 'banana']
"""
## 从上面的输出可以看到，在shop_list 删除了 'apple'后，my_list中的'apple'也随之不见

## 使用切片来获得一个副本
my_list = shop_list[:]
print(id(my_list), id(shop_list)) # 4490458376 4488609672 id不同啦

del my_list[0] # 删除my_list的第一个元素

print('shop_list is ', shop_list)
print('my_list is ', my_list)

"""
输出：
    shop_list is  ['mango', 'carrot', 'banana']
    my_list is  ['carrot', 'banana']
"""
## 从上面的输出可以看到，对于my_list的删除操作，shop_list并没有受到任何影响
