# 字典:dict
# 作用:记录多个key:value值,优势是每一个值value都有其对应关系
# 定义: 在{}内用逗号分割开多个key:value 元素,其中value可以是任意的数据类型,key必须是不可变类型
info = {'name': '大海', 'age': 19}
print(info)

print(info['name'])

# 列表和字典的区别: 列表是依靠索引,字典是依靠键值对
# 注意字典的key必须是不可变的类型,key无法提取
# info1 = {[1,2,3]:'蓝天'} # 错误
info2 = {(1, 2, 3): '蓝天'}  # 正确

# 生成字典的方式
dict1 = dict(x=1, y=2, z=3)  # 关键字传参的方式
print(dict1)  # {'x': 1, 'y': 2, 'z': 3}
# zip压缩函数,dict转类型
var1 = [1, 2, 3, 4]
var2 = ['a', 'b', 'c', 'd']
print(dict(zip(var1, var2)))  # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

# 字典的增加操作
info['addr'] = '长沙'
print(info)  # {'name': '大海', 'age': 19, 'addr': '长沙'}

# 字典是可变数据类型
# 字典的len查看的是键值对的个数
print(len(info))

# 成员运算in ,not in 字典的成员运算判断的是key,不是value,返回值是布尔类型
print('name' in info)  # Ture

# 删
# clear 清空字典
# info.clear()

# del 通用
# del info['name']
# print(info) # {'age': 19, 'addr': '长沙'}
# 删除不存在的key会报错
# del info['xxx']
# print(info)  # KeyError: 'xxx' 报错

# pop 删除,返回值是value, 实际上就是拿走了字典的value
res = info.pop('addr')
print(info)  # {'name': '大海', 'age': 19}
print(res)  # 长沙
# 删除不存在的key会报错
# info.pop('xxx')

# popitem 最后一对键值对删除,字典无序, 返回的是一个元组(内容是键值对),如果字典为空,则会报错
res1 = info.popitem()
print(info)
print(res1)

# 改
info['name'] = '红海'
print(info)
# update 该函数无返回值
info.update({'name': '小海', 'age': 13})
print(info)  # {'name': '小海', 'age': 13}

# dict.setdefault(key,value) 返回值为key所对应的value,如果dict中存在key,则会返回原字典中key对应的value,
# 如果dict中没有这个key,则会在字典中添加进这对键值对,并返回新的value
new_value1 = info.setdefault('name', 'xiaoma')
new_value2 = info.setdefault('sex', '男')
print(new_value1)  # 小海
print(new_value2)  # 男
print(info)  # {'name': '小海', 'age': 13, 'sex': '男'}

# values():获取当前字典中所有键值对中的值(value)
# 用法: dict.values() -> 无需传参,返回一个value集合的伪列表
print(info.values())  # dict_values(['小海', 13, '男'])
# 返回的这个值只能用来观察,无法像操作列表一样直接操作它,但是可以通过list()函数格式化它

# keys():获取当前字典中所有键值对中的值
print(info.keys())  # dict_keys(['name', 'age', 'sex'])
print(list(info.keys()))  # ['name', 'age', 'sex']
print('---------')

# []的获取方法
name = info['name']
print(name)  # 小海

# get用法: dict.get(key,default=None)
# key:需要获取value的key, default:key不存在则返回默认值,默认是None,也可以自定义
# 使用[]和get()两种不同的方式对value进行查看,[]方法如果获取的key不存在,则直接报错,get()获取的key不存在则返回default的信息
print(info.get('name'))

# 字典的copy
# dict.copy() -> 该函数无参数,返回一个一样的内存地址不同的字典
fruits = {
    'apple': 30,
    'banana': 50,
    'pear': 100
}
real_fruits = fruits.copy()
print(real_fruits)
real_fruits['orange'] = 50
real_fruits.update({'cherry': 100})
print(real_fruits)  # {'apple': 30, 'banana': 50, 'pear': 100, 'orange': 50, 'cherry': 100}
print(fruits)  # {'apple': 30, 'banana': 50, 'pear': 100}
real_fruits['apple'] = real_fruits['apple'] - 5
print(real_fruits)  # {'apple': 25, 'banana': 50, 'pear': 100, 'orange': 50, 'cherry': 100}
real_fruits.clear()
print(real_fruits)  # {}

# 字典推导式
# 把字典中的键值对位置进行交换
vardict = {'a': 1, 'b': 2, 'c': 3}
newdict = {}

# 普通方法
for k, v in vardict.items():  # vardict.items() = # dict_items([('a', 1), ('b', 2), ('c', 3)])
    newdict[v] = k
print(newdict)

# 使用字典推导式
newdict = {v: k for k, v in vardict.items()}
print(newdict)  # {1: 'a', 2: 'b', 3: 'c'}

# 注意:一下推导式,返回的结果是一个集合,集合推导式
newdict = {v for k, v in vardict.items()}
print(type(newdict))  # <class 'set'>

# 把以下字典中是偶数的值,保留下来,并且交换键值对的位置
vardict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 普通方法
# newlist = {}
# for k, v in vardict.items():
#     if v % 2 == 0:
#         newlist[v] = k
#     else:
#         newlist[k] = v
# print(newlist)  # {'a': 1, 2: 'b', 'c': 3, 4: 'd'}

# 字典推导式
newlist = {v: k for k, v in vardict.items() if v % 2 == 0}
print(newlist)



