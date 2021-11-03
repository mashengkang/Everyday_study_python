# coding:utf-8


# 在当前脚本中如果需要使用一些已经定义好的功能时,可以选择对象的模块,导入后使用
# 例如系统模块 time
import time
print(time.time())  # 1635946441.94826

# 例如使用自定义异常处理模块
import My

# 使用模块中定义的类
obj = My.MyExceptions()
print(obj)  # <My.MyExceptions object at 0x00000184C02710A0>

# 使用模块中的函数
My.func()  # 这是个函数

# 想使用模块中的内容时,除了导入模块,还可以在指定模块中,导入指定的内容

from My import love  # 导入My模块中的love变量
from My import love as lv  # 导入My模块中的love变量,起个别名,防止冲突
print(love)  # i love you
print(lv)  # i love you

from My import func
func()  # 这是个函数
from My import MyExceptions
print(MyExceptions())  # <My.MyExceptions object at 0x00000224D8931190>
