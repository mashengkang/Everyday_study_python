# coding:utf-8


# 银行卡类
class Card():
    # 卡号,秘密啊,余额,是否锁卡
    card_id = None
    password = None
    money = None
    islock = None

    def __init__(self, cardid, pwd, money=10, islock=False):
        self.card_id = cardid  # 卡号
        self.password = pwd  # 密码
        self.money = money  # 余额
        self.islock = islock  # 是否锁卡,False未锁卡
