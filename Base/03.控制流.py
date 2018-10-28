import random
# python 中包含 if for while 三个控制流语句

# if 用于检查一个条件是否成立

# number = 23
# guess = int(input('Enter an integer >>> ').strip())
#
# if guess == number:
#     # 如果条件成立，执行此代码块 注意python使用缩紧来区别代码块
#     print('Congratulations, you guessed it.')
#     print('(but you do not win any prizes!)')
#     # 代码块结束
# elif guess < number:
#     # 只有在上一个条件不成立时，才会判断这个条件
#     print('No, it is a little higher than that')
# else:
#     # 上面两个条件都不成立
#     print('No, it is a little lower than that')
#
# print('Done') # 无论条件是否成立，都会执行此处!

# while语句可以重复执行一个语句块，直到while的条件为假
# break 用于结束整个循环
# continue 用于跳出当前循环

number = random.randint(1, 100)

while True:  # 条件永远是真

    guess = input('Enter an integer or q(quit): >>>').strip()

    if guess == 'q': # 判断用户是否希望退出程序
        break
    else:
        guess = int(guess) # 将输入转换为整数
        if guess == number:
            print('Congratulations, you guessed it.')
            print('(but you do not win any prizes!)')
            break
        elif guess < number:
            print('No, it is a little higher than that')
            print('Try it again')
            continue
        else:
            print('No, it is a little lower than that')
            print('Try it again')
            continue
print('Done')
# 上面是一个猜测数字的小游戏
# 随机生成一个1～100的数字，如果用户猜中数字，那么程序结束
# 如果用户猜测的数字小于或者大于生成的数字，那么提示用户继续输入

# for 循环用于迭代一个序列
for i in range(1, 5):
    print(i) # 输出1 2 3 4