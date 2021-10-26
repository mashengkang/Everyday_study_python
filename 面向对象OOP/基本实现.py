# coding:utf-8


'''
类名的书写规范,建议使用驼峰命名法
    大驼峰: MyCar XiaoMa
    小驼峰:myCar xiaoMa
一个类有特征和功能两个内容组成:
    特征就是要给描述:白色, 品牌:奥迪, 排量...
    功能就是一个能力: 拉货,带美女兜风...

    特征在编程中就是一个变量,在类中,称为 属性
    功能在编程中就是一个函数,在类中,称为 方法
类中属性一般定义在前面,方法定义在后面
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

# 如何使用这个类?
# 通过类实例化一个对象
aodiobj = Cars()
print(aodiobj, type(aodiobj))  # <__main__.Cars object at 0x0000021B7CE9B610> <class '__main__.Cars'>

# 调用对象的 方法
aodiobj.lahuo()  # 小汽车能拉货
aodiobj.doufeng()  # 小汽车能兜风
