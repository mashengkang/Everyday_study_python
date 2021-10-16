# coding:utf-8

# 斐波那契数列
"""
0, 1, 1, 2, 3, 5, 8...
"""
# 获取用户输入的数据
nums = int(input('你需要计算几项:'))
n1 = 0
n2 = 1
count = 2
# 从之后的数据开始
if nums <= 0:
    print('请输入一个正整数')
elif nums == 1:
    print(f'斐波那契数列:{n1}')
elif nums == 2:
    print(f'斐波那契数列:{n1},{n2}', end=',')
else:
    print(f'斐波那契数列:{n1},{n2}', end=',')
    while count < nums:
        n3 = n1 + n2
        print(n3, end=',')
        # 更新
        n1, n2 = n2, n3
        count += 1

