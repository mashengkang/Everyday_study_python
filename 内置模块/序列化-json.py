# coding:utf-8

'''
JSON
    是一个受JavaScript 的对象字面量语法启发的轻量级数据交换格式
    在js语言中是一个对象的表示方法,和python中的字典的定义规则和语法都很像
    在互联网中又是一种通用的数据交换,数据传输,数据定义的一种数据格式

'''

# 一下语法格式定义的是一个 字典 数据类型
vardict = {'name': '张三', 'age': 20, 'sex': '男'}

import json

# json 模块 dumps方法进行转换
res = json.dumps(vardict)
print(res,type(res))  # {"name": "\u5f20\u4e09", "age": 20, "sex": "\u7537"} <class 'str'>

# 反转换
res = json.loads(res)
print(res,type(res))  # {'name': '张三', 'age': 20, 'sex': '男'} <class 'dict'>

# 写
vardict = [{'name': '张三', 'age': 20, 'sex': '男'}, {'name': '李四', 'age': 22, 'sex': '女'}]
with open("./data.json", 'w') as fp:
    json.dump(vardict, fp)

# 读
with open("./data.json", 'r') as rp:
    res = json.load(rp)
    print(res)