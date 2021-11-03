# coding:utf-8
# 导入方式的分类


'''
1. 绝对导入:使用[搜索路径]去查找和导入指定的包或模块
import 模块
import 包
import 包.模块
from 模块 import 内容
from 包 import 模块
from 包.模块 import 内容

2. 相对导入 注意:相对导入只能在非主程序的模块中使用,不需要直接运行的模块文件
from .包名/模块名 import 模块/内容
from ..包名/模块名 import 模块/内容

.   代表当前
..  代表上一级
'''

# 导入c模块,c模块中使用了相对导入
from package.package_2 import c


# 了解 搜索路径:在导入模块或包时,程序查找的路径
'''
主要的搜索路径
    1.当前导入模块的程序所在的文件
    2.python的安装目录的扩展目录中:..../Python38/lib
    3.python解释器指定的其他 第三方模块位置 lib/sitepackages
'''

# 在当前脚本中查看 包或模块 的 搜索路径
import sys
print(sys.path)
'''
['E:\\study_python_everyday\\模块与包', 
'E:\\study_python_everyday', 
'F:\\Program Files\\PyCharm 2020.3.3\\plugins\\python\\helpers\\pycharm_display', 
'F:\\Program Files\\python3.8.3\\python38.zip', 
'F:\\Program Files\\python3.8.3\\DLLs', 
'F:\\Program Files\\python3.8.3\\lib', 
'F:\\Program Files\\python3.8.3', 
'F:\\Program Files\\python3.8.3\\lib\\site-packages', 
'F:\\Program Files\\python3.8.3\\lib\\site-packages\\win32', 
'F:\\Program Files\\python3.8.3\\lib\\site-packages\\win32\\lib', 
'F:\\Program Files\\python3.8.3\\lib\\site-packages\\Pythonwin', 
'F:\\Program Files\\PyCharm 2020.3.3\\plugins\\python\\helpers\\pycharm_matplotlib_backend', '../']
'''


