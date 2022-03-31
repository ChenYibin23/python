
from flask import Flask, render_template, request, flash
# 使用wtf之前都需要提前引入
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
# stringfield用于生成账号框
# passwordfield用于生成密码框
# submitfield用于生成提交按钮
# 用于定义格式

from wtforms.validators import DataRequired, EqualTo
# DataRequired用于验证输入框是否为空，EqualTo用于验证两次填写的密码是否相同

app = Flask(__name__)
# 给模板传递信息


# flash -->需要对内容进行加密，因此需要设置secret_key，做加密混淆
# 模板中需要遍历get_flashed_messages以打印flash中的message
app.secret_key = 'hunxiao'


@app.route('/', methods={'GET', 'POST'})
def index():
    # return 'hello world'
    url_str = 'www.itheima.com'
    list01 = [1, 2, 3, 4, 5]
    dict01 = {"name": '张三', "age": 18}
    # 让网页中的url_str=python中的url_str
    return render_template('示例001.html', url_str=url_str, my_list=list01, my_dict=dict01)


# 设置端口使用<e>可自定义端口内容，
# 将其在视图函数中获取之后可在函数中进行操作
# 限定输入的端口值的类型为int
@app.route('/order/<int:e>')
def get_order_id(e):
    # 显示e的类型
    print(type(e))
    # python中变量的输出形式
    return '%s' % e


# 使用WTF实现表单类
# 自定义表单类

# 引用表单FlaskForm
class LoginForm(FlaskForm):
    # 后面（）中设置函数的返回值label
    username = StringField('用户名：', validators=[DataRequired()])
    password = PasswordField('密码：', validators=[DataRequired()])
    password2 = PasswordField(
        '验证密码：', validators=[DataRequired(), EqualTo('password', '密码填入不一致')])
    # EqualTo中的password用于将将passwoed2与password进行比较，message可自定义
    submit = SubmitField('提交')


@app.route('/form', methods=['POST', 'GET'])
def login():
    url_form = LoginForm()
    if request.method == 'POST':
        # 获取请求的参数
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 当所有验证都通过时运行
        if url_form.validate_on_submit():
            print(username, password)
            return "success"
        else:
            flash('参数有误')

    return render_template('request.html', form=url_form)


@app.route('/index', methods=['GET', 'POST'])
def inde():
    if request.method == 'GET':
        url_form = LoginForm()
        return render_template('request.html', form=url_form)
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        # 判断三个参数都不能为空
        if not all([username, password, password2]):
            # flash函数运行时，会将其中的值传回前端，之后需要在前端对get_flash_messages进行遍历将其显示在前端的页面当中
            flash('参数不完整')
        # 判断两次输入的密码是否相同
        elif password != password2:
            flash('密码不一致')
        else:
            return '登陆成功'

        return render_template('request.html', form=url_form)


    # request获取前端请求时传回的数据
if __name__ == '__main__':
    app.run(debug=True)
