# coding:utf-8


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

try:
    # 2.创建游标对象
    cursor = db.cursor()

    # 3.准备sql语句
    sql1 = 'insert into users(name,age,sex,classid) values("小a",32,"女",1)'
    sql2 = 'select * from users'
    sql3 = 'delete from users where id=1'
    # 4. 执行sql语句, 返回行数
    row = cursor.execute(sql1)
    # 5.提交数据 在添加修改删除时,需要commit, 如果只是查询的话,可以不用
    db.commit()
    # 6.提取结果 fetchall() 提取所有的结果, fetchone() 提取一条结果
    # 如果不是查询类sql的话,则没有返回的结果
    data = cursor.fetchall()
    # 7.关闭游标对象
    cursor.close()
except Exception as e:
    db.rollback()  # 当代码出现错误时,进行回滚
    print(e)
finally:
    # 8.关闭数据库连接
    db.close()