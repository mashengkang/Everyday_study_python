# coding:utf-8

# 描述符的案例解析
'''
要求,学员分数只能在0-100
解决方法:
    1.在__init__ 方法中检测分数范围  (这个解决方案只能在对象初始化时有效)
    2.定义一个setattr魔术方法
      检测如果给score分数进行赋值时,进行分数的检测判断
        if key == 'score':
            if value >= 0 and value <= 100:
                object.__setattr__(self, key, value)
            else:
                print('当前分数不符合')

        else:
            object.__setattr__(self, key, value)

        假如学员的分数不止一个时怎么办,比如,英语数学语文
        另外就是当前这个类中的代码是否就比较多了呢?

    3.可以思考使用描述符来代理分数属性
        1.定义score描述符
        2.把学生类中的score这个成员交给描述符类进行处理
        3.只要在代理的描述符类中对分数进行赋值和管理就可以了
'''
# 定义一个学生类,需要记录 学院id,名字,分数

"""
class Student():

    def __init__(self, id,name, score):
        self.id = id
        self.name = name
        # self.score = score
        # 检测分数
        if score >= 0 and score <= 100:
            self.score = score
        else:
            print('当前分数不符合')

    def returnMe(self):

        info = f'''
        学员编号:{self.id}
        学员姓名:{self.name}
        学员分数:{self.score}
        '''
        print(info)

    def __setattr__(self, key, value):
        # 检测是否时给score进行赋值操作
        if key == 'score':
            if value >= 0 and value <= 100:
                object.__setattr__(self, key, value)  # 等于self.score = value ,但是赋值方式要用object
            else:
                print('当前分数不符合')

        else:
            object.__setattr__(self, key, value)
"""


# 定义描述符类 代理分数的管理
class Score():
    __score = 0

    def __get__(self, instance, owner):
        return self.__score

    def __set__(self, instance, value):
        if value >= 0 and value <= 100:
            self.__score = value
        else:
            print('分数不符合要求')


# 使用描述符类代理score分数属性
class Student():
    score = Score()

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def returnMe(self):

        info = f'''
        学员编号:{self.id}
        学员姓名:{self.name}
        学员分数:{self.score}
        '''
        print(info)

# 实例化对象
zs = Student(1011, '张三', -77)
# 分数不符合要求 => 在实例化对象时,就会对score的代理Score()执行操作
zs.returnMe()
'''
学员编号:1011
学员姓名:张三
学员分数:00
'''
zs.score = 55
zs.returnMe()
'''
学员编号:1011
学员姓名:张三
学员分数:55
'''