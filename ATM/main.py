# coding:utf-8


from packages.viewclass import Views
from packages.controllerclass import Controller


class Main():

    def __init__(self):
        # 实例化视图对象
        view = Views()
        # 实例化操作对象
        obj = Controller()

        while True:
            # 让用户选择操作
            num = input('请输入你要进行的操作')
            # 需要验证用户的输入是否正确
            code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            if num not in code:
                print('您输入的内容有误')
                view.showfunc()
                # 跳过本次循环
                continue
            if num == '1':
                obj.register()
            elif num == '2':
                obj.query()
            elif num == '3':
                obj.get_money()
            elif num == '4':
                obj.add_money()
            elif num == '5':
                obj.save_money()
            elif num == '6':
                obj.lock()
            elif num == '7':
                obj.unlock()
            elif num == '8':
                obj.new_card()
            elif num == '9':
                obj.change_pwd()
            elif num == '0':
                obj.save()
                break




if __name__ == "__main__":
    Main()
