# coding:utf-8
# 带有参数的装饰器

# 如果你的装饰器需要有参数,那么给当前的装饰器套一个壳,用于接收装饰器的参数
def kuozhan(var):
    def outer(func):
        def inner1():
            print(f'妹子给了{var}微信')
            func()

        def inner2():
            print(f'妹子给{var}介绍了大妈')
            func()

        if var == '高富帅':
            return inner1
        else:
            return inner2
    return outer

@kuozhan('高富帅')
def love():
    print('end')

love()