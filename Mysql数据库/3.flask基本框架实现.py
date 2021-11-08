# coding:utf-8
# 留言板 flask框架实现

'''
1.先实现web的基本搭建
2.创建留言板数据库
3.完成留言板的逻辑代码
'''
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "hello world!"

@app.route('/love')
def love():
    return 'i love you!'

if __name__ == "__main__":
    app.run(debug=False, host='127.0.0.1', port=8080)
