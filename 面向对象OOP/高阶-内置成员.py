# coding:utf-8

# 内置成员
class A():
    pass
class B():
    pass
class C():
    pass

class Demo(A,B,C):
    name = 'a'
    age = 20
    def say(self):
        print('说')

obj = Demo()
obj.san='aaa'
# 获取类/对象的所属成员  类/对象.__dict__
res1 = Demo.__dict__
# {'__module__': '__main__', 'name': 'a', 'age': 20, 'say': <function Demo.say at 0x0000016AFF378B80>, '__doc__': None}
res2 = obj.__dict__
# 获取类的文档信息 类/对象.__doc__
res3 = Demo.__doc__
res4 = obj.__doc__
# 获取类名称组成的字符串,实例化对象不可以使用
res5 = Demo.__name__
# res6 =obj.__name__  # 错误用法
# 获取类所在文件名称,如果是当前文件,显示为__main__
res7 = Demo.__module__
# bases 获取当前类的所有父类列表
# base 获取继承的第一个父类
res8 = Demo.__bases__  # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>)
res9 = Demo.__base__  # <class '__main__.A'>

# MRO列表,获取当前类的继承链
res10 = Demo.__mro__
print(res1)