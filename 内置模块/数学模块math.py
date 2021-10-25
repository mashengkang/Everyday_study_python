# coding:utf-8


import math

# math.ceil() 向上取整, 内置函数 round():四舍五入,但是如果正好是取整时是 .5 ,则向偶数取整
r1 = math.ceil(2.25)
r2 = round(2.25)
print(r1, r2)  # 3 2

# math.floor() 向下取整
r3 = math.floor(2.22)
print(r3)  # 2

# math.pow() 计算数值的n次方,结果是浮点数
r4 = math.pow(2, 3)
print(r4)  # 8.0

# math.sqrt() 开平方运算,结果是浮点数
r5 = math.sqrt(5)
r6 = math.sqrt(4)
print(r5, r6)  # 2.23606797749979 2.0

# math.fabs() 计算绝对值,结果是浮点数
r7 = math.fabs(-100)
print(r7)  # 100.0

# math.modf() 把一个数值拆分成小数和整数组成的元组
r8 = math.modf(3.14)
print(r8)  # (0.14000000000000012, 3.0)

# math.copysign(x, y) 把第二个参数的正负符号拷贝给第一个参数,结果是浮点数
r9 = math.copysign(10, -31)
print(r9)  # -10.0

# math.fsum() 将一个容器类型数据中的元素进行一个求和,结果是浮点数,注意:容器中数据必须是可计算的
r10 = math.fsum([1, 2, 3])
print(r10)  # 5.0

# 常量 圆周率
pai = math.pi
print(pai)  # 3.141592653589793