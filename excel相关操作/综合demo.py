'''
1.找出指定目录下所有距离上次修改时间超过一个月的md文件
2.将所有文件重命名，再原本文件名开头加上最后修改日期
3.创建一个新的文件夹：长期未使用
4.将所有文件移动到：长期未使用 文件夹下
5.对 长期未使用 文件夹进行压缩处理，并在名字上加上今天日期

'''
import os, shutil, zipfile
from datetime import datetime

path = input('输入路径：')
os.chdir(path)

file_list = []

for dirpath, dirname, files in os.walk('./'):
    for file in os.scandir(dirpath):
        file_time = file.stat().st_mtime
        file_datetime = datetime.fromtimestamp(file_time)
        datetime_delta = datetime.now() - file_datetime
        if datetime_delta.days >= 31 and file.name.endswith('md'):
            new_name = f'{file_datetime.strftime("%Y-%m-%d")}-{file.name}'
            try:
                os.rename(dirpath + '/' + file.name, new_name)
                file_list.append(new_name)
            except:
                print(f'修改{file.name}失败')

if not os.path.exists('长期未使用'):
    os.mkdir('长期未使用')

for file1 in file_list:
    shutil.copy(file1, '长期未使用/')

os.chdir('长期未使用/')
zip_list  = os.listdir('./')

zip_filename = f'{datetime.now().strftime("%Y-%m-%d")}_长期未使用.zip'
with zipfile.ZipFile(zip_filename, 'w') as zipobj:
    for file in zip_list:
        zipobj.write(file)


