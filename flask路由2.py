# from crypt import methods
from flask import Flask
app = Flask(__name__)

# user后面的/<id>会获取网页url的端口值并调用函数


#  @app.route('/user/<id>')
# 用这种写法不需要转换类型（可添加多种类型）
# string：接受任何不包含/的文本
# float接受正浮点数
# int：接受正整数
# 接受包含斜杆的文本
@app.route('/user/<int:id>')
def index(id):
    # 添加端口值，返回时的端口值是string形式，需要转换形式判断
    if id == str(1):
        return 'python'
    if id == '2':
        return 'bbb'
    if int(id) == 3:
        return 'ccc'
    # 输入的值非上面的值时输出下面的内容
    return 'hello world'


if __name__ == '__main__':
    app.run()
