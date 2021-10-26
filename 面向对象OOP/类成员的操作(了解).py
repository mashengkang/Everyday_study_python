# coding:utf-8


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

# 在类的外部,可以直接通过类对成员进行操作

a = Cars()
# 一.类成员的操作
# 访问成员属性
print(Cars.brand)  # 奥迪

# 修改类成员属性
Cars.brand = '宝马'
print(Cars.brand)  # 宝马

# 思考:如果通过类把属性进行类的修改,那么再通过这个类实例化的对象,他的属性时什么呢?
b = Cars()
print(b.brand)  # 宝马
print(a.brand)  # 宝马  在类属性修改前创建的对象的属性也被修改

# 给类添加成员属性
Cars.name = 'A6'
print(Cars.name)  # A6
# 思考:通过类创建的对象是否也有这个属性?之前创建的对象和之后创建的?
# 答:都有这个属性
print(b.name)  # A6
c = Cars()
print(c.name)  # A6

# 删除类的成员:在之前和之后创建的对象,都不在有这个属性了
del Cars.name
# print(c.name)  # BAttributeError: 'Cars' object has no attribute 'name'

# 二.类成员方法的操作
