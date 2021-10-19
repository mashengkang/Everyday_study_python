# coding:utf-8

# 使用 生成器函数改写,斐波那契数列

# 常规
# def feibo(num):
#     a, b, i = 0, 1, 0
#     while i < num:
#         print(b, end=",")
#         a, b = b, a+b
#         i += 1
# feibo(7)  # 1,1,2,3,5,8,13,

# 使用生成器改写
def feibo(num):
    a, b, i = 0, 1, 0
    while i < num:
        yield b
        a, b = b, a+b
        i += 1
res = feibo(7)
print(res)  # <generator object feibo at 0x00000183E277CE40>
print(list(res))  # [1, 1, 2, 3, 5, 8, 13]


