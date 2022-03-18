import os
import zipfile

# 遍历文件和文件夹
dir_list = os.listdir()

w往压缩包里写入内容，r读取压缩包内容，a追加内容
with zipfile.ZipFile('myfile.zip', 'w') as zipobj:
    for file in dir_list:
        if file.endswith('.py'):
            zipobj.write(file)

with zipfile.ZipFile('myfile.zip', 'r') as zipobj:
    print(zipobj.namelist())

with zipfile.ZipFile('myfile.zip', 'r') as zipobj:
    # 解压单个文件
    zipobj.extract('os_demo1.py', 'osasdf/')
    # 解压所有文件
    zipobj.extractall('osasdf/b/')