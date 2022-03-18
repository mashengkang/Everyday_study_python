import os

print(os.getcwd())
# 当前路径F:\python\github_files\Everyday_study_python\excel相关操作

# 更改路径
os.chdir('F:\python\github_files\Everyday_study_python')
print(os.getcwd())
# F:\python\github_files\Everyday_study_python

dir_list = os.listdir()  # 返回的是列表
for d in dir_list:
    print(d, os.path.isdir(d), os.path.isfile(d))
'''
excel,csv相关操作 True False
files True False
Mysql数据库 True False
python基础 True False
...
'''

import datetime
dir_list = os.scandir()
print(dir_list)  # <nt.ScandirIterator object> 是一个迭代器，需要遍历
for file in dir_list:
    # print(file, file.name, file.is_dir())
    # print(file.name,file.stat())
    # Mysql数据库 os.stat_result(st_mode=16895, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0,
    #           st_atime=1641964723, st_mtime=1641878590, st_ctime=1641878590)
    # print(file.name, file.stat().st_size)
    print(file.name, datetime.datetime.fromtimestamp(file.stat().st_mtime))
    # README.md 2022-01-11 13:23:10.138534