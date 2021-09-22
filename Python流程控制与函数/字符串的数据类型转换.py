# coding:utf-8

# 相互转换时,字符串只能有数字或小数,不可以有其他的
# 转换函数 (和数字间的转换)
"""
整型   => 字符串  str  new_str = str(123)
浮点型 => 字符串  str  new_str = str(3.14)
字符串 => 整型    int  new_int = int('12')
字符串 => 浮点型  float new_float = float('1.2')
"""

int_data = 12
float_data = 3.14
str_int_data = str(int_data)
str_float_data = str(float_data)
print(str_int_data, str_float_data, type(str_int_data), type(str_float_data))
# 12 3.14 <class 'str'> <class 'str'>

str_float = '3.14'
str_int = '123'
real_float = float(str_float)
real_int = int(str_int)
print(real_float, real_int)
# 3.14 123

# 比特类型 bytes
a = 'hello xiaoma'
print(a, type(a))  # hello xiaoma <class 'str'>
b = b'hello xiaoma'
print(b, type(b))  # b'hello xiaoma' <class 'bytes'>
print(b.replace(b'xiaoma', b'xiaohu'))  # b'hello xiaohu'
print(b[3])  # 108
print(b[:3])  # b'hel'
print(b.find(b'x'))  # 6

# dir 函数 显示出来所有的对象的属性
print(dir(b))

# 字符串转bytes的函数->encode
"""
用法: string.encode(encoding='utf-8', errors='strict'
参数:encoding:转换成的编码格式,如ascii, gbk, 默认utf-8
    errors:  出错时的处理方法,默认strict,直接抛错误,也可以选择ignore忽略错误
返回值:返回一个比特(bytes)类型
"""

# bytes转字符串的函数->decode
"""
用法: string.decode(encoding='utf-8', errors='strict'
参数:encoding:转换成的编码格式,如ascii, gbk, 默认utf-8
    errors:  出错时的处理方法,默认strict,直接抛错误,也可以选择ignore忽略错误
返回值:返回一个比特(bytes)类型
"""
c = 'hello 小马'
d = c.encode('utf-8')
print(d, type(d))  # b'hello \xe5\xb0\x8f\xe9\xa9\xac' <class 'bytes'>
print(d.decode('utf-8'))  # hello 小马