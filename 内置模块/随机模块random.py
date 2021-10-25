# coding:utf-8

import random

# 随机数的应用场景:数字验证码,高并发下的订单号...

# random.random() 返回 0-1 之间的随机小数(左闭右开)
res = random.random()
print(res)  # 0.15234874497486495

# random.randrange([开始值],结束值,[步进值]) 随机获取指定范围内的整数,开始值省略的话,默认是0,左闭右开
res1 = random.randrange(5)
res2 = random.randrange(5, 10)  # [5~10)的整数
res3 = random.randrange(5, 10, 2)  # 只能返回5,7,9
print(res3)

# random.randint() 随机产生指定范围内的随机整数
res = random.randint(1,12)
print(res)

# random.uniform() 获取指定返回内的随机小数
res_uni = random.uniform(1, 3)
print(res_uni)  # 2.790554681017254

# random.choice() 随机获取容器类型中的值
res_cho1 = random.choice('123')
res_cho2 = random.choice([1,2,3])
print(res_cho1,res_cho2)  # 3 1

# random.shuffle() 随机打乱当前列表中的值,没有返回值,直接打乱元数据
arr = [1,2,3,4,5]
random.shuffle(arr)
print(arr)  # [2, 4, 5, 1, 3]
