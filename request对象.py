# request 包含前端发来的所有请求
# from crypt import methods
from flask import Flask, render_template, request


# 将app实例化
app = Flask(__name__)


@app.route('/index', methods=['GET', 'POST'])
def index():
    # 端口是index时是GET请求
    # 当在input框中输入数据之后是POST请求
    # '判断是get请求'
    if request.method == 'GET':
        return render_template('index.html')
    # '判断是post请求'
    if request.method == 'POST':
        # 获取网页当中的name的值并且赋值给aaa[get为获取关键字]
        aaa = request.form.get('name')
        # 获取网页当中的password并且赋值给bbb
        bbb = request.form.get('password')
        # return还可以返回到网页当中

        return str(aaa)
        return 'this is post'


if __name__ == '__main__':
    app.run()
