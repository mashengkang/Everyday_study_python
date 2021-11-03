def funcc():
    print('funcc')


# 假设在这个模块中如果需要 当前包中的d模块
# .d是相对导入,不可以直接在这个文件中执行这个 funcd()

from .d import funcd
funcd()

# 可以在这个模块中去使用上一级中的模块
from .. import a
a.funca()

from ..b import funcb
funcb()

# from ...My import func  # 不能使用...的方式,导入上两级模块
# func()
# 这个时候需要使用sys.path
import sys
sys.path.append("../")
from 模块与包 import My
My.func()
