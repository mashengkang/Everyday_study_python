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
print(varlist[3])
'''
Traceback (most recent call last):
  File "E:/study_python_everyday/装饰器和异常处理/11.异常处理-什么是异常.py", line 13, in <module>
    print(varlist[3])
IndexError: list index out of range
'''
