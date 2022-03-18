# 自动化办公excel，csv

## 1. os模块

| 方法名                                  | 作用                                                  |
| --------------------------------------- | ----------------------------------------------------- |
| os.remove('path/filename')              | 删除文件                                              |
| os.rename(oldname,newname)              | 重命名文件                                            |
| os.walk()                               | 生成目录树下的所有文件名                              |
| os.chdir('dirname')                     | 改变目录                                              |
| os.mkdir/makedirs('dirname')            | 创建目录、多层目录                                    |
| os.rmdir/removedirs('dirname')          | 删除目录、多层目录                                    |
| os.listdir('dirname')                   | 列出指定目录的文件                                    |
| os.scandir()                            | 和listdir相近的功能，列出指定目录的文件Python官方推荐 |
| os.getcwd()                             | 取得当前工作目录                                      |
| os.chmod()                              | 改变目录权限                                          |
| os.path.basename('path/filename')       | 去掉目录路径，返回文件名                              |
| os.path.dirname('path/filename')        | 去掉文件名，返回目录路径                              |
| os.path.join(path1,[path2,[path3,...]]) | 将分离的各部分组合成一个路径名                        |
| os.path.split('path')                   | 返回（dirname(), basename())元组                      |
| os.path.splitext()                      | 返回(filename,extension) 元组                         |
| os.path.getatime/ctime/mtime            | 分别返回最近访问，创建，修改时间                      |
| os.path.getsize()                       | 返回文件大小                                          |
| os.path.exists()                        | 是否存在                                              |
| os.path.isabs()                         | 是否是绝对路径                                        |
| os.path.isdir()                         | 是否为目录                                            |
| os.path.isfile()                        | 是否为文件                                            |

### a. os.getcwd()

获取当前python程序运行路径

```python
import os

print(os.getcwd())
# 当前路径F:\python\github_files\Everyday_study_python\excel相关操作
```

### b. os.chdir()

更改路径

```python
os.chdir('F:\python\github_files\Everyday_study_python')
print(os.getcwd())
# F:\python\github_files\Everyday_study_python
```

### c. os.listdir()

遍历文件或文件夹

```python
dir_list = os.listdir()  # 返回的是列表
for d in dir_list:
    print(d, os.path.isdir(d), os.path.isfile(d))
'''
excel相关操作 True False
files True False
Mysql数据库 True False
python基础 True False
...
'''	
```

### d. os.scandir(),file.stat()

遍历文件或文件夹，返回的是迭代器，需要遍历查看

```python
dir_list = os.scandir()
print(dir_list)  # <nt.ScandirIterator object> 是一个迭代器，需要遍历
for file in dir_list:
    # print(file, file.name, file.is_dir())
    print(file.name,file.stat())
    # Mysql数据库 os.stat_result(st_mode=16895, st_ino=0, st_dev=0, st_nlink=0, st_uid=0, st_gid=0, st_size=0,st_atime=1641964723, st_mtime=1641878590, st_ctime=1641878590)
```

其中，调用`file.stat()`获取更加详细的文件信息，

> st_size：文件的体积大小（单位：bytes），除以1024就是kb
>
> st_atime：文件的最近访问时间
>
> st_mtime: 文件的最近修改时间
>
> st_ctime: windows下表示创建时间

如,获取文件的大小

```python
dir_list = os.scandir()
for file in dir_list:
    print(file.name, file.stat().st_size)
'''
python基础 0
Python流程控制与函数 0
README.md 231
其中 python基础 和 Python流程控制与函数 都是文件夹,所以size是0,st_size判断的是文件的大小
'''
```

st_atime等,都是输出的时间戳,所以可以通过datetime转换下

```python
import datetime
dir_list = os.scandir()
for file in dir_list:
    print(file.name, datetime.datetime.fromtimestamp(file.stat().st_mtime))
    # README.md 2022-01-11 13:23:10.138534
```

## 2. os_demo1

```python
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
文件夹的数量是：18,文件夹是：['.git', '.idea', 'ATM'...]
含有i的文件夹的数量是：4,名称分别为：['.git',...]
'''
```

## 3.  glob，walk

Python os 模块的walk()函数，是用来遍历目录树的，此函数可以很方便的遍历以输入的路径为root的所有子目录和其中的文件。walk函数是一个Python生成器，调用方式是在一个for...in...循环中，walk生成器每次返回的是一个含有3个元素的元组，分别是`(dirpath, dirname, filenames)`

