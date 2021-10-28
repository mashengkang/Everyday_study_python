# coding:utf-8


"""
封装就是使用特殊的语法,对成员属性和成员方法进行包装,达到保护和隐藏的目的
但是一定注意,不能把成员全部封装死,就失去意义了
被封住的成员主要供类的内部使用
被特殊语法封装的成员,会有不同的访问权限

封装的级别
    公有的 public          成员
    受保护的 protected      _成员
    私有的 private         __成员

"""

class Person():
    name = '姓名'
    _age = '年龄'  # 在成员前面加一个 _受保护的成员
    __sanwei = '三围'  # 加两个__ 私有的

    def __init__(self, n, a, s):
        self.name = n
        self._age = a
        self.__sanwei = s

    def func(self):
        print(self.__sanwei)  # 在类的内部可以使用私有成员

    # 方法
    def say(self):
        print('聊人生')

    def sing(self):
        print('唱歌')

    def kiss(self):
        print('打kiss')


# 实例化对象
ym = Person('杨幂', 20, '60 80 60')


print(ym.name)  # 杨幂
print(ym._age)  # 20 python中可以查看受保护的成员
# print(ym.__sanwei)  #  AttributeError: 'Person' object has no attribute '__sanwei'
# 不能查看私有成员
print(ym._Person__sanwei)  # 60 80 60 可以通过特殊语法查看私有成员

print(ym.__dict__)  # {} 为空 可以获取当前对象的所有属性
# print(Person.__dict__)  # 可以获取当前类的所有成员信息
# {'__module__': '__main__', 'name': '姓名', 'age': '年龄', 'sanwei': '三围', 'say': <function Person.say at 0x0000020073229B80>, 'sing': <function Person.sing at 0x0000020073229AF0>, 'kiss': <function Person.kiss at 0x00000200732299D0>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None}
