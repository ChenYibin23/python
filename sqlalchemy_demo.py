from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)




# 解决兼容老版本问题 ModuleNotFoundError: No module named 'MySQLdb'
pymysql.install_as_MySQLdb()

# 对sqlalchemy进行实例化
# config中存着app的配置
# 添加数据库的地址
# app.config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root(用户名):root(数据库密码)@127.0.0.1(域名)/mysql_demo(数据库名)'
# ?charset用于设置编码方式
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/mysql_demo?charset=utf8'
# 跟踪数据库的修改，需要关闭
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# 实例化db对象
db = SQLAlchemy(app)


# 数据库的模型，需要继承db.Model
class Roles(db.Model):
    # 定义表名
    __tablename__ = 'Roles'

    # 定义字段
    # db.Column表示是一个字段
    # primary_key设置id为主键
    # unique设置name只能是唯一值
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(16),unique=True)

class User(db.Model):
    # 定义表名
    __tablename__ = 'User'
    user_id = db.Column(db.Integer,primary_key=True)
    user_name = db.Column(db.String(16),unique=True)
    # db.ForeignKey('roles.id')  表示是外键，表名.id  (此处的表名是其他表的)
    # 设置外键之后与外键关联的原列表的主键行不可删除
    role_id = db.Column(db.Integer,db.ForeignKey('Roles.id'))


@app.route('/')
def index():
    return 'hello world'


if __name__ == '__main__':
    # 先删除表，保证数据库中没有过多的其他表
    db.drop_all()
    # 创建表
    db.create_all()
    app.run(debug=True)
