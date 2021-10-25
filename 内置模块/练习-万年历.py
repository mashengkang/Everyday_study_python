# coding:utf-8
# 万年历

import calendar, time
import os


# 返回指定年份和月份的数据,月份是第一天是周几,和月份中的天数 monthrange(year,month)

def showdate(year, month):
    res = calendar.monthrange(year, month)
    days = res[1]  # 当前月份一共多少天
    week = res[0] + 1  # 当前月份的第一天是周几
    print("*"*20+ f'{year}年 {month}月'+'*'*20)
    print('一\t二\t三\t四\t五\t六\t日')
    # 实现日历信息的输入
    d = 1
    while d <= days:
        # 循环周
        for i in range(1, 8):
            # 判断是否输出t
            if d > days or (d == 1 and i < week):
                print('' * (week - 1), end="\t")
            else:
                print('{:0>2d}'.format(d), end='\t')
                d += 1
        print()
# 获取当前系统的年月
dd = time.localtime()
year = dd.tm_year  # 获取年
month = dd.tm_mon  # 获取月

while True:
    # 清屏(终端中能显示清屏效果)
    os.system('cls')
    # 默认输出当前年月的日历信息
    showdate(year, month)
    print('*'*18 + '<上一月 下一月>' + '*'*18)
    # 获取用户的输入
    c = input('请输入您的选择:')
    # 判断用户的输入内容
    if c == '<':
        if month <= 1:
            month = 12
            year -= 1
        else:
            month -= 1
    elif c == '>':
        if month >= 12:
            month = 1
            year += 1
        else:
            month += 1
    else:
        print('输入错误请重新输入!')