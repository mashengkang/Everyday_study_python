# coding:utf-8
# 字符串是不可被修改的,所有的函数都是生成新的字符串

#  1.capitalize 只能是字符串
#  只对字符串 ,将首字母大写,后面的全部小写
name = 'xiao Ma'
info = 'hello 小马'
_info = '小马 hello'
new_str = '1314'
new_name = name.capitalize()
new_info = info.capitalize()
_new_info = _info.capitalize()
new_new_str = new_str.capitalize()
print(new_name, name)  # Xiao ma xiao Ma
# print(new_info, info)
# print(_new_info, _info)
# print(new_str, new_new_str)

# 2.casefold 与lower 的用法 (将所有字符串字母小写)
# 用法: newstr = string.casefold()
#       newstr = string.lower()
# 只对字符串字母有效,已经小写的则无效
message_en = "How do you do?"
message_ch = "你好呀"
message_mix = '你好,HELLO'
message_en_lower = message_en.lower()
message_en_casefold = message_en.casefold()
message_mix_casefold = message_mix.casefold()
# print(message_en_lower)
# print(message_en_casefold)
print(message_mix_casefold)  # 你好,hello

# 3.upper 将字符串中的字母全部大写
# 用法:big_str = string.upper()
name2 = 'xiaoma2'
new_name2 = name2.upper()
print(new_name2)

# 4.swapcase 将字符串中的字母大小写进行转换
name3 = 'XiaoMa'
new_name3 = name3.swapcase()
print(new_name3)  # xIAOmA

# 5.zfill 为字符串定义长度,如不满足,不足的部分用0代替,如果定义长度小于当前字符串长度,则不发生变化
# newstr = string.zfill(width) width:新字符串设定的长度
new_name4 = name3.zfill(11)
print(new_name4)  # 00000XiaoMa
print(name3.zfill(3))  # XiaoMa

# 6.count 返回当前字符串某个元素的个数
# inttype = string.count(item)  item:所查的元素
info = 'ejgqoinvcaw4ewvbmarkjqiarodc,anfoijwerofiadansdwenfas'
print(info.count('a'))  # 7

# 7.startswith endswith 判断字符串 开始/结尾 是否是某成员(元素)
# bool_str = string.startswith(item) ->item:你想查询的元素,返回布尔值
info = 'this is a string'
result = info.startswith('this')
print(result)  # True
print(info.startswith('this is a string'))  # True

# 8. find(rfind) 和index(index)
# srting.find(item,start,end) ->item:你想查询的元素,返回一个整型(所在位置下标),start字符串查询的开始位置,end查询的结束位置
# srting.index(item) ->item:你想查询的元素,返回一个整型(所在位置下标).或者报错
# find 找不到元素会返回-1 , index找不到元素会报错,
# find 若字符串中出现多次查询的元素,只返回第一次出现的位置
info = 'python is a good code'
result = info.find('a')
print('----------')
result2 = info.rfind('o', 1, 20)  # 18
print(result2)
print(result)  # 10
print(info.find('ok'))  # -1
# print(info.index('ok'))  # ValueError: substring not found

# 9. strip  lstrip  rstrip   只能去掉字符串两侧的元素,
# newstr = string.strip(item) 括号里需要传一个你想去掉的元素,如不填写则表示去掉字符串两端的空格,中间的空格不会去掉
# 传入的元素如果不在两侧,则没有效果
info = ' xiao ma  '
new1_info = info.strip()
new2_info = info.strip(' ')
print('.' + new1_info + '.')  # .xiao ma.
print('.' + new2_info + '.')  # .xiao ma.

# 10. replace
# new_str = string.replace(old, new, max)
# old:被替换的元素,new:新元素 max:可选,代表替换几个,默认全部替换所有old元素
str_1 = 'hello xiaoma'
new_str_1 = str_1.replace('l', '0', 1)
print(new_str_1)  # he0lo xiaoma

# 11.isspace 判断字符串是否是一个由空格组成的字符串(空格不是空字符串)
# print(' '.isspace())  # true
# 12. istitle 判断字符串是否是一个标题类型 即首字母大写,只用于英文
# 13. isupper   islower 判断字符串是否都是由大写/小写字母组成,返回bool类型
title = 'Back Of China'
upper_str = 'PYTHON IS A GOOD CODE 哈哈!'
lower_str = 'i love you'
print(title.istitle())  # True 所有单词的首字母都是大写才是True
print(upper_str.isupper())  # True 只判断单词,中文和标点不作判断

# 14.字符的编码格式
# gbk:中文编码 ascii:英文编码
# utf-8 是一种国际通用的编码格式

# 15. 字符串的格式化
""" 
%c 格式化字符 字母只支持一个字母(print('%c' % 'a')) 数字从1到999999
%u 格式化无符号整型(正整型)
%f 格式化浮点型
%d 格式化整型
%s 格式化字符串,通用类型
%o 格式化无符号八进制数
%x 格式化无符号十六进制
%e 科学计数法格式化浮点数
"""
print('%c' % 1020)
print('%c' % 'b')
print('%u' % -1)
print('%f' % 3.14)  # 3.140000 小数点后6位
print('%d' % 10.9)  # 10 向下取整
print('%s' % 123)
print('%s' % '123.1')
print('{:d}'.format(1))  # 1
print('{:f}'.format(1.2))  # 1.200000

# 16. 转义字符 格式:\+字符
"""
\n 换行,一般用于末尾,strip对其也有效
\t 横向制表符(可以认为是要给间隔符,默认就是table键缩进)
\v 纵向制表符(会有一个男性符号)
\a 响铃
\b 退格符,将光标前移,覆盖(删除前一个)
\r 回车,代表光标的位置(从\r出现的位置开始作为光标的起点
\f 翻页(几乎用不到)
\' 转义字符串中的单引号
\" 转义字符串中的双引号
\\ 转义斜杠
"""
info1 = ('my name '
       'is xiaoma')
info2 = ('my name \nis xiaoma')
print(info1)  # my name is xiaoma 没有换行
print(info2) # 有换行
info_b = 'my name is x\biaoma'
print(info_b)  # my name is iaoma  \b前的字符被删除
print('my name is \'xiaoma\'')  # my name is 'xiaoma'
print('my name is \\ xiaoma')  # my name is \ xiaoma
# 转义无效符号 在字符串前面加r,则使转义字符无效
print(r'my name \tis xiaoma')  # my name \nis xiaoma
print('my name \tis xiaoma')  # my name 	is xiaoma
print('岁月是把杀猪刀,\r任谁都没有办法')  # 任谁都没有办法

# 17 split() 按照指定的字符进行分割,把一个字符串分割成一个列表
vars1 = 'user_admin_id_123'
vars2 = 'uid=123&type=ab&kw=hh'

# str.split()
res1 = vars1.split('_')
print(res1)  # ['user', 'admin', 'id', '123']
print(vars1.split("_", 1))  # ['user', 'admin_id_123']

res2 = vars2.split('&')
for i in res2:
       print(i.split('='), end=' ')  # ['uid', '123'] ['type', 'ab'] ['kw', 'hh']

arr = ['user', 'admin', 'id', '123']
# str.join() 按照指定的字符,把容器类型中的数据连接成一个字符串
res_arr = '='.join(arr)
print(res_arr)  # user=admin=id=123
