# coding:utf-8


'''
当子类继承父类后,就可去使用父类中的成员属性和方法(除了私有成员)
子类可以有自己的属性和方法,也可以没有
子类继承父类后,重新定义了父类中的方法,这种情况称为对父类方法的重写
在子类中可以去直接调用父类中定义的方法 super().方法名()
子类调用父类的方法时,如果该方法有参数,也需要传递参数
子类继承父类后,定义了父类中没有的方法,这种情况称为对父类的扩展
一个父类可以被多个子类继承
'''
# 继承
# 猫科动物
class Maoke():
    # 属性
    maose = '猫纹'
    sex = 'm'

    # 方法
    def pao(self):
        print('能跑')

    def pa(self):
        print('能爬')


# 定义猫类
class Mao(Maoke):
    # 继承父类后,重新定义父类中的方法
    def pa(self):
        # 在子类中,调用父类的方法 super().方法()
        super().pa()
        print('子也会爬')

    def zhua(self):
        print('抓老鼠')


# 通过猫类 实例化对象
h = Mao()
print(h.__dict__)  # {} 为空

# 可以获取对象的属性, 先找猫对象自己的属性=>没有的话,找猫类的属性=>还没有就到父类中找
print(h.maose)  # 猫纹
# 可以调用对象方法
h.pao()  # 能跑
h.pa()  # 子也会爬 重写父类方法
h.zhua()  # 抓老鼠 扩展方法


# 一个父类可以被多个子类继承
class Bao(Maoke):
    pass

b = Bao()
b.pa()


# 多继承
# 父亲类
class F():

    def eat(self):
        print('大口吃')


# 母亲类
class M():

    def eat(self):
        print('浅尝即止')


# 子类
class Z(F, M):
    def eat(self):
        super().eat()  # 父类方法的调用
        print('吃也哭不吃也哭')

# 实例化对象
z = Z()
z.eat()  # 大口吃 吃也哭不吃也哭

print('-----菱形继承-----')

# 菱形继承
'''
  Human
F       M
    Z
'''
# 祖先类
class Human():
    num = 444
    def eat(self):
        print(self.num)
        print('顿顿都是烧烤')


# 父亲类
class F(Human):
    num = 333
    def eat(self):
        super().eat()
        print(super().num)
        print('大口吃')


# 母亲类
class M(Human):
    num = 222
    def eat(self):
        super().eat()
        print(super().num)
        print('浅尝即止')


# 子类
class Z(F, M):
    num = 111
    def eat(self):
        super().eat()  # 父类方法的调用
        print(super().num)
        print('吃也哭不吃也哭')

z = Z()
z.eat()  # 333 吃也哭不吃也哭

'''
继承的关系
Z->F->M->Human
    111    Human的self是Z的self对象,在层层调用时,self是Z的对象传递的
    顿顿都是烧烤
    444
    浅尝即止
    222
    大口吃
    333
    吃也哭不吃也哭
'''
# mro() 获取MRO列表,就是类的继承关系
print(Z.mro())

'''
super()
    使用super()调用父级的方法时,实际上是在用super调用MRO列表中的上一级中的方法
    使用super()调用父级的属性时,实际上是在用super调用MRO列表中的上一级中的属性
super() 本身调用父级方法时,传递的self对象,就是这个方法的self对象自己
'''


print('====继承关系检测====')
# 继承关系检测

class A:
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

# 获取类的MRO列表
print(D.mro())  # D-B-C-A

# 检测一个类是不是另一个类的子类
res1 = issubclass(D, B)  # True 检测D类是不是B类的子类
res2 = issubclass(A, B)  # False 检测A类是不是B类的子类
