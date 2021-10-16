# coding:utf-8

'''
函数调用自己本身
递归函数内必须要有结束条件
递归函数的效率并不高,尽量能不用就不用
'''


# 3,2,1,0

def digui(num):
    print(num, end=' ')  # 3 2 1 0
    # 判断
    if num > 0:
        # 调用本身
        digui(num - 1)
    print(num, end=' ')  # 0 1 2 3

# digui(3)

# 实现阶乘
def jiecheng(n):
    if n == 1:
        return 1
    else:
        return n *jiecheng(n-1)

res = jiecheng(7)
print(res)