# coding:utf -8

# 装饰带有多参数的函数

def outer(func):
    def inner(who, name, *args, **kwargs):
        print('inner 1')
        func(who, name, *args, **kwargs)
        print('inner 2')
    return inner


# 定义多参数的函数
@outer
def love(who, name, *args, **kwargs):
    print(f'{who}和{name}聊人生')
    print('去吃了好多美食,', args)
    print('看了一场电影,', kwargs)


love('小美','小马','火锅','辣条', mov = '喜剧之王')
'''
inner 1
小美和小马聊人生
去吃了好多美食, ('火锅', '辣条')
看了一场电影, {'mov': '喜剧之王'}
inner 2
'''