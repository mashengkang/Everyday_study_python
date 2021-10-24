# coding:utf-8


# 专门定义数据变量,存放已经注册的数据
userlist = []  # 存放所有的用户名
pwdlist = []  # 存放密码
# 读取所有的注册信息,使用a+的模式打开文件,再调整指针位置,防止文件不存在时报错
with open('./user.txt', 'a+', encoding='utf-8') as fp:
    fp.seek(0)  # 调整指针再文件头部
    res = fp.readlines()
    for i in res:
        r = i.strip()  # qwe:123123 可以去掉\n
        arr = r.split(':')  # ['qwe', '123123']
        userlist.append(arr[0])
        pwdlist.append(arr[1])

    # print(res)  # ['qwe:123123\n', 'eqq:123321\n']


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


register()