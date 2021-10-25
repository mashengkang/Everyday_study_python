# coding:utf-8


import os

# getcwd() 获取当前的工作目录,注意获取的不是当前脚本的目录
res = os.getcwd()

# os.chdir() 修改当前的工作目录为:E:\study_python_everyday\内置模块
# os.chdir('E:\study_python_everyday\内置模块')

# os.listdir() 获取当前或指定目录中的所有项,(文件,文件夹,隐藏文件),组成的列表
res1 = os.listdir(path="E:\study_python_everyday\\")
res2 = os.listdir()  # 不指定目录时,默认为当前的工作目录(linux中的ls -al指令,windows中的dir指令
print(res1)

# os.mkdir(path=文件路径, [mode=权限]) 创建文件夹,如果文件夹已存在,则报错
# os.mkdir('aa')  # 默认在工作目录创建
# os.mkdir("E:\study_python_everyday\\aa\\bb\\cc")  # 报错,中间路径如果不存在的话,会报错
# FileNotFoundError: [WinError 3] 系统找不到指定的路径。: 'E:\\study_python_everyday\\aa\\bb\\cc'
'''
关于系统中的文件权限,仅限linux系统
    drwxr-xr-x
    第一位 d 代表一个目录,如果是-则表示为一个文件
    第2-4位的rwx代表文件所有人(u)的权限
    第5-7位的r-x代表文件所属组(g)的权限
    第8-10位的r-x代表文件其他人(o)的权限
    
    其中 r w x - 代表不同的操作权限
        r 可读 
        w 可写
        x 可执行
        - 不可读不可写不可执行,在rwx三个位置中的哪个位置代表哪个权限
'''

# os.makedirs() 可以递归创建文件夹,如果最后的文件夹ce存在,会报错
# os.makedirs("E:\study_python_everyday\\内置模块\\bb\\ce")

# os.rmdir()删除空文件夹
# os.rmdir("E:\study_python_everyday\\内置模块\\bb")
# OSError: [WinError 145] 目录不是空的。: 'E:\\study_python_everyday\\内置模块\\bb'

# os.removedirs() 递归删除空文件夹
# E:\study_python_everyday\\内置模块\\bb\\ce,首先删除ce文件夹,然后检测bb文件夹是不是空,是空继续删除,依此类推
# 如果是mac系统中,文件夹只要被使用过,都会默认创建一个隐藏文件,因此文件夹不再是空文件夹

# os.remove() 删除文件
# os.remove('E:\study_python_everyday\\内置模块\\data.txt')

# os.rename() 修改文件或文件夹的名字
# os.rename('./data.txt', './data1.txt')

# os.system() 执行操作系统中的命令
# os.system('python3 ./随机模块random.py')


# os.path 路径模块
# 相对路径转化为绝对路径
res_abspath = os.path.abspath('./')
print(res_abspath)  # E:\study_python_everyday\内置模块

# 获取路径中的主体部分 就是返回路径中的最后一部分
res_basepath = os.path.basename('E:\study_python_everyday\内置模块')
print(res_basepath)  # 内置模块

# 获取路径中的路径部分
res_dirname = os.path.dirname("E:\study_python_everyday\内置模块")
print(res_dirname)  # E:\study_python_everyday

# join() 链接多个路径,组成一个新的路径
res_join = os.path.join(r'E:\study_python_everyday\a\b', '2.jpg')
print(res_join)  # E:\study_python_everyday\a\b\2.jpg

# split() 拆分路径为路径和主体部分
res_split = os.path.split(r'E:\study_python_everyday\a\b\2.jpg')
print(res_split)  # ('E:\\study_python_everyday\\a\\b', '2.jpg')

# splitext() 拆分路径,可以拆分文件后缀名
res_splitext = os.path.splitext(r'E:\study_python_everyday\a\b\2.jpg')
print(res_splitext)  # ('E:\\study_python_everyday\\a\\b\\2', '.jpg')

# 获取文件(文件夹)的大小,返回字节数
res_size = os.path.getsize(r'E:\study_python_everyday\内置模块\data.json')
print(res_size)  # 108

# 检测是否是一个文件夹,是否存在
res_isdir = os.path.isdir('./bb')
print(res_isdir)  # True

# 检测文件是否存在
res_isfile = os.path.isfile('./data.txt')
print(res_isfile)  # True

# 检测文件(文件夹)是否存在,既可以检测文件,也可以检测路径
res_exists = os.path.exists(r"E:\study_python_everyday\内置模块\data.json")
print(res_exists)

# 检测两个path路径或文件是否同时指向了一个目标位置(两个路径或文件必须真实存在)
# res_same = os.path.samefile(f1, f2)