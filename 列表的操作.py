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

# copy 将当前的列表复制一份相同的列表,新列表与旧列表内容相同,但内存空间不同
# 用法 list.copy()-> 该函数无参数,返回一个一模一样的列表
# copy():浅拷贝,deepcopy():深拷贝
# 多层嵌套的列表,如果改变嵌套列表里的元素的话,浅拷贝的新列表会发生变化,但深拷贝的新列表则不会变化
