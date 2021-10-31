# coding:utf-8
# 使用函数装饰器装饰类

'''
@装饰器和异常处理
class Demo():
    pass
装饰器给函数进行装饰,目的是不改变函数调用和代码的情况下给原函数增加新功能
装饰器给类进行装饰,目的是不改变类的定义和调用的情况下给类增加新的成员(属性过方法)
'''

# 使用函数装饰器,给类进行装饰,增加新的属性和方法
def kuozhan(cls):

    def func2():
        print('我是在装饰器中追加的新方法,func2')

    cls.func2 = func2
    cls.name = '我是在装饰器中追加的新属性'

    # 返回时,把追加类新成员的 类 返回去
    return cls


@kuozhan  # kuozhan(Demo) ==> cls ==>Demo
class Demo():

    def func():
        print('我是Demo类中定义的func方法')


Demo.func()  # 我是Demo类中定义的func方法 此时在调用的Demo类时通过装饰器,更新过的Demo类
Demo.func2()
print(Demo.name)
'''
我是Demo类中定义的func方法
我是在装饰器中追加的新方法,func2
我是在装饰器中追加的新属性
'''