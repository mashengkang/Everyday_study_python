# coding:utf-8

import calendar

# 返回指定年份和月份的数据,月份的第一天是周几,和月份中的天数
# calendar.monthrange(年,月)
res = calendar.monthrange(2020, 9)
print(res, type(res))  # (4, 30) <class 'tuple'>
days = res[1]  # 当前月份一共多少天
week = res[0] + 1  # 当前月份的第一天是周几

print('一\t二\t三\t四\t五\t六\t日')
# 实现日历信息的输入
d = 1
while d <= days:
    # 循环周
    for i in range(1, 8):
        # 判断是否输出t
        if d > days or (d == 1 and i < week):
            print(''*(week-1), end="\t")
        else:
            print('{:0>2d}'.format(d), end='\t')
            d += 1
    print()