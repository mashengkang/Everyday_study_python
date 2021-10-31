# coding:utf-8

'''
单例设计模式:
    在当前脚本中,同一个类只能创建出一个对象去使用,这种情况就称为单例(单态)
    实现单例的案例,思考:
1.需要有一个方法,可以去控制当前对象的创建?
    构造方法 __new__
2.需要有一个标示来存储和表示是否有对象
    创建一个属性,进行存储,默认值是None
3.在创建对象的方法中去检测和判断是否有对象?
    如果没有对象,则创建对象,并且把对象存储起来
    如果存储的是对象,则直接返回对象,就不需要创建新的对象了
'''

class Demo():
    # 定义私有属性存储对象, 默认None
    __obj = None

    # 定义构造方法
    def __new__(cls, *args, **kwargs):
        # 如果没有对象
        if not cls.__obj:
            # 创建对象并保存起来
            cls.__obj = object.__new__(cls)
        # 返回对象
        return cls.__obj


# 实例化对象
a = Demo()
b = Demo()
print(a)  # <__main__.Demo object at 0x0000024CAFF11070>
print(b)  # <__main__.Demo object at 0x0000024CAFF11070>
