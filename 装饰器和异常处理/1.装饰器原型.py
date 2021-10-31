# coding:utf-8

'''
# 装饰器和异常处理 decorator
> 在不改变原有函数代码,且保持原函数调用方法不变的情况下,给原函数增加新的功能(或者给类增加属性和方法)
> 核心思想: 用一个函数(或者类) 去装饰一个旧函数(或者类),造成个新函数(或者新类)
> 语法规则:在原有的函数上加上, @符,装饰器会把下面的函数当作参数传递到装饰器中,@符又被称为 语法糖
> 应用场景:引入日志,函数执行时间的统计,执行函数前的准备工作,执行函数后的处理工作,权限校验,缓存等场景中
@outer
def func():
    pass
'''

# 1.装饰器原型
# 利用闭包,把函数当作参数传递,并且在函数内去调用传递进来的函数,并返回一个函数
# 定义外函数,接收一个函数作为参数
def outer(f):
    # 定义内函数,并且在内函数中调用了外函数的参数
    def inner():
        print('我是外函数中的内函数1')
        f()
        print('我是外函数中的内函数2')

    return inner
    # 此处的inner后不加 '()' 不然直接就是调用了

# 定义普通函数
def old():
    print('我是个普通函数')

# old()  # 作为普通函数直接调用
# outer(old)
# old()
'''
我是外函数中的内函数1
我是个普通函数
我是外函数中的内函数2
'''

# 改为装饰器

# 定义普通函数
@outer  # 此处使用的@outer的语法就是把outer作为了装饰器,等同于调用了innor
def old():
    print('我是个普通函数')

old()
