'''
1.键盘输入一个路径
2.统计该路径下的文件和文件夹，以及分别的数量
3.统计当前路径下文件夹名称中 包含字母 i 的文件数量和名称，注意不区分大小写
'''

import os

path = input('请输入一个路径：')
os.chdir(path)

file_list = []
dir_list = []
for file in os.scandir():
    if file.is_dir():
        dir_list.append(file.name)
    else:
        file_list.append(file.name)
print(f'文件夹的数量是：{len(dir_list)},文件夹是：{dir_list}')
print(f'文件的数量是：{len(file_list)},文件是：{file_list}')

demo_list = []
for name in dir_list:
    if 'i' in name.lower():
        demo_list.append(name)
print(f'含有i的文件夹的数量是：{len(demo_list)},名称分别为：{demo_list}')
'''
请输入一个路径：F:\python\github_files\Everyday_study_python
文件夹的数量是：18,文件夹是：['.git', '.idea', 'ATM', 'excel相关操作', 'files', 'Mysql数据库', 'python基础', 'Python流程控制与函数', 'spider', 'venv', 'web', '内置模块', '文件读写操作', '模块与包', '第三方库的管理和虚拟环境', '练习', '装饰器和异常处理', '面向对象OOP']
文件的数量是：1,文件是：['README.md']
含有i的文件夹的数量是：4,名称分别为：['.git', '.idea', 'files', 'spider']
'''
