# coding:utf-8

'''
内置函数:
    内置函数就是再系统安装完python解释器时,python解释器给提供的函数
'''

# 1. range()函数
'''
range() 函数
    功能:能够生成一个指定的数字序列,不是列表,也不是迭代器
'''
res = range(10)
# 转为list列表
print(list(res))
# for循环遍历
for i in res:
    print(i)
# 转为迭代器,使用next()函数调用
res = iter(res)
print(next(res))  # 0
print(next(res))  # 1

# 2. zip(*iterables)函数
'''
功能:zip函数是可以接受多个可迭代的对象,然后把每个可迭代对象中的第i个元素组合在一起,形成一个新的迭代器
参数: *iterables ,任意个数的可迭代对象
返回值:返回一个元组的迭代器,元组的个数:与多个可迭代对象中最少元素个数的那个相一致
'''

var1 = [1, 2, 3, 4]
var2 = ['a', 'b', 'c', 'd']
var3 = ['A', 'B', 'C', 'D', 'E']
# 调用zip函数,组成新的元组迭代器
res = zip(var1, var2, var3)
print(res, type(res))  # <zip object at 0x0000022B7F9DF200> <class 'zip'>

# for i in res:
#     print(i, type(i))
'''
输出为:
(1, 'a', 'A') <class 'tuple'>
(2, 'b', 'B') <class 'tuple'>
(3, 'c', 'C') <class 'tuple'>
(4, 'd', 'D') <class 'tuple'>
'''

print(list(res))  # [(1, 'a', 'A'), (2, 'b', 'B'), (3, 'c', 'C'), (4, 'd', 'D')]

'''
变量相关函数
    1.id()  获取当前数据的ID标识
    2.type()  获取当前数据的类型字符串
    3.print()  打印数据
    4.input()  输入的数据
    5.isinstance() 检测是否是某类型的数据
数学相关函数
    1.abs() 获取一个数的绝对值
    2.sum([1,2,3]) 求和,返回总计值,参数只能是容器类型,不可以写成sum(1,2,3)
    3.max([1,2,3]) min(1,2,3) 最大最小值,参数可以是容器类型,也可以比较两个以上的参数
    4.pow(x,y) 返回x 的y次幂
    5.round(3.1415926,2) 小数点保留位数,如果不带第二个参数,默认取整
遵循四舍五入:但如果与两个倍数的距离相等，则选择偶数 (因此，round(0.5) 和 round(-0.5) 均为 0 而 round(1.5) 为 2)

'''
print(round(4.5))  # 4
print(round(3.5))  # 4
print(round(0.5))  # 0
print(round(-0.5))  # 0
print(round(3.1415926, 2))  # 3.14

"""
进制相关参数
    1.bin() 将数值类型转为二进制
    2.int() 转为整数
    3.oct() 转为八进制
    4.hex() 转为十六进制数
"""
print(oct(613))  # 0o1145
print(hex(613))  # 0x265
print(int(0o1145), int(0x265))  # 613 613

'''
内置函数中的几个高阶函数
    1.sorted(iterable,[reverse],[key]) 
        排序,把可迭代的对象里的元素,一个一个取出来,放到key函数中进行处理,并按照函数中return的结果进行排序,返回一个新的列表
        reverse:默认为False,不进行反转,True反转
        key:可以是自定义函数,也可以是内置函数
'''
# sorted()
arr = [1, 3, 67, -4, 12, 52, 34]
# 默认从小到大,返回的是一个新的列表
res = sorted(arr)
print(res)  # [-4, 1, 3, 12, 34, 52, 67]
print(arr)  # [1, 3, 67, -4, 12, 52, 34]
print(sorted(arr, reverse=True))  # [67, 52, 34, 12, 3, 1, -4]
# 使用abs这个函数(求绝对值)作为sorted作为key关键字参数使用
print(sorted(arr, key=abs))  # [1, 3, -4, 12, 34, 52, 67]


# 使用自定义函数
def func(num):
    return num % 2


print(sorted(arr, key=func))  # [-4, 12, 52, 34, 1, 3, 67]
# 优化版
print(sorted(arr, key=lambda x: x % 2))  # [-4, 12, 52, 34, 1, 3, 67]

'''
2.map(func, *iterables)
        对传入的可迭代数据中的每个元素放入到函数中进行处理,返回一个新的迭代器
        func : 函数,自定义函数或者内置函数
        iterables:可迭代的数据
        返回值: 迭代器
'''
# map()
# 将str转成int
varlist = ['1', '2', '3', '4']
res = list(map(int, varlist))
print(res)  # [1, 2, 3, 4]


# 元素取二次方
def my_func(x):
    return x ** 2


res_func = map(my_func, res)
print(res_func, list(res_func))

# 优化版
res_lambda = map(lambda x: x ** 2, res)
print(res_lambda, list(res_lambda))

'''
3. reduce(func,*iterable)函数
    功能:每一次从iterable拿出两个元素,放入到func函数中进行处理,得出一个计算结果
        然后把这个结果和iterable中的第三个元素,放入到func函数中继续运算,以此类推
    参数:
        func:自定义函数或者内置函数
        iterable:可迭代数据
    返回值:最终的运算处理结果
    注意:使用 reduce函数时,需要导入 from functools import reduce
'''
from functools import reduce

# [5,1,3,2] =>5132
# 普通方法
varlist = [5, 1, 3, 2]
res = ''
for i in varlist:
    res += str(i)
print(int(res))  # 5132


# 使用reduce()
def func_reduce(x, y):
    return x * 10 + y


res = reduce(func_reduce, varlist)
print(res)  # 5132
# 优化
res = reduce(lambda x, y: 10 * x + y, varlist)
print(res)  # 5132


'''
4. filter(func,iterable)过滤函数
    功能:过滤数据,把iterable中的每个元素拿到func函数中进行处理,如果函数返回True则保留这个数据,返回False则丢弃这个数据
    参数:
        func 函数
        iterable:可迭代的数据
    返回值:保留下来的数据组成的迭代器
'''
# 要求:保留所有的偶数,丢弃所有的奇数
varlist = [1,2,3,4,5,6,7,8,9]
# 普通方法
newlist = []
for i in varlist:
    if i % 2 == 0:
        newlist.append(i)
print(newlist)  # [2, 4, 6, 8]


# 使用filter
def func_filter(n):
    if n % 2 == 0:
        return True
    else:
        return False

it = filter(func_filter,varlist)
print(list(it))  # [2, 4, 6, 8]

# 优化
it1 = list(filter(lambda x: True if x % 2 == 0 else False, varlist))
print(it1)