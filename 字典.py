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
dict1 = dict(x=1, y=2, z=3)
print(dict1)  # {'x': 1, 'y': 2, 'z': 3}

# 字典的增加操作
info['addr'] = '长沙'
print(info)  # {'name': '大海', 'age': 19, 'addr': '长沙'}

# 字典是可变数据类型
# 字典的len查看的是键值对的个数
print(len(info))

# 成员运算in ,not in 字典的成员运算判断的是key,返回值是布尔类型
print('name' in info)

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

# popitem 最后一对键值对删除,字典无序, 返回的是一个元组
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
print(info.values())
# dict_values(['小海', 13, '男'])
# 返回的这个值只能用来观察,无法像操作列表一样直接操作它,但是可以通过list()函数格式化它

# []的获取方法
name = info['name']
print(name)  # 小海
# get用法: dict.get(key,default=None)
# key:需要获取value的key, default:key不存在则返回默认值,默认是None,也可以自定义
# 使用[]和get()两种不同的方式对value进行查看,[]方法如果获取的key不存在,则直接报错,get()获取的key不存在则返回default的信息

