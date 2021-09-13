# coding:utf-8
# 字符串是不可被修改的,所有的函数都是生成新的字符串

#  1.capitalize 只能是字符串
#  只对字符串 ,将首字母大写
name = 'xiao ma'
info = 'hello 小马'
_info = '小马 hello'
new_str = '1314'
new_name = name.capitalize()
new_info = info.capitalize()
_new_info = _info.capitalize()
new_new_str = new_str.capitalize()
print(new_name, name)  # Xiao ma xiao ma
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
info= 'this is a string'
result = info.startswith('this')
print(result)  # True
print(info.startswith('this is a string'))  # True

# 8. find 和index
# srting.find(item) ->item:你想查询的元素,返回一个整型(所在位置下标)
# srting.index(item) ->item:你想查询的元素,返回一个整型(所在位置下标).或者报错
# find 找不到元素会返回-1 , index找不到元素会报错
info = 'python is a good code'
result = info.find('a')
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

