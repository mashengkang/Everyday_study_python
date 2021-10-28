# coding:utf-8

# 多态
# 对于同一个方法,由于调用的对象不同(或者传入的对象不同,产生了不同形态的结果

# 普通版多态展示
# 定义电脑类
class Computer():
    #
    def usb(self, obj):
        obj.start()

# 定义鼠标类
class Mouse():

    def start(self):
        print('鼠标启动')

# 定义键盘类
class KeyBord():

    def start(self):
        print('键盘启动了')

# 定义u盘类
class Udisk():

    def start(self):
        print('u盘启动了')

# 实例化对象
c = Computer()
m = Mouse()
k = KeyBord()
u = Udisk()

# 把不同的设备插入电脑的usb接口中
c.usb(m)  # 鼠标启动
c.usb(k)  # 键盘启动了
c.usb(u)  # u盘启动了


print('==========多态 继承版=========')
# 多态 继承版
'''
定义一个接口规范类,其他类都继承这个类,并实现(重写)父类中的方法
由于每个对象实现父类方法的方式或者过程不同,最后的结果也不同
'''
# 定义USB
class USB():
    '''
    当前类的说明:
        这个类是一个接口规范类,需要子类继承start方法
        start方法不做任何具体功能实现
    '''
    # 在usb类中定义一个规范的接口方法,但是不实现任何功能
    def start(self):
        pass

# 定义鼠标类
class Mouse(USB):

    def start(self):
        print('鼠标启动')

# 定义键盘类
class KeyBord(USB):

    def start(self):
        print('键盘启动了')

# 定义u盘类
class Udisk(USB):

    def start(self):
        print('u盘启动了')

# 实例化对象
m = Mouse()
k = KeyBord()
u = Udisk()
m.start()  # 鼠标启动
u.start()  # u盘启动了
k.start()  # 键盘启动了
