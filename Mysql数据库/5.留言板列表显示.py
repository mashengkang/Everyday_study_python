from flask import Flask, render_template, request
import pymysql, time

app = Flask(__name__)
app.jinja_env.auto_reload = True




# 留言板列表
@app.route('/')
def index():
    # 1.获取所有留言板数据
    data = model('select * from lyb')

    # 2.把数据分配到模板中(html页面)
    return render_template("index.html", data=data)


# 定义视图
@app.route("/add")
def add():
    # 显示留言添加的页面
    return render_template("add.html")


# 定义视图函数 接收表单数据,完成数据的入库
@app.route("/insert", methods=["POST"])
def insert():
    # 1.接收表单数据
    data = request.form.to_dict()
    # 处理数据
    data['date'] = time.strftime('%Y-%m-%d %H:%M:%S')

    # 2.把数据添加到数据库
    sql = f'insert into lyb values(null,"{data["nikename"]}", "{data["info"]}","{data["date"]}")'
    res = model(sql)
    # 3.成功后页面跳转
    # 判断结果
    if res == 'EXc':
        return '<script>location.href="/"</script>'
    else:
        return '<script>alert("留言失败");location.href="/add/"</script>'


# 定义视图函数,接收id,完成数据删除
@app.route("/delete")
def del_into():
    # 1. 接收id
    id = request.args.get('id')

    # 2. 准备sql
    sql = f'delete from lyb where id={id}'
    # 3.执行sql
    res = model(sql)
    # 4.判断结果
    if res:
        return '<script>location.href="/"</script>'
    else:
        return '<script>alert("删除失败");location.href="/"</script>'


# 定义视图,接收id,完成修改数据
@app.route("/xiugai", methods=['GET', 'POST'])
def xiugai():
    data = request.form.to_dict()
    print(data)
    if not data:
        id = request.args.get('id')
        data = model(f'select * from lyb where id={id}')
        return render_template("xiugai.html", data=data[0])

    else:
        date = time.strftime('%Y-%m-%d %H:%M:%S')
        for i in data.keys():
            if i == 'info':
                info = data['info']
            else:
                nikename = data[i]
                id = int(i)

        sql = f'update lyb set nikename="{nikename}", info="{info}",date="{date}" where id={id}'
        print(sql)
        res = model(sql)
        # 3.成功后页面跳转
        # 判断结果
        if res:
            return '<script>location.href="/"</script>'
        else:
            return '<script>alert("修改失败");location.href="/xiugai/"</script>'


# 定义视图


# 封装mysql操作方法
def model(sql):
    db = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='pymysql',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )
    try:
        cursor = db.cursor()
        # 执行sql语句, 返回行数
        row = cursor.execute(sql)
        # 提交数据
        db.commit()
        # 6.提取结果 fetchall() 提取所有的结果, fetchone() 提取一条结果
        # 如果不是查询类sql的话,则没有返回的结果
        data = cursor.fetchall()
        cursor.close()

        # 返回结果,如果有结果,返回结果,没有就返回函数
        if data:
            return data
        else:
            return row

    except Exception as e:
        db.rollback()  # 当代码出现错误时,进行回滚
        print(e)
        return 'Exc'
    finally:
        # 8.关闭数据库连接
        db.close()


@app.route('/love')
def love():
    return 'i love you!'


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=8080)
