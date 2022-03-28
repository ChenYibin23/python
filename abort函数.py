# raise 主动抛出异常
# abort 在网页中抛出异常
# request返回前端发来的所有请求
# render_template用于网页的跳转

# from urllib import request
from flask import Flask, abort, render_template, request

app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        # 当输入的name与password满足以下条件时就会返回login success
        if name == 'zhangsan' and password == '123':
            return 'login success'
    else:
        abort()


# 自定义错误处理方法
# 错误控制器errorhandler，当出现404错误时自动调用下面的函数
@app.errorhandler(404)
def error(aaa):
    return render_template('001.html')
    return '出现了404错误,错误为%s' % aaa
# 若render_template跳转的网页当中有图片，需要将图片放在与python文件同级的static文件夹当中


if __name__ == '__main__':
    app.run()
