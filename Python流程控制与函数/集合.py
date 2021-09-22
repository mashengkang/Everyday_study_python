# coding:utf-8

'''
集合无法通过索引获取元素,集合是无序的
集合无获取元素的任何方法
集合只是用来处理列表或元组的一种临时类型,不适合存储与传输
'''

# add 的功能,用于集合中添加一个元素,若已存在这个元素,则不执行这个函数
# 用法:set.add(item) =>item 要添加的元素,无返回值
a_list = ['python', 'django', 'django', 'flask']
a_set = set()
a_set.add(a_list[0])
a_set.add(a_list[1])
a_set.add(a_list[2])
a_set.add(a_list[-1])
print(a_set)  # {'python', 'flask', 'django'}
a_set.add(True)
a_set.add(None)
print(a_set)  # {True, 'django', None, 'flask', 'python'}

# update 加入一个新的集合(或列表,元组,字符串),如新集合内的元素在原集合中存在则无视
# 用法: set.update(iterable)=> iterable:集合,列表元组字符串
a_tuple = ('a', 'b', 'c')
a_set.update(a_tuple)
print(a_set)  # {True, 'django', None, 'flask', 'b', 'c', 'a', 'python'}
a_set.update('python')
print(a_set)  # {'b', True, 'a', 'o', None, 'python', 'y', 'n', 'django', 'flask', 'p', 't', 'c', 'h'}

# remove 删除集合中某个元素,若不存在则报错
# set.remove(item) 无返回值,直接作用于原集合,若集合中没有item则报错
a_set.remove('python')
print(a_set)  # {'c', True, 'a', 'p', 'flask', None, 'y', 't', 'b', 'h', 'o', 'n', 'django'}

# clear 清空
# set.clear()

# del 删除集合这个自身对象
b_set = {1, 2, 3}
del b_set
# print(b_set)  # NameError: name 'b_set' is not defined

# 集合的交集 intersection
# a_set.intersection(b_set,...) 返回值是set类型
a_set = {1, 2, 3, 4}
b_set = {6, 7, 5, 4}
c_set = {8, 9, 5, 4}
res_set = a_set.intersection(b_set, c_set)
print(res_set)  # {4}

# 集合的并集 union 多个集合的所有元素的集合,重复的元素只取一个
# a_set.union(b_set, c_set,...) 返回值是set类型
res_set2 = a_set.union(b_set, c_set)
print(res_set2)  # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# isdisjoint 判断两个集合是否包含相同的元素,如果没有返回True,否则返回False
# a_set.isdisjoint(b_set)
res_set3 = a_set.isdisjoint(b_set)
print(res_set3)  # False 