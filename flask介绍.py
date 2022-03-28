from flask import Flask

app = Flask(__name__)

# 路由
# 点击URL之后会到路由中进行匹配，匹配到之后运行index
# 运行之后返回值‘hello world’到网页当中


@app.route('/user/<id>')
def index(id):
    # 返回值到网页当中
    if id == str(1):
        return'111111111'
    else:
        return 'hello world'


app.run()
