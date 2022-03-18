'''
1.键盘输入一个路径
2.搜索该路径下文件大小超过50M的zip文件
3.搜索该路径下最后修改日期在30天前的文件
4.打印显示2，3的文件
'''

import os, datetime, glob

path = input('输入一个路径：')
os.chdir(path)

paths = glob.glob('**/*.zip', recursive=True)
print(paths)
for path in paths:
    file_sizes = os.stat(path).st_size/1024/1024
    file_modify = datetime.datetime.fromtimestamp(os.stat(path).st_mtime)
    days = (datetime.datetime.now()-file_modify).days
    if (file_sizes>50) and (days>30):
        print(f'压缩包的名称是：{path},文件大小：{file_sizes}MB,修改时间：{days}天前')
