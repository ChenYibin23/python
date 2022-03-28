# 重定向


from flask import Flask, redirect, url_for


app = Flask(__name__)

# 当url加上/index之后便会自动调用下面的aaa函数，运行aaa函数之后通过重定向跳转到指定的网页当中


@app.route('/index')
def aaa():
    # 重定向到的网址(网址前需要加上https://（代表协议内容）)
    return redirect('https://www.baidu.com')


@app.route('/')
def hello():
    return 'this is hello fun'


if __name__ == '__main__':
    app.run()
