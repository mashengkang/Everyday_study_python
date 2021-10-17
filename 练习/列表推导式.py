# coding:utf-8

# 1.把字典中的键值对改成a=b的数据格式
'''
字典 {'user':'admin','age': 20, 'phone': '133'}
列表 ['user=admin', 'age=20', 'phone=123'
'''
vardict = {'user':'admin','age': 20, 'phone': '133'}
newlist1 = [i + '=' + str(vardict[i]) for i in vardict]
newlist2 = [k +'='+str(v) for k, v in vardict.items()]
print(newlist1)  # ['user=admin', 'age=20', 'phone=133']
print(newlist1)  # ['user=admin', 'age=20', 'phone=133']
print('&'.join(newlist2))  # user=admin&age=20&phone=133


# 2.把列表中的所有的字符全部转为小写
# ['AAAAA','BBbbb','ccCCc'] ==>['aaaaa','bbbbb','ccccc]
varlist = ['AAAAA','BBbbb','ccCCc']
newlist = [i.lower() for i in varlist]
print(newlist)  # ['aaaaa', 'bbbbb', 'ccccc']


# 3. x 是0-5之间的偶数,y是0-5之间的奇数,把xy组成一个元组,放到列表中
newlist = [(x, y) for x in range(6) for y in range(6) if x % 2 == 0 and y % 2 != 0]
print(newlist)  # [(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5)]


# 4. 使用列表推导式,完成九九乘法表
newlist = [f'{i}*{j}={i*j}' for i in range(1, 10) for j in range(1, i+1)]
print(newlist)


# 5. 求M,N中矩阵和元素的乘积
'''
M=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
N=[
    [2,2,2],
    [3,3,3],
    [4,4,4]
]
实现乘积的结果
(1) ==>[2,4,6,12,15,18,28,32,36]
(1) ==>[[2,4,6],[12,15,18],[28,32,36]]
'''
M=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
N=[
    [2,2,2],
    [3,3,3],
    [4,4,4]
]
print('--------------')
# 常规(1)
res = []
for i in range(3):
    for j in range(3):
        result = M[i][j]*N[i][j]
        res.append(result)
print(res)
# 列表推导式(1)
newlist = [M[i][j]*N[i][j] for i in range(3) for j in range(3)]
print(newlist)  # [2, 4, 6, 12, 15, 18, 28, 32, 36]

# 常规(2)
res1 = []
for i in range(3):
    res2 = []
    for j in range(3):
        result = M[i][j]*N[i][j]
        res2.append(result)
    res1.append(res2)
print(res1)
# 列表推导式(2)
newlist = [[M[i][j]*N[i][j] for j in range(3)]for i in range(3)]
print(newlist)  # [[2, 4, 6], [12, 15, 18], [28, 32, 36]]