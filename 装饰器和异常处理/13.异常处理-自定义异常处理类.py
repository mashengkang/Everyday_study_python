# coding:utf-8
# 自定义异常处理类


'''
在出现异常后,对异常进行处理,并且把异常信息写入日志
日志的基本格式:
    日期时间,异常的级别
    异常信息:引发的异常类,异常的信息,文件及行号
'''
import traceback, logging
# 通过tarceback 模块获取异常信息  traceback.format_exc()

try:
    int('aa')
except:
    errormsg = traceback.format_exc()
    print(errormsg)
'''
Traceback (most recent call last):
  File "E:/study_python_everyday/装饰器和异常处理/13.异常处理-自定义异常处理类.py", line 16, in <module>
    int('aa')
ValueError: invalid literal for int() with base 10: 'aa'
Process finished with exit code 0

'''


# 自定义异常日志处理类
class Myexceptions():
    def __init__(self):
        import traceback, logging

        # logging 的基本配置
        logging.basicConfig(
            filename='./error.log',  # 日志存储的文件及目录
            format='%(asctime)s %(levelname)s \n %(message)s',  # 格式化存储的日志格式
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        # 写入日志
        logging.error(traceback.format_exc())

# 使用自定义异常处理类
try:
    int('aa')
except:
    print('在此处进行异常处理')
    Myexceptions()  # 在异常处理的代码块中去调用自定义异常类