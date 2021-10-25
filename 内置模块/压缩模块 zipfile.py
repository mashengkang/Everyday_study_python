# coding:utf-8
import os
import zipfile

'''
zipfile.ZipFile(路径包名, 模式, 压缩或打包)
'''
# 压缩文件
with zipfile.ZipFile('./spam.zip', 'w') as myzip:
    myzip.write('data.json')
    myzip.write('data2.txt')
    myzip.write('data.txt')

# 解压缩   extractall(路径),提取所有文件到 路径
with zipfile.ZipFile("./spam.zip", 'r' ) as myzip:
    myzip.extractall('../')

# 如果压缩当前文件夹中的所有文件
with zipfile.ZipFile("spam2.zip", 'w', zipfile.ZIP_DEFLATED) as myzip:
    arr = os.listdir("./")
    for i in arr:
        print(i, os.path.getsize(i))
        myzip.write(i)

# 使用shutil 模块进行归档压缩
import shutil

# 参数1 创建的压缩文件名称, 参数二,指定的压缩格式(zip,tar) 参数3 要压缩的文件或文件夹路径
shutil.make_archive('a', 'tar', './')