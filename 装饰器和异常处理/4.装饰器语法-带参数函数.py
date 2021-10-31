# coding:utf-8


# 对带有参数的函数进行装饰

# 定义装饰器
def outer(func):
    # 如果装饰带有参数的函数,需要在内函数中定义形参,并传递给调用的函数,因为调用原函数等于调用内函数
    def inner(var):
        print('inner s')
        func(var)
        print('inner e')
    return inner

# 有参数的函数
@outer
def love(name):
    print(f'我喜欢{name}')

love('xiaohua')
'''
inner s
我喜欢xiaohua
inner e
'''
