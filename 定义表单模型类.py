from atexit import register
from cProfile import label
from flask import Flask,render_template,request
# StringField,PasswordField用于获取字段（相当于前端文本框）
# SubmitField用于提交（相当于前端提交按钮）
from wtforms import StringField,PasswordField,SubmitField
from flask_wtf import FlaskForm
# 用于验证，如验证数据不能为空，验证数据是否相同（验证两次）
from wtforms.validators import DataRequired,EqualTo



# 使用数据库中的类的两种方式：实例化&继承
app = Flask(__name__)
# 用于保护代码的随机字符串
app.config['SECRET_KEY'] = 'asdweafassfwaw'
# 定义表单模型类
# 继承数据库中的类
class Register(FlaskForm):
    # 这里的label与validators均为关键字
    # label用于将文字与文本框进行关联，点击文字时锁定到文本框
    user_name = StringField(label='用户名',validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码',validators=[DataRequired('密码不能为空')])
    # EqualTO用于检测两次输入的密码是否相同
    password2 = PasswordField(label='再次输入密码',validators=[DataRequired('密码不能为空'),EqualTo('password')])
    # 提交
    submit = SubmitField(label='提交')

@app.route('/index',methods=['GET','POST'])
def ccc():
    # 创建表单对象
    form = Register()
    if request.method == 'GET':
        return render_template('003.html',form = form)
    if request.method == 'POST':
        # 验证数据是否正确
        # validate_on_submit
        # 表单传回来的数据如果是正确的就会往后面执行
        if form.validate_on_submit():
            # 对文本框中的内容进行获取
            username = form.user_name.data
            password = form.user_name.data
            password2 = form.user_name.data
            # 打印上面赋值后的变量
            print(username)
            print(password)
            print(password2)
            # 返回到003网页当中
            # form调用表单对象
        else:
            print('验证失败')
        return render_template('003.html',form = form)

if __name__ == '__main__':
    app.run()
    