```python
import os

 for dirpath, dirname, files in os.walk('../'):
     print(dirpath, dirname, files)
'''
../files ['Typora操作学习文档.assets', '其他问题汇总.assets'] ['github登录慢的解决方式.txt', 'git上传代码时遇到的问题汇总.txt', ]
../files\Typora操作学习文档.assets [] ['扩展语法.png', '波浪号.png', '示例.png', '示例2.png']
../files\其他问题汇总.assets [] ['1.png', '2.png', '3.png', '4.png', '5.png', '安装mysqlclient.png', '安装mysqldb.png', ]
'''
# dirpath=str, dirname=list, files=list
```

另一个函数glob其实更加的方便，glob函数可以指定查看文件夹

```python
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
```

##  4. os.demo2

```python
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
```

## 5.批量操作文件夹

创建文件夹和多层文件夹	

```python
import os

if os.path.exists('package01'):
    print('存在')
else:
    # 在当前目录下创建文件夹
    os.mkdir('package01')

# 创建多层文件夹
os.makedirs('package02/package03/package04')
```

复制文件或文件夹

复制、移动、删除文件夹需要借助另一个模块：`shutil`模块

### shutil 模块

```python
# 导入shutil模块
import shutil, os

# 删除文件夹
shutil.rmtree('文件夹名')
# 删除文件
os.remove('文件名')

# 复制文件
shutil.copy('os_demo3.py', 'package01')
shutil.copy('os_demo3.py', 'package01/os_demo4.py')
# 复制文件夹，需要注意的是已存在的路径后的文件夹名称一定要有，可以重命名文件
shutil.copytree('package01', 'package02/package001')

# 移动
shutil.move('package02/package001/os_demo3.py', 'package02/package03/package04/')
```

### shutil_demo

```python
'''
1.键盘输入一个路径
2.获取里面所有的mp4文件
3.重命名mp4文件在每个文件前面添加前缀，前缀就是文件最后修改的年月日（如：2021-03-31_西游记01.mp4）
4.新建文件夹：最新视频
5.将重命名的视频批量移动到最新视频文件夹
'''
import os, datetime, shutil, glob

path = input('请输入要查询的路径：')
os.chdir(path)

if not os.path.exists('最新视频'):
    os.mkdir('最新视频')

for dirpath, dirname, files in os.walk('./'):
    for file in os.scandir(dirpath):
        if file.name.endswith('.mp4'):
            tm = datetime.datetime.fromtimestamp(file.stat().st_mtime)
            new_file = str(tm.year) + '-' +str(tm.month)+ '-'+ str(tm.day)+'-'+file.name
            os.rename(dirpath+ '/'+ file.name, new_file)

file_ls = glob.glob('*.mp4')
for name in file_ls:
    shutil.move(name,'最新视频/')
print('over')
```

## 6.临时文件

创建临时文件或者临时文件夹的话需要使用`tempfile`模块

该模块这种TemporaryFile类是tempfile中最常用的类之一，其目的就在于提供一个同意的临时文件调用接口，读写临时文件，并且保证临时文件的隐形性，这个类的构造方法和一般的文件对象类似：

```python
tempfile.TemporaryFile([mode='w+b'[, bufsize=-1[, suffix=''[, prefix='tmp'[, dir=None]]]]])
```

可以看到，默认的打开模式是w+b，但是和一般通过wb模式打开的文件对象不同之处在于，正如上面所示它也可以读取文件。

在TemporaryFile类的基础上有衍生出了两个更加精细化的类用来处理。NamedTemporaryFile类是在前者的基础上，初始化时加上了delete参数，默认值为True。当此参数为True时和TemporaryFile类完全一致，如果是False，那么临时文件对象在被关闭时不会删除，因此可以在下面的代码中通过同样的对象再次打开

### 创建临时文件夹

```python
# file：临时文件夹.py
from tempfile import TemporaryDirectory

with TemporaryDirectory() as temp_dir:
    print('文件夹已经创建：', temp_dir)
```

文件夹的名字是随机的，比如我们使用解压软件解压文件到指定位置就是，创建临时文件夹保存，绕后移动到指定位置的

### 创建临时文件保存数据

```python
# file：临时文件夹.py
from tempfile import TemporaryFile

with TemporaryFile(mode='w+') as tmp_file:  # w+表示写入及读取文件
    tmp_file.write('文件搬运工！')
    tmp_file.seek(0)  # .seek(0)表示回到文件开头位置
    data = tmp_file.read()
    print(data)
```

程序运行完后自动删除临时文件

## 7. 压缩和解压缩文件

### a.压缩文件

压缩包的处理使用zipfile模块，创建一个压缩包文件：

```python
import os
import zipfile

# 遍历文件和文件夹
dir_list = os.listdir()

# w往压缩包里写入内容，r读取压缩包内容，a追加内容
with zipfile.ZipFile('myfile.zip', 'w') as zipobj:
    for file in dir_list:
        if file.endswith('.py'):
            zipobj.write(file)
```

