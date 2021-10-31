# coding:utf-8
# 使用类装饰器装饰类


class Kuozhan():

    def __call__(self, cls):
        # 把接收的类,赋值给当前对象,作为一个属性
        self.cls = cls
        # 返回一个函数
        return self.newfunc

    def newfunc(self):
        self.cls.name = '我是在类装饰器中追加的属性 name'
        self.cls.func2 = self.func2
        # 返回传递进来的类的实例化结果 obj
        return self.cls()

    def func2(self):
        print('我是在类装饰器中追加的新方法 func2')

@Kuozhan()
class Demo():
    def func(self):
        print('我是Demo类中定义的func方法')


obj = Demo()
print(obj)  # 此时的obj依然是Demo类的实例化对象,只不过经过装饰器,增加了新的方法和属性
obj.func()
obj.func2()
print(obj.name)
'''
<__main__.Demo object>  Demo类的实例化对象
我是Demo类中定义的func方法
我是在类装饰器中追加的新方法 func2
我是在类装饰器中追加的属性 name
'''