# ATM



## ATM系统项目说明文档

> 运用基础截断所学习的python的知识,来模拟出银行的ATM系统
>
> 要求:使用面向对象编程来完成这个项目

### ATM系统的主要功能:

1. 注册: 用户名,手机号,身份证号(18位),密码(两次确认,长度6位)
2. 查询: 账号必须存在,密码(三次机会,不对锁卡)
3. 取款: 账号必须存在,密码(三次机会,不对锁卡),取款金额不能大于存款
4. 存款: 账号必须存在,存款金额不能低于0
5. 转账: 你的账号,转款账号都必须存在,密码(三次机会,不对锁卡),转账金额不能超过余额
6. 锁卡:账号必须存在,可以使用密码冻结和身份证号冻结
7. 解卡: 账号必须存在,只能使用身份证好进行解锁
8. 补卡: 使用身份证进行补卡,每个身份证只能有一张卡, 之前的卡作废
9. 改密: 原密码改密,身份证改密
10.  0 退出: 保存数据

### 项目分析

> 根据需求进行分析,思考如何对项目进行设计和架构

#### 思考一:如何使用面向对象编程思想来完成

当前的项目功能和项目演示中,有几个对象??

##### 银行卡对象:Card 存储银行卡信息

- 卡号 		cardid
- 密码         password
- 余额         money
- 是否锁卡  islock

##### 用户对象:Person 存储用户信息

- 用户名	  name
- 身份证号  userid
- 手机卡      phone
- 卡              card

##### 控制器对象:Controller 具体的操作控制类

> 控制器对象中主要就是去实现ATM这个系统中的操作,十个方法

1. 注册: regiser
2. 查询: query
3. 取款: get_money
4. 存款: add_money
5. 转账: save_money
6. 锁卡: lock
7. 解卡:  unlock
8. 补卡: new_card
9. 改密: change_pwd
10. 退出:  save

##### 试图对象: Views 显示操作界面的

欢迎界面,操作界面

#### 思考二:如何存储数据

用文件进行存储

卡号:用户==> user_dict ==> user.txt

身份证:卡号 ==> user_id_dict ==> userid.txt

#### 开发周期

花四个小时左右的时间,去分析这个项目,可以先动手尝试一部分

花4-10个小时左右,可以去完成和实现这个项目

#### 扩展功能

给当前ATM增加一个交易记录的功能

就像存折一样,每次对金额的变动都需要记录下来

每个银行卡都有自己的交易记录

记录的格式:

[2021/11/4 12:12:12] 存款 200 元, 余额 300 元

[2021/11/4 13:13:13] 转账 向用户:张三, 卡号:100100 转账 100 元,余额: 200 元

## 项目基本功能

1. 注册: regiser
2. 查询: query
3. 取款: get_money
4. 存款: add_money
5. 转账: save_money
6. 锁卡: lock
7. 解卡:  unlock
8. 补卡: new_card
9. 改密: change_pwd
10. 退出:  save

## 项目基本结构

```python
E:\STUDY_PYTHON_EVERYDAY\ATM  	# 项目目录
│  main.py						# 单入口文件
│  README.md					# 项目文档
│
├─databases
│      user.txt					# 用户
│      userid.txt				# 银行卡
│
└─packages						# 包
        cardclass.py			# 银行卡类
        controllerclass.py 		# 操作控制类
        personclass.py			# 用户类
        viewclass.py			# 视图显示类
        __init__.py
```

## 运行环境

- 系统: windows/Linux/Mac
- 版本: python3.8
- 其他: 无

## 迭代计划

- 增加银行卡流水日志