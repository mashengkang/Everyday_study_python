# coding:utf-8

'''
集合类型:确定的一组无序的数据的组合
    当前集合中的元素的值不能重复
    由多个数据组合的复合型数据(容器类型数据)
    集合中的数据没有顺序
'''

# 集合的定义
'''
可以直接使用{}来定义集合
可以使用set()进行集合的定义和转换
使用集合推导式完成集合的定义
注意:集合中的元素不能重复,集合中存放的数据,Number,String,Tuple
'''
# 定义集合
vars = {1, 2, 3, 'abc', 'love', True, (1, 2, 3), 0, False, 3.1415, 123}
print(vars)  # {0, 1, 2, 3, 3.1415, (1, 2, 3), 'abc', 'love', 123}
# 1.无序
# 2. False在集合中表示0,所以0和Flase只能存在一个,True表示1,所以和1也只能存在一个

# 检测集合中的值
res1 = '123' in vars
res2  = '123' not in vars

# 获取集合中的元素的个数 len()
res_len = len(vars)
print(res_len)  # 9

# 集合的遍历
for i in vars:
    print(i)

# 向集合中追加元素
vars.add('def')
print(vars)  # {0, 1, 2, 3, 3.1415, (1, 2, 3), 123, 'def', 'love', 'abc'}

# 删除集合中的元素
# res_pop = vars.pop()
# print(res_pop) # 随机删除,返回值:删除的值

# 指定删除集合中的元素,remove(),返回None,不存在则报错
# vars.remove('abc')
print(vars)
# 指定删除集合中的元素,discard(),不存在也不会报错
# vars.discard('sdf')
print(vars)

# 清空
vars.clear()
print(vars)  # set()

# update(others) 更新集合.添加来自others中的所有集合,others必须是容器类型
vars.update({1, 2, 3, 4})
print(vars)

'''
集合中的拷贝并不存在深拷贝的问题
    因为集合中的元素都是不可变类型的,包括元组和冰冻集合
    不存在拷贝后,对集合中不可变的二级容器进行操作的问题
'''
res = vars.copy()
print(res)
print(res is vars)  # False

# 冰冻集合,是不可变类型的集合,set是可变类型的集合
'''
定义冰冻集合,只能使用frozenset()函数进行冰冻集合的定义
    冰冻集合不可修改
    冰冻集合只能做集合相关的运算:求交集,差集
    frozenset()本身就是一个强制转换类型的函数,可以把其他任何容器类型的数据转为冰冻集合
'''
v = frozenset([1,2,3])
print(v)  # frozenset({1, 2, 3})

# 遍历,无序
for i in v:
    print(i)

# 冰冻集合的推导式
res = frozenset({i << 1 for i in v})
print(res)  # frozenset({2, 4, 6})


# 集合的运算
'''
运算  符号   函数
交集   &    set.intersection()       set.intersection_update()
并集   |    union()                  update()
差集   -    difference()             difference_update()
对称差集     symmetric_difference()   symmetric_difference_update()
'''

var1 = {'黎明','刘德华','张学友', '郭富城', '大脚'}
var2 = {'赵四', '刘能', '小沈阳', '宋小宝', '大脚'}

# 求交集
res = var1 & var2
print(res)  # {'大脚'}

# 求并集,就是把多个集合中所有的元素集中放在一个集合中(去除重复)
res = var1 | var2
print(res)  # {'刘德华', '赵四', '郭富城', '刘能', '大脚', '张学友', '黎明', '小沈阳', '宋小宝'}

# 求差集 a-b ==> 求 a 中有但 b 中没有的元素
res1 = var1 - var2 # 求 var1 有 var2 没有的元素
print(res1)  # {'刘德华', '黎明', '郭富城', '张学友'}
res2 = var2 - var1
print(res2)  # {'小沈阳', '宋小宝', '赵四', '刘能'}

# 对称差集 (与交集相反,取两个集合中不是都有的元素)
res = var1 ^ var2
print(res)  # {'刘德华', '刘能', '宋小宝', '小沈阳', '张学友', '郭富城', '赵四', '黎明'}


# 交集运算的函数

# set1.intersection(set2) 返回交集的结果,新的集合
res = var1.intersection(var2)
print(res)  # {'大脚'}

# set1.intersection_update(set2)
# 没有返回值,计算两个集合的相交部分,并把计算结果重新赋值给第一个集合(就是求出来的交集直接赋值给了set1,更改了set1集合)
# res = var1.intersection_update(var2)
print(res)  # None
print(var1)  # {'大脚'}

# 并集运算函数 union() update()
res = var1.union(var2) # 返回并集结果,新的集合
print(res)  # {'大脚', '郭富城', '刘德华', '张学友', '刘能', '小沈阳', '宋小宝', '黎明', '赵四'}
# set1.update(set2)
# 没有返回值,计算两个集合所有元素,并把计算结果重新赋值给第一个集合(就是求出来的集合直接赋值给了set1,更改了set1集合)
# var1.update(var2)
print(var1)  # {'赵四', '小沈阳', '郭富城', '大脚', '张学友', '黎明', '刘能', '宋小宝', '刘德华'}

# 差集运算函数
res = var1.difference(var2)
print(res)  # {'刘德华', '郭富城', '张学友', '黎明'}
# var1.difference_update(var2)  # 把差集的结果重新赋值给var1
print(var1)  # {'张学友', '郭富城', '刘德华', '黎明'}

# 对称差集的函数
res = var1.symmetric_difference(var2)
print(res)  # {'黎明', '郭富城', '刘能', '小沈阳', '刘德华', '赵四', '张学友', '宋小宝'}
var1.symmetric_difference_update(var2)
print(var1)  # {'刘德华', '黎明', '郭富城', '宋小宝', '小沈阳', '赵四', '张学友', '刘能'}

# 检测 超集(父集) 子集
var1 = {1,2,3,4,5,6,7,8,9}
var2 = {1,2,3}

# issuperset() 超集
res1 = var1.issuperset(var2) # 检测var1是不是var2的超集
res2 = var2.issuperset(var1)
print(res1)  # True
print(res2)  # False

# issubset() 子集
res_s = var2.issubset(var1)
print(res_s)  # True

# 检测两个集合是否不相交,不相交返回True,相交返回False
res = var1.isdisjoint(var2)
print(res)  # False
