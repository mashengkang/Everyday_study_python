# coding:utf-8
# try ...except 详细用法


# 1. 使用try 处理指定的异常类,如果引发了非指定的异常,则无法处理
try:
    s1 = 'hello'
    int(s1)  # ValueError:
# except IndexError as e: 如果引发了非指定的异常,则无法处理
except ValueError as e:
    print(e)

# 2.多分支处理异常类
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print('IndexError')
except KeyError as e:
    print('KeyError')
except ValueError as e:
    print('ValueError')

# 3. 通用异常类 Exception
s1 = 'world'
try:
    int(s1)
except Exception as e:
    print(e)

# 4. 多分支异常类加通用异常类,这样引发异常会按照从上到下的顺序去执行对象的异常处理类
s1 = 'hello'
try:
    int(s1)
except IndexError as e:
    print('IndexError')
except KeyError as e:
    print('KeyError')
except ValueError as e:
    print('ValueError')
except Exception as e:
    print('Exception')

# 5.try except else...str
s1=  'hello'
try:
    str(s1)
except IndexError as e:
    print('IndexError')
except ValueError as e:
    print('ValueError')
except Exception as e:
    print('Exception')
else:
    print('try代码块中没有引发异常时,执行')  # try代码块中没有引发异常时,执行

# 6.try...except..else.finally
# finally 无论是否引发异常,都会执行,通常情况下用于执行一些清理工作
s1=  'hello'
try:
    int(s1)
    print('如果前面的代码引发了异常,这个位置代码块将不会被执行')
except Exception as e:
    print('Exception')
else:
    print('try代码块中没有引发异常时,执行')
finally:
    print('无论是否引发异常,都会执行这个代码块')
print('如果上面的代码有异常并且进行了处理,那么后面的代码依然会执行')

# 7.使用 raise 主动抛出异常
try:
    # 可以使用 raise 主动抛出异常,并设置异常信息
    raise Exception('a', 'b')
except Exception as e:
    print(e)  # ('a', 'b')

# 8. assert 断言
assert 1 =='1'  # 如果后面的表达式错误,则抛出错误 AssertionError
assert 1 == 1  # 如果后面的表达式正确,则什么也不做



