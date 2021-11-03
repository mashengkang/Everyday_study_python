# coding:utf-8
# 自定义包


# 如果需要使用包可以直接导入包
# 直接把包当作模块导入,可以用的内容是__init__.py文件中定义的(不推荐使用)
import package
package.funcd()

# 可以导入模块中的所有内容
# 注意这个内容是由__init__.py文件中定义的__all__ 这个变量指定的模块
# 好处是可以直接导入指定的所有模块,并且使用时,直接使用指定的模块名
from package import a  #  from package import *
a.funca()  # 需要在__init__.py中,定义内容__all__ = ['a',]

# 导入指定包中的指定模块
from package import a
a.funca()

# 从指定包的指定模块中导入指定的内容
from package.b import funcb
funcb()

# 从指定包的子包中导入模块
from package.package_2 import c
c.funcc()

# 从指定包的子包的模块中导入指定内容
from package.package_2.c import funcc
funcc()
