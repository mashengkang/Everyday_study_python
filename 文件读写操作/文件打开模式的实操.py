# coding:utf-8

# 文件操作的步骤和方式
# 写入文件操作
# 1. 打开文件
fp = open('./1.txt', 'a', encoding='utf-8')
# 2. 写入文件
fp.write('\n你好')
# 2. 关闭文件
fp.close()

# 文件操作的 高级写法
'''
with open(文件路径,打开模式) as 变量:
    变量.操作()
'''

# w+ 既可读又可写,注意w模式的特点,时打开文件后直接清空了文件
# r+ 既可读又可写
# a+ 追加写,并且可读,但是直接read是读不到文件的,因为文件指针在最后,需要移动指针
with open('./1.txt','a+',encoding='utf-8') as rf:
    rf.write('\nBB')
    # 设置指针位置
    rf.seek(0)  # 设置当前指针的位置,seek(0),最开始的位置
    res = rf.read()
    print(res)