# coding:utf-8
# 切片(顾头不顾尾),切片出来的列表是个全新的列表,即使是全且整个列表也一样
l1 = [1, 2, 3, 4, 5, 7]
print(l1[0:3:2])  # [1, 2, 3]

# len 长度
print(len(l1))  # 6

# 成员运算 in , not in
print(2 in l1)  # True

# 查看列表某个元素的个数 count
print(l1.count(0))  # 0

# 在列表中从左至右查找指定元素,找到了返回该值的下标/索引,
# index (查询元素,起始位置,结束位置) 不写默认全部
print(l1.index(2, 0, -1))  # 2
# print(l1.index(6, 0, -1))  # 没有找到会报错,ValueError: 6 is not in list

# 增
# append(元素) 列表末尾追加
l1.append(6)
print(l1)  # [1, 2, 3, 4, 5, 7, 6]
# insert(索引,元素) 往指定索引位置插入一个元素
l1.insert(0, '大海')
print(l1)  # ['大海', 1, 2, 3, 4, 5, 7, 6]
# extend()_往列表当中添加多个元素,括号里放列表,也是末尾追加
l1.extend(['蓝天', '白云'])
print(l1)  # ['大海', 1, 2, 3, 4, 5, 7, 6, '蓝天', '白云']

# 删
# del l1[0]
# 指定删除 remove()
l1.remove('白云')
print(l1)  # ['大海', 1, 2, 3, 4, 5, 7, 6, '蓝天']
# pop 从列表里面拿走一个值
l1.pop()
# 按照索引删除值,默认是删除最后一个, 相当于 l1.pop(-1)

# 清空列表
# l1.clear()

# 改
l1[2] = '红海'

# 反序 reverse
l1.reverse()
print(l1)

# sort 排序,对数字
list_num = [1, 3, 4, 2]
list_num.sort(reverse=True)  # 反序
print(list_num)  # [4, 3, 2, 1]
list_num.sort(reverse=False)  # 正序
print(list_num)  # [1, 2, 3, 4]

# 列表(元组)之间的累加与乘法
names = ('xiaoma', 123, 'xiaoming')
names_add = names + names
names_c = names * 3
print(names_add)
print(names_c)
names_list = ['xiaoma', 'xiaoming']
names_list += ['xiaowang']
print(names_list)  # ['xiaoma', 'xiaoming', 'xiaowang']

'''
copy 将当前的列表复制一份相同的列表,新列表与旧列表内容相同,但内存空间不同
用法 list.copy()-> 该函数无参数,返回一个一模一样的列表
copy():浅拷贝,  copy.deepcopy():深拷贝
多层嵌套的列表,如果改变嵌套列表里的元素的话,浅拷贝的新列表会发生变化,但深拷贝的新列表则不会变化
'''
varlist = [1, 2, 3, 4]
# 简单的拷贝,就可以把列表复制一份,复制的是新列表,只是两个列表相同
newlist = varlist.copy()
print(newlist, id(newlist))  # [1, 2, 3, 4] 3175375254144
print(varlist, id(varlist))  # [1, 2, 3, 4] 3175375254016

# 多维列表
varlist_duo = [1, 2, 3, [4, 5, 6]]
newlist_duo = varlist_duo.copy()
print(newlist_duo)  # [1, 2, 3, [4, 5, 6]]
# 删除原来多维列表中的嵌套列表里的元素
del varlist_duo[3][1]
# 拷贝的列表也发生了变化
print(newlist_duo)  # [1, 2, 3, [4, 6]]

# 深拷贝,使用深拷贝需要导入copy
import copy

newlist_duo_dc = copy.deepcopy(varlist_duo)
print(newlist_duo_dc)  # [1, 2, 3, [4, 6]]
# 删除原来多维列表中的嵌套列表里的元素
del varlist_duo[3][1]
# 深拷贝的列表未发生变化
print(newlist_duo_dc)  # [1, 2, 3, [4, 6]]

# 列表推导式,提供一个更简单的创建列表的方法(采用一种表达式的方式,对数据进行过滤或处理,并且把结果组成一个新的列表

# 1. 创建0-9的平方的列表
# 普通方法
varlist = []
for i in range(0, 10):
    varlist.append(i ** 2)
print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 使用map和lambda
varlist = list(map(lambda x: x ** 2, range(10)))
print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
# 列表推导式
varlist = [i ** 2 for i in range(10)]
print(varlist)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 2. '1234'==> [2,4,6,8]
varlist = [int(i) * 2 for i in '1234']
print(varlist)
# 位运算   00001 << 1 =00010 左移1位
varlist = [int(i) << 1 for i in '1234']
print(varlist)  # [2, 4, 6, 8]

# 3.带有判断条件的列表推导式
# 变量 = [变量或变量的处理结果 for i in 容器类型数据 条件表达式]

# 0-9 求所有的偶数
# 一.
newlist = []
for i in range(0, 10):
    if i % 2 == 0:
        newlist.append(i)
print(newlist)  # [0, 2, 4, 6, 8]
# 二.
newlist = [i for i in range(10) if i % 2 == 0]
print(newlist)  # [0, 2, 4, 6, 8]

# 4.带有条件判断的多循环的推导式
# [1,2,3],[3,1,4] ==> 把两个列表中的元素,两两组合,要求组合的元素不能重复
# 常规方法
newlist = []
for x in [1, 2, 3]:
    for y in [3, 1, 4]:
        if x != y:
            newlist.append((x, y))
print(newlist)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
# 列表推导式
newlist = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
print(newlist)  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

# 对于嵌套循环的列表推导式
# 把下面的矩阵,行转列,列转行

arr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
res_list = []
for i in range(4):
    newlist = []
    for row in arr:
        newlist.append(row[i])
    res_list.append(newlist)
print(res_list)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

# 使用列表推导式
newlist = [[row[i] for row in arr]for i in range(4)]
print(newlist)  # [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]