# coding:utf-8

'''
python操作mysql
    1.连接mysql数据库
    2.创建游标对象
    3.准备sql语句
    4.用游标对象执行sql
    5.提取结果
    6.关闭数据库连接
连接mysql数据库时的cursorclass=pymysql.cursors.DictCursor
可以把结果转为字典类型,默认为元组
'''
import pymysql

# 1.连接mysql数据库
db = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    db='python4',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# 2.创建游标对象
cursor = db.cursor()

# 3.准备sql语句
sql = 'select version()'

# 4. 执行sql语句
cursor.execute(sql)

# 5.提取结果
data = cursor.fetchall()

# 6.关闭数据库连接
db.close()

print(data)  # [{'version()': '8.0.20'}]











