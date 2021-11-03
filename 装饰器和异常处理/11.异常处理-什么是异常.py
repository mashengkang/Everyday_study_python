# coding:utf-8
# 什么是异常?

'''
异常是一个事件,并且这个异常事件在我们的程序运行过程中出现,会影响我们程序正常执行
异常分两种:
    1. 语法错误导致
    2.逻辑错误导致
在程序无法正常运行处理时,就会出现一个异常,在puthon中异常时一个对象,表示一个错误
'''

varlist = [1, 2, 3]
# print(varlist[3])
'''
Traceback (most recent call last):
  File "E:/study_python_everyday/装饰器和异常处理/11.异常处理-什么是异常.py", line 13, in <module>
    print(varlist[3])
IndexError: list index out of range
'''


'''
如何处理异常?
1. 如果错误是可以预知的,可以通过判断预防处理
'''

n2 = 3
if isinstance(n2, int):
    res = 10 + n2
    print(res)  # 13

'''
2. 如果错误的发生不可预知,就可以使用try,except 处理
语法:
try:
    可能发生的异常错误的代码
except:
    如果发生异常则进入 except  代码'''

# 假设读取的文件不存在,会发生错误,可以使用两种方法进行处理
# 1. 可以在文件读取前先判断当前的文件是否存在
# 2. 使用try except
try:
    with open("./user.txt", 'r') as fp:
        res = fp.read()
    print(res)
except:
    print('文件不存在')

print('程序继续执行')