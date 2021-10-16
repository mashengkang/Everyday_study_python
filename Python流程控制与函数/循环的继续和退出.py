# coding:utf-8

# continue break 一定是在循环体内,break执行时,else也不会执行

users = [
    {'username': 'xiaoma', 'age': 33, 'top': 174, 'sex': '男'},
    {'username': 'xiaoming', 'age': 32, 'top': 178, 'sex': '男'},
    {'username': 'xiaoxu', 'age': 31, 'top': 184, 'sex': '男'},
    {'username': 'xiaomei', 'age': 23, 'top': 164, 'sex': '女'},
]

man = []

for user in users:
    if user.get('sex') == '女':
        continue
    man.append(user)
    print(f'{user.get("username")} 加入了行列')

l = range(100)
for i in l:
    if i == 80:
        print('已经循环80次,要退出了')
        break
    print(i)
else:
    print('else执行了')