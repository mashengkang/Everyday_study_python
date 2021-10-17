# coding:utf-8

# 闭包函数
# 既然可以吧函数作为一个形参进行传递,作为回调函数,那么如果在一个函数中,返回了一个函数呢?
# 在一个函数内返回了一个内函数,并且这个返回的内函数还使用了外函数中局部变量,这就是闭包函数
'''
闭包的特点
    1.在外函数中定义了局部变量,并且在内部函数中使用了这个局部变量
    2.在外函数中返回了内函数,返回的内函数就是闭包函数
    3.主要在于保护了外函数中的局部变量,既可以被使用,又不会被破坏
'''
money = 0

# 工作
def work():
    global money
    money += 100

# 加班
def overwork():
    global money
    money += 200

# 购物
def buy():
    global money
    money -= 50

work()
work()
work()
overwork()
buy()
money = 0
print(money)


# 改成闭包
def person():
    money = 0
    # 工作   在外函数中定义的内函数
    def work():
        nonlocal money  # 在内函数中使用了外函数的临时变量
        money += 100
        print(money)
    # 在外函数中返回了内函数,这个内函数就是闭包函数
    return work


res = person() # return work ==> res = work
res()  # 100
res()  # 200
res()  # 300

