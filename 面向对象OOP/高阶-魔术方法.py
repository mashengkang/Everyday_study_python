# coding:utf-8
# 魔术方法

'''
1. __init__ 初始化方法
    触发机制:   在通过类实例化对象后,自动触发的一个方法
    作用:     可以在对象实例化后完成对象的初始化(属性的赋值,方法的调用..)
    参数:     一个self,接受当前对象,其他参数根据需要定义即可
    返回值:    默认 无 None
2. __new__构造方法
    触发机制:   实例化对象时自动触发(在__init__之前触发)
    作用:      管理控制对象创建的过程
    参数:      一个cls 接收当前类,其他参数根据初始化方法的参数进行决定
    返回值:    必须返回 object.__new__(cls) 进行对象的创建,如果没有返回值,则实例化对象的结果为None
    注意:
        __new__方法的参数和__init__方法的参数要保持一致(除了第一个参数)
        必须返回 object.__new__(cls) 进行对象的创建,如果没有返回值,则实例化对象的结果为None
    应用场景:设计模式中的单例设计模式
3. __del__ 析构方法
    触发机制:   析构方法会在对象被销毁时自动触发
    作用:      释放或关闭对象创建时打开或创建的一些资源
    参数:      一个self,接受当前对象,无其他参数
    返回值:    默认 无 None
4. __call__
    触发机制:   把对象当作函数直接调用时,自动触发
    作用:      一般用于归纳类或对象的操作步骤,方便调用
    参数:      一个self,其他参数根据需求确定
    返回值:    可有可无
'''


class Person():

    # 构造方法,参数除了cls外,其他在初始化方法中的参数,这里都要有
    def __new__(cls, *args, **kwargs):
        print('触发了构造方法')
        print(args)

        # 如果在该方法中没有返回如下格式,则无法创建对象
        return object.__new__(cls)

    # 初始化方法
    def __init__(self, name, age, sex):
        print('触发了初始化方法')
        self.name = name
        self.age = age
        self.sex = sex

    # 析构方法
    def __del__(self):
        print('触发了析构方法')

    def __call__(self, *args, **kwargs):
        print('把对象当作函数调用')


zs = Person('张三', 22, '男')
print(zs)  # <__main__.Person object at 0x0000022F701DB610>

zs()  # 把对象当作函数调用

'''
5. __len__
    触发机制:   当使用len函数去检测当前对象的时候自动触发
    作用:      可以使用len函数检测当前对象中某个数据的xinxi
    参数:      一个self接收当前对象
    返回值:    必须有,并且必须是一个整型
    注意:     len要获取什么属性的值,就在返回值中返回哪个属性的长度即可
6.__str__
    触发机制:   当使用str或print函数对对象进行操作时,自动触发
    作用:      代码对象进行字符串的返回,可以自定义打印的信息
    参数:      self
    返回值:     必须有,而且必须是字符串类型的值
7.__repr__
    触发机制:   在使用repr方法对当前对象进行转换时自动触发
    作用:      可以设置repr函数操作对象的结果
    参数:      self
    返回值:    必须有,而且必须是字符串类型的值
    注意:     正常情况下,如果没有__str__时,__repr__方法就会代替__str__魔术方法
8.__bool__
    触发机制:   当前使用bool函数转换当前对象时,自动触发,默认情况下对象会转为True
    作用:      可以代替对象进行bool类型的转换,可以转换任何数据
    参数:      self
    返回值:    必须时一个bool类型的返回值
'''


class Demo():
    listurl = [1,2,3]

    # 可以代替对象使用len函数,并返回一个指定的整型
    def __len__(self):
        return len(self.listurl)

    # 可以代替对象进行str或print的字符串信息返回
    def __str__(self):
        return '<这是当前脚本中的一个对象 str>'

    def __repr__(self):
        return '这是一个对象repr'

    def __bool__(self):
        return bool(self.listurl)

obj = Demo()
# res = len(obj)  # 3

print(obj)  # <这是当前脚本中的一个对象 str>
print(obj)  # 这是一个对象repr (不存在时,才执行repr,此时已将__str__注释)

# str  repr 和对应魔术方法的区别

# 认识str和repr的却别

num = 123
res1 = str(num)
res2 = repr(num)

# str 和 repr 函数都可以把其他类型的值传为字符串
print(res1, type(res1))  # 123 <class 'str'>
print(res2, type(res2))  # 123 <class 'str'>

