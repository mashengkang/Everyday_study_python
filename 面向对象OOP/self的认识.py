# coding:utf-8


class Person():
    # 成员属性
    name = '名字'
    age = '年龄'
    sex = '性别'

    # 成员方法
    def sing(self):
        print('会唱')

    def dance(self):
        print('会跳')

    def rap(self):
        print('会rap')

    def func(self):
        # 测试:在类的内部是否可以像类的外部一样,去访问和操作成员
        print(self)
        print(self.name)  # 访问对象的属性
        self.rap()  # 调用对象的方法
        # 只要是对象能干的,self都可以代表对象去完成

    # 定义不含self的方法 绑定类方法 (不接受对象参数的方法,只能使用类去访问
    def func2():
        print('不含self的方法')



# 实例化对象
zs = Person()
# 通过类实例化的对象,可以在类的外部去访问成员属性和方法(对象.成员)
print(zs.name)
print(zs)  # <__main__.Person object at 0x000001065098B610>
zs.func()  # <__main__.Person object at 0x000001065098B610>  名字 会rap
'''
self 单词本身的意思是自己
self 在类的方法中 代表 当前这个对象
self 代表调用这个方法的对象
self 就可以在类的内部代替对象进行各种操作

如果在类中定义的方法不含self这个形参时,(self形参,包括其他的代替都不可以,也就是没有参数的)
那么这个方法就不能使用对象去调用
不含self形参的方法,只能使用类去调用
这种不接受对象作为形参的方法,叫做绑定类发法
'''
# zs.func2()  # TypeError: func2() takes 0 positional arguments but 1 was given
Person.func2()  # 不含self的方法