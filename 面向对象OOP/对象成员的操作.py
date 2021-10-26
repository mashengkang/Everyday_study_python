# coding:utf-8


'''
什么是对象的成员?
    一个对象通过类实例化之后,那么在类中定义的属性和方法,可以使用实例化的对象进行操作
    类中定义的属性,也称为成员属性,类中定义的方法,也称为成员方法
'''


# 定义一个汽车的类
class Cars():
    # 属性(特征) 变量
    color = '白色'
    brand = '奥迪'
    pailinag = 2.5

    # 方法(功能) 函数
    def lahuo(self):
        print('小汽车能拉货')

    def doufeng(self):
        print('小汽车能兜风')


# 实例化对象
a = Cars()
b = Cars()
print(a)  # <__main__.Cars object at 0x0000023F6CAAB610>
print(b)  # <__main__.Cars object at 0x0000023F6CBC1070>
'''
一个类可以实例化多个对象
以上的a和b变量都是对象,也都是用过Cars这个类实例化出来的对象
但是a和b是两个对象,相同之处就在于都同由一个类实例化出来
'''

# 对象成员的操作

# 一.在类的外部,使用对象操作成员
# 访问成员属性:先访问a对象自己的color属性,如果没有就去访问这个对象的类的属性
res1 = a.color  # 通过对象访问类中的属性

# 修改对象的属性值:实际上等于给这个对象创建了一个a对象自己的color属性
a.color = '黑色'  # 修改对象属性

# 添加对象的属性: 给当前a对象创建了自己独有的属性
a.name = 'A6'  # 给对象添加属性 ,此时的name属性只属于a
res2 = a.lahuo() # 通过对象访问类中的方法  # 小汽车能拉货

# a.color修改后,会影响b的属性吗?
print(b.color)  # 白色 ,还是原来的值
# print(b.name)  # b中没有name这个属性
# AttributeError: 'Cars' object has no attribute 'name'

# 删除属性: 只能删除这个对象自己的属性,包括给对象添加的和修改的
# del a.brand  # AttributeError: brand  不可以删除brand属性
del a.name  # 可以删除后添加的name属性
# print(a.name)  # AttributeError: 'Cars' object has no attribute 'name'
"""
上面例子中的brand属性并不是a对象自己的属性,而是属于Cars这个类,因此不能删除
而name属性,是单独给a的属性,所以可以删除
"""

# 二 在类的外部,操作对象的方法
# 访问对象的方法:实际上如果这个对下给你没有自己独立的方法,那么会访问这个对象的类的方法
res = a.lahuo()  # 通过对象访问类中的方法


# 修改对象的方法
def func():
    print("这是一个新的方法")


a.lahuo = func  # 把一个函数赋值给成员
a.lahuo()  # 这是一个新的方法

# 添加新的方法
a.func2 = func
a.func2()  # 这是一个新的方法

# 删除方法
del a.lahuo
a.lahuo()  # 小汽车能拉货
del a.func2
# a.func2  # AttributeError: 'Cars' object has no attribute 'func2'
# del a.lahuo  # AttributeError: lahuo  不可以删除这个对象的类的方法

'''
总结:
    一个类定义类成员属性和成员方法,那么通过这个类实例化的对象,也具备这些方法和属性吗?
    实际上,创建对象的时候,并不会把类中的属性和方法复制一份给对象,而是在对象中引用父类的方法
    因此在访问对象的属性时,会先去找对象自己的属性,如果没有就去找这个类的属性和方法
    
    一个对象由类创建以后,是一个独立的对象,会引用父类中的属性和方法
    如果在对象创建后,给对象的属性或方法,进行修改或添加,那么此时等于给这个对象创建了一个自己的属性和方法
    所以在删除时,只能删除对象被修改或添加的成员
'''


