# coding:utf-8

# 常用函数

class A():
    pass


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    name = 'a'
    age = 20

    def say(self):
        pass


# issubclass(类1, 类2) 检测类1是否为类2的子类
res1 = issubclass(D, B)  # True

# isinstance(对象, 类) 检测对象是否是指定类或该类的子类的实例化的结果
c = C()
res2 = isinstance(c, B)  # False
res3 = isinstance(c, A)  # True

# hasattr(对象/类, '成员名称') 检测类/对象 是否包含指定名称的成员,(除私有成员)
res4 = hasattr(D, 'name')  # True
res5 = hasattr(D, 'say')  # Truesay

# getattr(对象/类, '成员名称') 获取类/对象的成员的值
d = D()
res6 = getattr(d, 'name')  # a
res7 = getattr(D, 'say')  # <function D.say at 0x000001A4EF756B80>

# setattr(对象/类, '成员名称', '设置的值') 设置类/对象的成员的属性值,没有返回值
res8 = setattr(d, 'name', 'b')
print(res8)  # None
print(d.name)  # b

# delattr() 删除类/对象的成员属性,和 del 直接删除对象的成员是一样的结果(只能删自己的,不能删引用的)
delattr(d, 'name')
print(d.name)  # a 删除了直接设置的b,所以返回引用的a,再删除的话就会报错

# dir() 获取当前对象所有可以访问的成员列表
res9 = dir(d)
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'age', 'name', 'say']