如果没有这个压缩包，直接创建的话使用`w`,如果已经存在了，要向压缩包里面添加内容的时候，将`w`改成`a`，否则系统会报错

如果需要读取或者查看一个zip文件中的内容，就使用

```python
with zipfile.ZipFile('myfile.zip', 'r') as zipobj:
    print(zipobj.namelist())
# 只能看到压缩包里的文件名称列表，不能看文件内的内容，需要解压缩才可以
```

### b.解压缩

解压压缩包单个文件`.extract`(压缩包内要解压的文件名，解压到哪个位置)

```python
with zipfile.ZipFile('myfile.zip', 'r') as zipobj:
    # 解压单个文件
    zipobj.extract('os_demo1.py', 'osasdf/')
    # 解压所有文件
    zipobj.extractall('osasdf/b/')
```

### c.综合demo

```python
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
```

# Excel处理模块

## 1.安装`openpyxl`模块

```
pip install openpyxl
```

## 2. 创建

### a.创建一个sheet

```python
from openpyxl import Workbook

# 实例化
wb = Workbook()
# 获取当前active的sheet，激活状态
sheet = wb.active
print(sheet.title)  # 打印当前sheet名
sheet.title = 'sheet学习01'  # 更改sheet名

# 保存并创建
wb.save('excel_test.xlsx')
```

### b.创建多个sheet

```python
from openpyxl import Workbook

# 实例化
wb = Workbook()
# 创建多个sheet
for i in range(1,4):
    sheet = wb.create_sheet(str(i))

# 保存
wb.save('excel_test.xlsx')
```

## 3.写入

```python
from openpyxl import Workbook


wb = Workbook()
sheet = wb.active

# 写入数据
# 方法一：
sheet['B9'] = 'yaya'
sheet['C9'] = 'mama'
# 方法二"append,会将数据添加在最后一行
sheet.append([1,2,3])
# 方法三：python类型会被自动转换
sheet['A3'] = datetime.datetime.now().strftime("%Y-%m-%d")

# 保存
wb.save('excel_test.xlsx')
```

## 4. 打开已有文件

```python
# file:excel_demo.py
wb = load_workbook('excel_test.xlsx')

print(wb.sheetnames)  # 推荐使用这种方式获取sheetname
print(wb.get_sheet_names())  # python推荐使用第一种
sheet = wb['sheet学习01']  # 推荐使用这种方式选择操作某个sheet
sheet = wb.get_sheet_by_name('sheet学习01')  # python推荐使用第一种
```

## 5.获取数据

### a.获取某个单元格数据

```python
# file:excel_demo.py
wb = load_workbook('excel_test.xlsx')
sheet = wb['sheet学习01']  # 选择sheet

print(sheet['C9'])  # <Cell 'sheet学习01'.C9>
print(sheet['C9'].value)  # 获取某个单元格值：mama

for cell in sheet['A4:A9']:
    print(cell)  # (<Cell 'sheet学习01'.A9>,)是一个元组
    print(cell[0].value)  # <Cell 'sheet学习01'.A9> 所对应的值
```

### b.按行遍历

```python
# file:excel_demo.py
wb = load_workbook('excel_test.xlsx')
sheet = wb['sheet学习01']  # 选择sheet

# 按行遍历
for row in sheet:
    print(row)
    for cell in row:
        print(cell.value)
# 其中 row是一行中所有的数据，元组形式：
# row：(<Cell 'sheet学习01'.A12>, <Cell 'sheet学习01'.B12>, <Cell 'sheet学习01'.C12>, <Cell 'sheet学习01'.D12>)
# 遍历的顺序是：A1,A2...B1,B2,,
# 空的单元格显示None
```

### c.按列遍历

```python
# file:excel_demo.py
wb = load_workbook('excel_test.xlsx')
sheet = wb['sheet学习01']  # 选择sheet
# 按列遍历
for column in sheet.columns:
    for cell in column:
        print(cell.value,end=',')
    print()
```

### d.指定行&列

```python
# file:excel_demo.py
wb = load_workbook('excel_test.xlsx')
sheet = wb['sheet学习01']  # 选择sheet

# 指定行&列进行遍历
# 遍历6-11行，前3列的数据
for row in sheet.iter_rows(min_row=6, max_row=11,max_col=3):
    for cell in row:
        print(cell.value,end=',')
    print()
# 遍历2-4列，第3行到第6行的数据
for col in sheet.iter_cols(min_col=2, max_col=4,max_row=6,min_row=3):
    for cell in col:
        print(cell.value,end=',')
    print()
```

### e.删除工作表

```python
# 删除工作表
# 方法1
wb.remove(sheet)
# 方法2
del wb[sheet]
```

