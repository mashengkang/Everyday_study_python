# coding:utf-8

# 魔术方法 初始化方法
'''
魔术方法:
    和普通方法一样都是类中定义的成员方法
    就是不需要手动调用,魔术方法会在某种情况下,自动触发(自动执行)
    特殊的地方:就是多数的魔术方法,前后都有两个连续的下划线
    不是我们自己定义的,而是系统定义好的,我们来使用

__init__ 初始化方法
    触发机制:在通过类实例化对象后,自动触发的一个方法
    作用: 可以在对象实例化后完成对象的初始化(属性的赋值,方法的调用..)
    应用场景: 文件的打开,数据的获取...

'''


class Person():
    # 成员属性
    name = None
    age = None
    sex = None

    # __init__
    def __init__(self, n, a, s):
        print(n, a, s)
        print('我是初始化方法')
        # 完成对象属性的初始化
        self.name = n
        self.age = a
        self.sex = s
        self.say()

    def say(self):
        print('你好')


zzh = Person('渣渣灰', '60', '男')
# 渣渣灰 60 男
# 我是初始化方法
# 你好
print(zzh.name)  # 渣渣灰

