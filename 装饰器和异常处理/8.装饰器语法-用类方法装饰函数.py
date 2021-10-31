# coding:utf-8
# 用类方法装饰一个函数


class Outer():

    def newinner(func):
        Outer.func = func  # 把传递进来的函数定义为类方法
        return Outer.inner  # 同时返回一个新的类方法

    def inner():
        print('要到微信')
        Outer.func()
        print('看电影')


@Outer.newinner
def love():
    print('和妹子聊天')

love()
'''
要到微信
和妹子聊天
看电影
'''