s = '123'
r1 = str(s)
r2 = repr(s)
print(r1,type(r1))  # 123 <class 'str'>
print(r2,type(r2))  #'123' <class 'str'> repr解析的结果带了引号


'''
str 和 repr的区别
str 和 repr 函数都可以把其他类型的值传为字符串
str函数会把对象 转为 更适合人类阅读的形式
repr函数会把对象 转为 解释器读取的形式
如果数据对象并没有更明显的区别的话,str和repr的转为结果是一样的
'''

class Demo2():

    def __str__(self):
        return '123'

    def __repr__(self):
        return  '123'


obj = Demo2()
r1 = str(obj)  # 123 <class 'str'>
r2 = repr(obj)  # 123 <class 'str'>


# 成员相关魔术方法
'''
1. __getattribute__ 优先级最高
    触发机制:当访问对象成员时,自动触发,无论当前成员是否存在
    作用   : 可以在获取对象成员时,对数据进行处理
    参数   : 一个self接收对象, 一个 item 接收当前访问的成员名称
    返回值 : 可有可无,返回的值就是访问的结果
    注意事项:在当前的魔术方法中,禁止对当前对象的成员进行访问,会触发递归
            如果想要在当前魔术方法中访问对象的成员必须使用object来进行访问
            语法格式:object.__getattribute__(self, item)
2. __getattr__
    触发机制:当访问对象中不存在的成员时,自动触发
    作用   :防止访问不存在的成员时报错,也可以为不存在的成员进行赋值操作
    参数   :self, 一个item接收当前访问的成员名称
    返回值 :可有可无
    注意事项:当存在 __getattribute__ 方法时,会去执行__getattribute__ 方法
3. __setattr__
    触发机制:当给对象的成员进行赋值操作时会自动触发(包括添加,修改)
    作用   :可以限制或管理对象的添加和修改操作
    参数   :1.self 2.设置的成员名 3.设置的成员值
    返回值 :无
    注意事项:在当前的魔术方法中,禁止给当前对象成员直接进行赋值操作,会触发递归操作
            如果想要给当前对象的成员进行赋值,需要借助 object
            格式: object.__setattr__(self,item,value)
4. __delattr__
    触发机制:当删除对象成员时自动触发
    作用   :可以去限制对象成员的删除,还可以删除不存在成员时防止报错
    参数   :1.self 2.item
    返回值 : 无
    注意事项: 在当前魔术方法中禁止直接删除对象的成员,会触发递归操作
            如果想要删除当前对象的成员那么需要借助object
            格式: object.__delattr__(self,item)
'''
class Person():
    name = '名字'
    age = '年龄'
    sex = '性别'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        print('说')

    def sing(self):
        print('唱')

    # 获取对象成员时自动触发
    # def __getattribute__(self, item):
    #     try:
    #         # 不可以self.name 获取
    #         # print(self.name)  # RecursionError: maximum recursion depth exceeded
    #
    #         # 在方法中使用 object 来获取属性值
    #         res = str(object.__getattribute__(self, item))
    #         # 在方法中可以对访问的成员数据进行处理
    #         return res[0] + '*' + res[-1]
    #     except:
    #         return False

    # 当访问不存在的成员时,自动触发,此时已注释掉 __getattribute__ 方法)
    def __getattr__(self, item):
        return '不存在这个成员'

    # 当给对象成员赋值时触发,注意该方法中如果没有给对象成员赋值],那么对象成员赋值失败
    def __setattr__(self, key, value):
        print(self, key, value)  # <__main__.Person object at 0x000002441F9433D0> abc aabbcc
        object.__setattr__(self, key, value)

    # 当删除对象的成员时,自动触发
    def __delattr__(self, item):
        print(item)
        # 只有执行下面的语句,才会执行删除操作
        object.__delattr__(self, item)



zs = Person('张三', 20, '男')
print(zs.name)  # 张*三
print(zs.age)  # 2*0
# __getattr__ (此时已注释掉 __getattribute__ 方法)
# print(zs.tall)  # False

zs.abc ='aabbcc'
print(zs.abc)  # aabbcc

del zs.abc
print(zs.abc)  # 不存在这个成员 如果注释掉 object.__delattr__(self, item) 语句,则删除失败,依然可以返回 张三
