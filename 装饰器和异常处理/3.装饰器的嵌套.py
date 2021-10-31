# coding:utf-8
# 装饰器的嵌套

#1.普通装饰器的定义
# 外函数
def outer(f):
    print('in outer')
    # 内函数
    def inner():
        print('outer 1')
        f()  # 在内函数中调用外函数中的形参-函数
        print('outer 2')
    # 在外函数中返回内函数
    return inner

# @outer
# def love():
#     print('谈人生...')

# love()

# 2.再定义一个装饰器
def kuozhan(f):
    print('in kuozhan')
    def kzinner():
        print('kz1')
        f()
        print('kz2')
    return kzinner


@kuozhan  # 2.再使用上面的 kuozhan 装饰器和异常处理,装饰上一次返回的 inner 函数,又返回了 kzinner 函数
@outer  # 1.先使用离的近的,outer装饰器,装饰love函数,返回了一个inner函数
def love():
    print('谈人生...')

love()
'''
in outer
in kuozhan
kz1
outer 1
谈人生...
outer 2
kz2

1.先使用离的近的,outer装饰器,装饰love函数,返回了一个inner函数
2.再使用上面的 kuozhan 装饰器和异常处理,装饰上一次返回的 inner 函数,又返回了 kzinner 函数
'''