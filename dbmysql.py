from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import pymysql

# 解决兼容老版本问题 ModuleNotFoundError: No module named 'MySQLdb'
pymysql.install_as_MySQLdb()

app = Flask(__name__)
# 此处已经改动，记得更改数据表
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/qrcode?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # 关掉数据跟踪修改
db = SQLAlchemy(app)  # 实例化db对象

# db.Model必须加上
class aaa(db.Model):
    __tablename__ = 'aaa'
    # primary_key=True  设置主键
    # autoincrement=True 下次事件触发时新建一行
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    zhanghao = db.Column(db.String(50))
    password = db.Column(db.String(50))


if __name__ == '__main__':
    # db.drop_all()
    # 创建一个表
    db.create_all()

    app.run(debug=True)
