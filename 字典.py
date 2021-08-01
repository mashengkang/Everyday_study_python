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

info.update({'name': '小海'})
print(info)
