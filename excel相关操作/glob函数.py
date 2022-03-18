import os

print(os.getcwd())

# for dirpath, dirname, files in os.walk('../'):
#     print(dirpath, dirname, files)
'''
../files ['Typora操作学习文档.assets', '其他问题汇总.assets'] ['github登录慢的解决方式.txt', 'git上传代码时遇到的问题汇总.txt', ]
../files\Typora操作学习文档.assets [] ['扩展语法.png', '波浪号.png', '示例.png', '示例2.png']
../files\其他问题汇总.assets [] ['1.png', '2.png', '3.png', '4.png', '5.png', '安装mysqlclient.png', '安装mysqldb.png', ]
'''

import glob
t_list = glob.glob('*s*')
print(t_list)  # 获取当前目录下 文件名和文件夹名 中含有s的文件，但是不能获取子文件夹里面的内容
# ['os_demo1.py', 'glob函数.py', 'os相关操作.py']

t_list = glob.glob('**')  # 获取当前目录的文件和文件夹
print(t_list)
# ['osasdf', 'os_demo1.py', 'glob函数.py', 'os相关操作.py', '自动化办公相关.md']

t_list = glob.glob('**/')  # 获取当前目录的文件夹
print(t_list)
# ['osasdf\\']

# 如果**结合recursive=True使用，可以实现递归
t_list = glob.glob('**', recursive=True)  #遍历当前路径下所有的文件和文件夹
print(t_list)
# ['osasdf', 'osasdf\\b', 'osasdf\\b\\b.py', 'osasdf\\sqr.py', 'os_demo1.py', 'glob函数.py', 'os相关操作.py', '自动化办公相关.md']

t_list = glob.glob('**/', recursive=True)  # 遍历文件夹
print(t_list)
# ['osasdf\\', 'osasdf\\b\\']

t_list = glob.glob('**/*.py', recursive=True)  # 遍历目录下所有的.py文件
print(t_list)
# ['os_demo1.py', 'glob函数.py', 'os相关操作.py', 'osasdf\\sqr.py', 'osasdf\\b\\b.py']




