# enum模块定义了一个可迭代和可比较的枚举类型
# 它可以为'值'创建具有良好定义的标识符，而不是直接使用字面上的字符串或整数

import enum

# 创建枚举
## 尽管我们使用class语法创建enumerate，但它仍不是python的标准class
## 这种语法只是更宜都、易写而已
## Enum的成员是可哈希的，所以它们可以用作字典或者set的键
class BugStatus(enum.Enum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

    by_design = 4
    closed = 1

print('Member name: {}'.format(BugStatus.wont_fix.name))
print('Member value: {}'.format(BugStatus.wont_fix.value))

## Enum 每一个实例都有一个name属性对应成员名称 value属性对应成员值

# 迭代枚举

for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

"""
    输出:
        new             = 7
        incomplete      = 6
        invalid         = 5
        wont_fix        = 4
        in_progress     = 3
        fix_committed   = 2
        fix_released    = 1
"""
## 每一次迭代都产生一个独立的枚举成员
## 成员以它们在类中定义的顺序逐个产生

# 迭代的比较

## 由于枚举成员不是有序的，所以只能以ID或者按值的相等性比较

actual_state = BugStatus.wont_fix
desired_state = BugStatus.fix_released

print('Equality:',
      actual_state == desired_state,
      actual_state == BugStatus.wont_fix)

print('Identity:',
      actual_state is desired_state,
      actual_state is BugStatus.wont_fix)

"""
    输出:
        Equality: False True
        Identity: False True
"""
## 对枚举成员应用大于和小于比较操作符将会抛出TypeError异常
## 若想使用'<' 或 '>' 比较枚举成员，则需要使用IntEnum类

class BugIntStatus(enum.IntEnum):

    new = 7
    incomplete = 6
    invalid = 5
    wont_fix = 4
    in_progress = 3
    fix_committed = 2
    fix_released = 1

print('Ordered by value:')
print('\n'.join(' ' + s.name for s in sorted(BugIntStatus)))

"""
    输出:
        Ordered by value:
         fix_released
         fix_committed
         in_progress
         wont_fix
         invalid
         incomplete
         new
"""

# 枚举值是唯一的
## 具有相同值的枚举成员，会被解释器当作同一个对象
## 还是以BugStatus(enum.Enum) 类为例
for status in BugStatus:
    print('{:15} = {}'.format(status.name, status.value))

print('\n Same: by_design is wont_fix: ',
      BugStatus.by_design is BugStatus.wont_fix)

print('\n Same: closed is fix_released: ',
      BugStatus.closed is BugStatus.fix_released)
"""
    输出:
        new             = 7
        incomplete      = 6
        invalid         = 5
        wont_fix        = 4
        in_progress     = 3
        fix_committed   = 2
        fix_released    = 1
        
        Same: by_design is wont_fix:  True

        Same: closed is fix_released:  True
"""
## 上面可以清晰的看到，by_design 和 closed 没有出现在迭代中
## by_design 与 wont_fix 是同一个对象
## closed 与 fix_released 是同一个对象

