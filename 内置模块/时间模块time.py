# coding:utf-8
import time


"""
    1.时间戳:1635174752.165824 表示从1970年1月1日0时0分0秒到现在的一个秒数,目前可以计算到2038年
    2.时间字符串: Mon Oct 25 23:16:06 2021
    3.时间元组:time.struct_time(tm_year=2021, tm_mon=10, tm_mday=25, tm_hour=23, tm_min=16, tm_sec=6, tm_wday=0, tm_yday=298, tm_isdst=0)
"""
# 1. 获取当前系统的时间戳
res = time.time()
print(res)  # 1635174752.165824

# 2. 获取当前系统时间,时间字符串
res = time.ctime()
print(res, type(res))  # Mon Oct 25 23:14:59 2021 <class 'str'>

# 3. 获取当前系统时间,时间元组
res = time.localtime()
print(res)

# 4.以上时间字符串和时间元组可以通过指定的时间戳来获取
t = 1635174752.165824
res_ctime = time.ctime(t)
res_local = time.localtime(t)

# 5. 使用localtime方法获取的时间元组,如何格式化称为 XXXX年xx月xx日 时:分:秒
print(f'{res_local.tm_year}年{res_local.tm_mon}月{res_local.tm_mday}日 {res_local.tm_hour}:{res_local.tm_min}:{res_local.tm_sec}')

# 6.strftime(格式) 格式化时间 年-月-日 时:分:秒 星期几
res = time.strftime('%Y-%m-%d %H:%M:%S %w')  # %w 周天是0 ,周六是6
print(res)

# 7.sleep(秒) 睡眠时间.可以暂停当前线程的执行,该参数可以是浮点数
print(time.strftime('%H:%M:%S %w'))  # 23:37:42 1
# time.sleep(3)
print(time.strftime('%H:%M:%S %w'))  # 23:37:45 1

# 计算程序的运行时间
# time.perf_counter()
start = time.perf_counter()
for i in range(1000000):
    if 'abc' > 'avd':
        pass
end = time.perf_counter()
print(end-start)  # 0.04653310000000002