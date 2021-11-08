# coding:utf-8


class Views():

    def __init__(self):
        self.__showindex()
        print('系统正在加载,请稍后...')
        self.showfunc()
    # 显示 欢迎界面
    def __showindex(self):
        varstr = '''
        *****************************
        *                           *
        *                           *
        *      Welcome To Bank      *
        *                           *
        *                           *
        *****************************
        '''
        print(varstr)

    # 显示 操作界面
    def showfunc(self):
        varstr = '''
        *****************************
        *    (1)注册     (2)查询     *
        *    (3)存款     (4)取款     *
        *    (5)转账     (6)改密     *
        *    (7)锁卡     (8)解卡     *
        *    (9)补卡     (0)退出     *
        ***********输入序号***********
        '''
        print(varstr)


if __name__ == "__main__":

    Views()