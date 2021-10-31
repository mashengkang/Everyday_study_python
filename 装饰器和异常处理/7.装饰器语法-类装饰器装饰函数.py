# coding:utf-8


class Outer():

    # 魔术方法:当把该类的对象当作函数调用时,自动触发obj()
    def __call__(self, func):
        # 把传进来的函数作为对象的成员方法
        self.func = func
        return self.inner  # 返回一个函数

    # 在定义的需要返回的新方法中,去进行装饰和处理
    def inner(self, who):
        print('in class 1')
        self.func(who)
        print('in class 2')


@Outer()
def love(who):
    print(f'{who}和妹子聊天')


love('小马')
'''
in class 1
小马和妹子聊天
in class 2
'''
print(love)  # <bound method Outer.inner of <__main__.Outer> 现在的love是outer类这个对象的inner方法