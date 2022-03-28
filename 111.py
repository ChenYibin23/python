from crypt import methods
from flask import Flask
app = Flask(__name__)

# 通过修改url（在url后面加上app.route中的端口值，完成对函数的调用）
# 端口值为hello
# method表示可用请求时可用的方法   GET请求为输入url时发出的请求
# 当两个路由匹配的字符相同时，只会运行第一个路由中的内容
# endpoint为端口值


@app.route('/hello', methods=['GET', 'POST'], endpoint='hello')
def hello():
    return 'hello world'
# 可用的是POST请求但是不能使用GET请求


@app.route('/hi', methods=['POST', 'GET'], endpoint='hi')
def hi():
    return 'hi hi hi'


if __name__ == '__main__':
    app.run()
