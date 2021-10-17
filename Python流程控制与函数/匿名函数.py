# coding:utf-8

# lambda 表达式
# 匿名函数的意思就是可以不使用def定义,并且这个函数也没有名字
# 在python中可以使用lambda表达式来定义匿名函数
# 注意:lambda表达式仅仅是一个表达式,不是一个代码块,所以lambda又称为一行代码的函数
# lambda表达式也有形参,并且不能访问除了自己的形参之外的任何数据包含全局变量
'''
语法:
lambda [参数列表]:返回值
'''


# 封装一个函数做加法运算
def jia(x, y):
    return x + y

print(jia(1, 2))

# 改成lambda
res = lambda x, y: x + y
print(res(1, 2))  # 3

# lambda是一个表达式,因为不能写太复杂的逻辑,功能相对单一
# lambda是否可以使用分支结构

def func(sex):
    if sex == '男':
        return '很man'
    else:
        return '很nice'
res = func('男')
print(res)  # 很man

# 带有分支结构的lambda表达式
# lambda 参数列表:真区间 if 表达式判断 else 假区间
res = lambda sex: '很man' if sex == '男' else '很nice'
print(res('女'))  # 很nice