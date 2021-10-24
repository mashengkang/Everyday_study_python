# coding:utf-8

# 功能的合并
# 专门定义数据变量,存放已经注册的数据
userlist = []  # 存放所有的用户名
pwdlist = []  # 存放密码
blacklist = [] # 黑名单用户


# 读取所有数据的方法
def readallusers():
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


# 封装一个函数.完成注册功能
def register():
    # 定义一个变量,用于控制循环
    site = True
    # 循环执行用户输入用户名
    while site:
        username = input('欢迎注册,请输入用户名:')
        if username in userlist:
            print('当前用户已存在,请更换用户名:')
        else:
            while True:
                # 输入密码
                pwd = input('请输入密码:')
                # 检测密码长度是否不低于3位
                if len(pwd) >= 6:
                    # 再次输入密码
                    repwd = input('请再次输入密码:')
                    if pwd == repwd:
                        # 用户名和密码正确,就可以写入文件
                        with open('./user.txt', 'a+', encoding="utf-8") as wf:
                            wf.write(f'{username}:{pwd}\n')
                        print(f'注册成功,用户名位:{username}')
                        # 结束外循环
                        site = False
                        # 结束内循环
                        break
                    else:
                        print('两次密码不一致,请重新输入')
                else:
                    print('密码格式不正确,最小6位密码')


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


# 判断当前的脚本是否作为一个主进程脚本在执行
if __name__ == "__main__":
    # 这里的代码,只有在使用python解释器直接运行时才执行
    # 如果当前的脚本,作为了一个模块被其他的文件导入后使用,那么这个地方的代码不会执行
    # 因为这个地方的代码,适合写当前脚本中国内的一些测试,这样不会影响其他脚本

    # 初始化数据方法,加载数据
    readallusers()
    while True:
        vars = '''
        ******************************
        **登录(1)*注册(2)*退出(其他按键)**
        ******************************
        '''
        print(vars)

        # 让用户选择对应的操作
        num = input('请输入对应的序号,体验功能:')
        if num == "1":
            login()
            break
        elif num == "2":
            register()
            readallusers()
            login()
            break
        else:
            print('其他功能待开发')
