# coding:utf-8


# 注册功能
# 专门定义数据变量,存放已经注册的数据
userlist = []  # 存放所有的用户名
pwdlist = []  # 存放密码
blacklist = [] # 黑名单用户

# 读取所有的注册信息,使用a+的模式打开文件,再调整指针位置,防止文件不存在时报错
with open('./user.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)  # 调整指针再文件头部
    res = fp.readlines()
    for i in res:
        r = i.strip()  # qwe:123123 可以去掉\n
        arr = r.split(':')  # ['qwe', '123123']
        userlist.append(arr[0])
        pwdlist.append(arr[1])

# 设置黑名单
with open('./black.txt', 'a+', encoding='utf-8') as bf:
    bf.seek(0)
    res = bf.readlines()
    for i in res:
        blacklist.append(i.strip())

print(userlist)  # ['qwe', 'eqq', 'msk1', 'msk2']
print(pwdlist)  # ['123123', '123321', '123321', '123123']


# 封装函数实现登录功能
def login():
    islogin = True
    # 定义变量,检测输入密码次数
    errornum = 3
    while islogin:
        # 获取用户登录时输入的用户名
        username = input('欢迎登录,请输入您的用户名:')
        # 检测当前用户名是否存在
        if username in userlist:
            # 检测用户是否属于锁定状态
            if username in blacklist:
                print('当前用户名已锁定')
                # islogin = False
            else:
                while True:
                    # 让用户输入密码
                    pwd = input('请输入密码:')
                    # 获取用户名在用户名列表中的索引
                    inx = userlist.index(username)
                    # 判断输入的密码是否正确
                    if pwd == pwdlist[inx]:
                        print('登录成功')
                        # 结束循环
                        islogin = False
                        break
                    else:
                        errornum -= 1
                        if errornum == 0:
                            print('3次输入密码错误,账号锁定')
                            # 如何锁定账户信息? 把需要锁卡的用户拉入黑名单
                            with open('./black.txt', 'a+', encoding='utf-8') as bf:
                                bf.write(username + '\n')
                            islogin = False
                            break
                        print(f'密码错误,请重新输入,还有{errornum}次机会')
        else:
            # 用户名不存在
            print('用户名错误,请重新输入')


login()