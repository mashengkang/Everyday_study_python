# coding:utf-8

# 针对磁盘中的文件的读写
'''
文件操作步骤
    1.打开文件 2.读写文件 3.关闭文件
写入文件的操作:
    1. 打开文件 open()
    2. 写入文件 write()
    3. 关闭文件 close()
读取文件的操作:
    1. 打开文件 open()
    2. 读取文件 read()
    3. 关闭文件 close()
'''

'''
open()
格式: open(文件的路径,打开的方式,[字符集])
    路径:url 统一资源定位符
        相对路径: 
            1.txt ==> 具体文件前没有任何表示时,默认当前目录,和./1.txt 是一个位置
            ./1.txt ==> ./代表当前目录中的1.txt
            ../1.txt ==> ../代表当前目录中的 上一级目录中的1.txt
        绝对路径:
            Windows: c:users/appdata/1.txt
            Linux: /user/home/python/1.txt
    打开方式:
        基础模式: w r x a 
        w模式: write 写入
            1.文件如果不存在,则创建这个文件
            2.文件如果存在,则打开这个文件并且清空文件内容
            3.文件打开后,文件的指针在文件的最前面
    字符集: encoding 可选参数,设置文件的字符集,如果是一个二进制的文件时,不需要设置字符集
        多设置为:encoding:'utf-8'
'''
# 1.打开文件,创建了一个文件对象
fp = open('./1.txt', 'w', encoding='utf-8')
print(fp, type(fp))  # <_io.TextIOWrapper name='./1.txt' mode='w' encoding='utf-8'> <class '_io.TextIOWrapper'>

# 2.写入文件
fp.write('hello world')

# 3.关闭文件
fp.close()


