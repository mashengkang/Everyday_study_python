# coding:utf-8

'''
方法的分类:
1.对象方法
    1.在类中定义的方法,含有self参数
    2.含有self的方法,只能使用对象进行第哦啊有
    3.该方法会把调用的对象传递进来
2.类方法
    1.在类中定义的方法,使用装饰器 @classmethod 进行装饰
    2.方法中有 cls 这个形参
    3.不需要实例化对象,直接使用类进行调用
    4.会把调用这个方法的类传递进来
3.绑定类方法
    1.在类中定义的方法
    2.只能使用类进行调用
    3.不会传递对象或者类进来
4.静态方法
    1.在类中定义的方法,使用了装饰器 @staticmethod 进行装饰
    3.可以私用对象或者类进行调用
    4.不会传递对象或者类进来


'''
class Demo():

    # 对象方法
    def func1(self):
        print(self)
        print('this is func1')

    # 类方法
    @classmethod
    def func2(cls, a):
        print(cls, a)
        print('this is class function func2')

    # 绑定类方法,可以不带形参
    def func3():
        print()
        print('this is bind')

    # 静态方法
    @staticmethod
    def func4(a, b):
        print(a, b)
        print('this is func4')


obj = Demo()
obj.func1()
# Demo.func1()  # 不能直接使用类调用,不推荐

Demo.func2(1)
# <class '__main__.Demo'> this is class function func2
obj.func2(1)  # 即便使用对象调用,传递的依然是类

Demo.func3()  # this is bind
# obj.func3()  # 不能实例化对象调用

Demo.func4(3,1)
obj.func4(2,5)