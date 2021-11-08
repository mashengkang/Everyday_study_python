# coding:utf-8


# 操作控制类
import random, pickle, os

from ATM.packages import cardclass, personclass


class Controller():
    # 数据存储格式
    userid_cardid = {}  # 身份证id:银行卡id
    cardid_userobj = {}  # 银行卡id:用户对象

    # 数据存储的url
    user_file_url = './databases/user.txt'  # 银行卡id:用户对象
    card_file_url = './databases/userid.txt'  # 身份证id:银行卡id

    def __init__(self):
        # 加载所有数据信息
        self.__loaddate()

    def __loaddate(self):
        # 检测文件是否存在
        if os.path.exists(self.card_file_url):
            # 读取数据
            with open(self.card_file_url, "rb") as fp:
                self.userid_cardid = pickle.load(fp)
                # print(self.userid_cardid)  # {'身份证': 银行卡号}

        if os.path.exists(self.user_file_url):
            # 读取数据
            with open(self.user_file_url, "rb") as fp:
                self.cardid_userobj = pickle.load(fp)
                # print(self.cardid_userobj)  # {206182: <ATM.packages.personclass.Person object}

    # 1.注册: regiser
    def register(self):
        # 获取用户输入的 用户名, 身份证号, 手机号, 密码
        name = self.__getuserinfo('用户名')
        userid = self.__getuserinfo('身份证号')
        # 检测当前身份证号是否已经存在
        if userid in self.userid_cardid:
            print(f'当前用户已存在,卡号为: {self.userid_cardid[userid]}')
            return
        phone = self.__getuserinfo('手机号')
        # 获取密码并判断两次输入密码是否一致
        password = self.__isuserpwd()

        # 创建一个银行卡
        cardid = random.randint(100000, 999999)
        cardobj = cardclass.Card(cardid, password)

        # 创建用户对象,和银行卡进行绑定
        userobj = personclass.Person(name,  userid, phone, cardobj)

        # 保存用户信息:创建需要保存的数据格式 {身份证号:cardobj} {cardid: userobj}
        self.userid_cardid[userid] = cardid
        self.cardid_userobj[cardid] = userobj

        # 完成创建
        print(f'恭喜你开户成功,卡号为:{cardid} 余额为:{cardobj.money}元')
        print('注册功能')

    # 2.查询: query
    def query(self):
        # 获取用户输入的卡号
        cardid = int(input('请输入您的卡号:'))
        # 验证卡号是否存在
        if cardid not in self.cardid_userobj:
            print(self.cardid_userobj)
            print('当前卡号不存在')
            return
        # 获取卡对象
        cardobj = self.cardid_userobj[cardid].card
        # 存在,输入密码
        if self.__checkpwd(cardobj):
            # 验证卡是否锁定
            if cardobj.islock:
                print('当前卡已锁定,请先解卡')
                return
            else:
                # 未锁定的话,执行查询
                print(f'您当前卡号为: {cardid},余额为:{cardobj.money} 元')

    # 3.取款: get_money
    def get_money(self):
        print('收款功能')

    # 4.存款: add_money
    def add_money(self):
        print('存款功能')

    # 5.转账: save_money
    def save_money(self):
        print('转账注能')

    # 6. 锁卡: lock
    def lock(self):
        print('锁卡功能')

    # 7.解卡: unlock
    def unlock(self):
        print('解卡功能')

    # 8.补卡: new_card
    def new_card(self):
        print('补卡功能功能')

    # 9.改密: change_pwd
    def change_pwd(self):
        print('改密功能')

    # 10.退出: save
    def save(self):
        # 把当前的数据 写入到文件中
        with open(self.card_file_url, 'wb+') as fp:
            pickle.dump(self.userid_cardid, fp)

        with open(self.user_file_url, 'wb+') as fp:
            pickle.dump(self.cardid_userobj, fp)

        print('退出成功')

    def __isuserpwd(self):
        while True:
            pwd = self.__getuserinfo('密码')
            repwd = input('请再次输入密码进行确认:')
            if repwd == pwd:
                print('两次输入密码一致')
                return pwd  # return函数就结束了,所以循环也已经结束
            else:
                print('两次密码不一致,请重新输入密码')



    # 检测密码是否正确
    def __checkpwd(self, cardobj):
        number = 3
        while True:
            pwd = input('请输入密码:')
            # 检测密码是否正确
            if pwd == cardobj.password:
                return True
            else:
                number -= 1
                if number == 0:
                    # 直接锁卡
                    cardobj.islock = True
                    print('您当前的卡已被锁定')
                    break
                else:
                    print(f'密码错误,您还有{number}次机会')

    # 循环获取用户数据
    def __getuserinfo(self, info):
        while True:
            userinfo = input(f'请输入您的{info}:')
            if not userinfo:
                print('输入内容有误,请重新输入')
                continue
            else:
                return userinfo

