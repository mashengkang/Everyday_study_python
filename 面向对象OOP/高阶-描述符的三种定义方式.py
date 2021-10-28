# coding:utf-8
# 描述符的三种定义方式

# 格式1 通过定义 描述符类来实现
'''
class ScoreManage():
    def __get__(self, instance, owner):
        pass

    def __set__(self, instance, value):
        pass

    def __delete__(self, instance):
        pass

class Student():
    score = ScoreManage()
'''


# 格式二 使用property 函数 实现
'''
class Student():
    # 在当前需要被管理的类中,直接定义类似下面三个方法
    def getscore(self):  # getscore中,有返回值,获取的值
        return 'getscore'

    def setscore(self, value):
        print('setscore', value)

    def delscore(self):
        print('delscore')

    # 在函数中指定对应的三个方法.对应的方法顺序:1.__get__, 2. __set__, 3.d__del__
    score = property(getscore, setscore, delscore)

zs = Student()
print(zs.score)  # getscore
zs.score = 200  # setscore 200
del zs.score  # delscore
'''

# 格式三 使用 @property 装饰器来实现
class Student():
    __score = None

    @property
    def score(self):
        print('get')
        return self.__score

    @score.setter
    def score(self, value):
        print('set')
        self.__score = value

    @score.deleter
    def score(self):
        print('delete')
        del self.__score

zs = Student()
print(zs.score)  # get None
# 先执行 zs.score的获取操作,print出'get', 然后print zs.score这个操作的返回值,为None
zs.score = 199  # set
print(zs.score) # get 199
del zs.score  # delete