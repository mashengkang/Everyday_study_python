# coding:utf-8

a_1 = 1
a_2 = 0
print(bool(a_1))  # True
print(bool(a_2))  # False
print(bool(not a_1))  # False
print(bool(not a_2))  # True

b_1 = '1'
b_2 = ''
print('-----')
print(bool(b_1))  # True
print(bool(b_2))  # False

# 字典,列表,元组,判断如果不为空则为True