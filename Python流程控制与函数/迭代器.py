# coding:utf-8


'''
迭代器:
    迭代器是python中最具有特色的功能之一,是访问集合元素(容器类型:列表,元素...)的一种方式
    迭代器是一个可以记住访问遍历的位置的对象
    从集合的第一个元素开始访问,直到集合中的所有元素被访问完毕
    迭代器只能从前往后的一个一个遍历,不能后退
    迭代器是一个能被next()函数调用,并不能返回下一个值的对象称为迭代器(Iterator迭代器对象)
'''

# range(2, 10) 2,9 返回一个可迭代对象,左闭右开
# for i in range(10, 3, -1):
#     print(i)

'''
iter()
    功能:把可迭代对象,转为一个迭代器对象
    参数:可迭代对象 (str, list, tuple, dict, set, range...)
    返回值:迭代器对象
注意:迭代器一定是一个可以迭代的对象,但是可迭代对象不一定是迭代器
'''
# 定义一个列表,是一个可迭代对象
f4 = ['赵四', '刘能', '小沈阳', '宋小宝']
# 可以使用for循环来遍历数据
# 可以把可迭代对象转为迭代器使用
res = iter(f4)
print(res, type(res))  # <list_iterator object at 0x00000249720D20A0> <class 'list_iterator'>

'''
迭代器取值的特点,取出一个少一个,直到都取完,最后再获取的话就会报错
迭代器取值的方案
    1. next()
    2. list()
    3. for
'''

# 1. 使用next()函数去调用迭代器对象
# r = next(res)
# print(r)  # 赵四
# r = next(res)
# print(r)  # 刘能
# print(next(res))  # 小沈阳
# print(next(res))  # 宋小宝
# print(next(res))  # 报错StopIteration,超出可迭代的范围

# 2. 使用list()取值
# r = list(res)
# print(r)  # ['赵四', '刘能', '小沈阳', '宋小宝']

# 3. for 取值
for i in res:
    print(i, end=' ')  # 赵四 刘能 小沈阳 宋小宝

# 检测迭代器和可迭代对象的方法
from collections.abc import Iterable, Iterator

varstr = '123456'
res = iter(varstr)
# type()函数返回当前数据的类型
# isinstance() 检测一个数据是不是一个指定的类型
r1 = isinstance(varstr, Iterable)  # True 是可迭代对象
r2 = isinstance(varstr, Iterator)  # False 不是一个迭代器
r3 = isinstance(res, Iterator)  # True 是可迭代对象
r4 = isinstance(res, Iterator)  # True 是迭代器
print(r1, r2, r3, r4)
