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


class users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50))  # 这里要改为不能重复，未改
    wx_id = db.Column(db.String(50))  # 这里要改为不能重复，未改
    sex = db.Column(db.String(2))
    age = db.Column(db.String(3))
    tel = db.Column(db.String(11))
    remark = db.Column(db.String(50))


if __name__ == '__main__':
    # db.drop_all()
    db.create_all()

    app.run(debug=True)
