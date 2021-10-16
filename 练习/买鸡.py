# coding:utf-8
'''
一共100块钱,需要买100只鸡,多少种方案
公鸡,3元==>33只
母鸡,1元==>100只
小鸡,0.2元==>200只
'''

from time import time

# 1.
num = 0
count = 0
starttime = time()
for gj in range(0, 34):
    for mj in range(0, 101):
        for xj in range(0, 201):
            count += 1
            # 判断
            if gj+mj+xj == 100 and gj*3 + mj*1 + xj*0.5 == 100:
                print(f'公鸡{gj}只,母鸡{mj}只,小鸡{xj}只,')
                num += 1
endtime = time()
print(num)
print(count)  # 690234
print(endtime - starttime)  # 0.1017615795135498

# 2.优化
num = 0
count = 0
starttime = time()
for gj in range(0, 34):
    for mj in range(0, 101):
        xj = 100 - gj - mj
        count += 1
        # 判断
        if gj * 3 + mj * 1 + xj * 0.5 == 100:
            print(f'公鸡{gj}只,母鸡{mj}只,小鸡{xj}只,')
            num += 1
endtime = time()
print(num)
print(count)  # 3434 运算
print(endtime - starttime)  # 0.0009918212890625
