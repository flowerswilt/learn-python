# 面向对象编程是一种组织程序代码的方式
# python即支持面向过程，也完整支持面向对象
# 面向对象有两个主要的概念
# 类和对象
# 一个类创建了一个新的数据类型，而对象就是这个类的实例
class Person(object):
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello my name is {}'.format(self.name))

person = Person('zhq')
person.say_hi()
# Person就是我们自己创建的数据类型
# person是Person类的一个实例对象

# 关于self
## 对象能够使用原始数据类型存储数据
## 比如上面的name，这在面向对象中成为对象属性，python简明教程中译版中将其翻译为域
## 对象也可以使用属于类的函数实现一定功能，这在面向对象中称之为方法
## 域和方法都可以被成为类的属性
## 类的方法和普通函数相比只有一个区别: 它们在入口参数表的开头必须有一个额外的形式参数，但你在调用它的时候，不用提供它
## python会自动提供给它，这个特别的参数指向对象自身，名称叫做self
## 如果可以类比，self与java中的this引用等价
## 在上面的栗子中，我们调用person.say_hi()时，python解释器会将其翻译为Person.say_hi(person)

# 关于__init__方法
## 此方法将会在对象被创建时由解释器自动调用

# 类和对象中的变量
## 这些变量只是绑定到类或对象中的普通变量，只在类和对象的上下文中有效
## 有两种类型，分别是: 类变量和对象变量(也可以成为实例变量)
## 类变量是所有实例对象共享，对象变量是实例本身自己所有
## 类中的变量都是public的，在其他面向对象编程语言中有public、protected、private的概念
## python中没有这种概念，只有public或private
## 区别仅仅是:
##    普通变量默认为public 如 name
##    双下划线的变量为private 如 __name

class Robot():
    """代表一个机器人，拥有一个名字属性"""

    # 类属性，统计机器人数量
    population = 0

    def __init__(self, name):
        """初始化数据"""
        self.name = name

        print('(Initializing {})'.format(self.name))

        # 当机器人被生产出来时
        # 机器人人口+1
        Robot.population += 1

    def die(self):
        """机器人死亡"""
        print('{} is being destroyed!'.format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print('{} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working.'.format(Robot.population))

    def say_hi(self):
        """来自机器人的问候"""
        print('Greetings my master call me {}.'.format(self.name))

    @classmethod
    def how_many(cls):
        """显示当前机器人总数"""
        print('We have {:d} robots'.format(cls.population))

droid1 = Robot('R2-D2')
droid1.say_hi()
Robot.how_many()

droid2 = Robot('C-3P0')
droid2.say_hi()
Robot.how_many()

print('\nRobot can do some work here. \n')

print('Robots have finished their work. So let\'s destroy them.')
droid1.die()
droid2.die()

Robot.how_many()

"""
输出:
    (Initializing R2-D2)
    Greetings my master call me R2-D2.
    We have 1 robots
    (Initializing C-3P0)
    Greetings my master call me C-3P0.
    We have 2 robots
    
    Robot can do some work here. 
    
    Robots have finished their work. So let's destroy them.
    R2-D2 is being destroyed!
    There are still 1 robots working.
    C-3P0 is being destroyed!
    C-3P0 was the last one.
    We have 0 robots
    
程序按照我们所预想的执行了:

    population 是一个类属性，由所有Robot实例共享
    name 是一个对象属性(使用self来指向)，它属于每一个实例个体所有
        两者的访问方式也不相同
        population使用Robot.population 来访问
        name 使用 self.name 来访问
    除了使用类名.类变量来访问以外，也可以使用self.__class__.population来访问
    因为每一个对象实例的self.__class__都指向了类本身，在这个栗子中也就是Robot
    how_many是一个使用装饰器装饰过的方法
    @classmethod装饰器装饰的方法是类方法
    也就是说我们可以使用Robot.how_many()的方式来调用它
    这个方法第一个参数cls代表类自身
"""

## 关于面向对象的继承、多态以后再补充
