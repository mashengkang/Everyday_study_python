# 元组 tuple
# 用途:记录多个值,当多个值没有更改的需求,此时元素更合适
# 定义方式:在()内用逗号分割开多个任意类型的值

t = (1, 2, '大海', (2, 3), [1, 2, 3])
print(t)
print(type(t))
print(len(t))
print(t[0])

# t[0] = 8
# print(t)
# 直接更改值不行,但是可以更改元素中列表中的值
t[4][0] = 8
print(t)  # (1, 2, '大海', (2, 3), [8, 2, 3])

# 元组是不能修改和添加元素的,所以元组是不可变类型
# 如果想修改可转换成列表
t = list(t)
t[0] = 8
print(tuple(t))


# 元组推导式--生成器
'''
列表推导式返回了一个列表,元组推导式返回一个生成器
    语法:
        列表推导式 ==> [变量运算 for i in 容器] ==>结果是一个 列表
        元组推导式 ==> (变量运算 for i in 容器) ==>结果是一个生成器
生成器是什么?
    生成器是一个特殊的迭代器,生成器可以自定义,也可以使用元组推导式去定义
    生成器是按照某种算法去推算下一个数据或结果,只需要往内存中存贮一个生成器,节约内存消耗,提升性能
    语法:
        (1) 里面是推导式,外面是一个()的结果就是一个生成器
        (2) 自定义生成器,含有yield关键字的函数就是生成器
            含有yield关键字的函数,返回的结果是一个迭代器,换句话说,生成器函数就是一个返回迭代器的函数
如何使用操作生成器?
    生成器是迭代器的一种,因此可以使用迭代器的操作方法来操作生成器
'''
# 列表推导式--列表
varlist = [1, 2, 3, 4, 5, 6]
newlist = [i**2 for i in varlist]
print(newlist)  # [1, 4, 9, 16, 25, 36]
# 元组推导式--生成器
newt = (i**2 for i in varlist)
print(newt, type(newt))  # <generator object <genexpr> at 0x0000025558E90CF0> <class 'generator'>
# 使用next()调用
print(next(newt))  # 1
# 使用list 或 tuple
# print(list(newt))  # [4, 9, 16, 25, 36]
print(tuple(newt))  # (4, 9, 16, 25, 36)

# yield 关键字

'''
yield 关键字使用在生成器函数中
    yield和函数中的return 有点像
    共同点:执行到这个关键字后会把结果返回
    不同点:
        return 会把结果返回,并结束当前函数的调用
        yield 会返回结果,并记住当前代码的执行位置,下一次调用时会从上一次离开的位置继续向下执行
'''
# 定义一个普通函数
# def hello():
#     print('hello1')
#     return 1  # return在函数中会把结果返回,并且结束当前的函数,后面的代码不再执行
#     print('hello2')
#     return 2

# 使用yield定义一个生成器函数
def hello():
    print('hello 1')
    yield 1
    print('hello 2')
    yield 2

# 调用生成器函数,返回一个迭代器,next如果没有元素的话会报错
res = hello()
# r1 = next(res)
# print(r1)
# r2 = next(res)
# print(r2)
# 转成列表
r3 = list(res)
print(r3)  # [1, 2]

'''
上面的生成器函数调用时的过程
    首先,调用来生成器函数,返回一个迭代器
    1.第一次去调用迭代器:
        走到函数中,遇到了yield 1,把1 返回,并且记住当前的执行状态(位置),暂停了函数的执行,等待下一次调用
    2.第二次去调用迭代器:
        从上一次遇到的yield 1位置后开始执行,遇到yield 2,把2 返回
    如果在最后又调用了迭代器,那么会从上一次的yield位置开始,结果后面没有了,就会报错
'''










