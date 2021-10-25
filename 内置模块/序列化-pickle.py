# coding:utf-8

import pickle
'''
什么是序列化?为什么要序列化?
pickle模块提供的函数
    dumps()序列化,返回一个序列化后的二进制数据,可以把一个python的任意对象序列化称为一个二进制
    loads()序列化,返回一个反序列化后的python对象,可以把一个序列化后的二进制数据反序列化为python的对象
    dump() 序列化,把一个数据对象进行序列化并写入到文件中
        参数1:需要序列化的数据对象
        参数2:写入的文件对象
        pickle.dump(var,fp)
    load() 反序列化,在一个文件中读取序列化数据,并且完成一个反序列化
        参数:读取的文件对象
        返回值:文件读取的内容
        res = pickle.load(fp)

'''

vars = 'i love you'
# 1. 转化成二进制
res = pickle.dumps(vars)
print(res, type(res))
# b'\x80\x04\x95\x0e\x00\x00\x00\x00\x00\x00\x00\x8c\ni love you\x94.' <class 'bytes'>

# 反序列化loads
res_loads = pickle.loads(res)
print(res_loads,type(res_loads))  # i love you <class 'str'>

# 如何把一个python数据进行序列化后写入文件?并且再次读取出来
# 1. 使用dumps loads 方法完成
# 定义数据
vars = {'name': '张三', 'age': 20, 'sex': 'm'}
# 进行序列化
res_dumps = pickle.dumps(vars)
# 写入文件
with open("./data.txt", 'wb') as fp:
    fp.write(res_dumps)
# 读取
with open("./data.txt", 'rb') as rf:
    res_read = rf.read()
res_loads = pickle.loads(res_read)
print(res_loads)  # {'name': '张三', 'age': 20, 'sex': 'm'}

# 2. 使用load,dump
vars = {'name': '张三', 'age': 20, 'sex': 'm'}
with open("./data2.txt", 'wb') as fp:
    pickle.dump(vars, fp)
with open("./data.txt", 'rb') as rf:
    res_load = pickle.load(rf)
print(res_load)

