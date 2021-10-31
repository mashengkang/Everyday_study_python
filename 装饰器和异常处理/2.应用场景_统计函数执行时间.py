# coding:utf-8
import time


# 定义统计时间的装饰器
def runtime(f):
    def inner():
        starttime = time.perf_counter()
        f()
        endtime = time.perf_counter()
        res = (endtime - starttime)
        print(f'函数执行了{res}秒')
    return inner


# 定义个函数
@runtime
def func():
    for i in range(10):
        print(i)
        time.sleep(0.5)

func()