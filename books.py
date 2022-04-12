from pickle import TRUE
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import pymysql
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# 解决兼容老版本问题 ModuleNotFoundError: No module named 'MySQLdb'
# 需要引用pymysql
pymysql.install_as_MySQLdb()

app = Flask(__name__)

# 创建db对象

# 添加密钥
app.secret_key = 'hunxiao'

# 连接数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/books?charset=utf8'
# 跟踪数据库的修改，需要关闭
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# 引用FlaskForm表单类


class BookForm(FlaskForm):
    author_name = StringField('作者名：', validators=[DataRequired()])
    book_name = StringField('书名：', validators=[DataRequired()])
    submit = SubmitField('提交')


class Author(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 引用关系
    # 在Author模型中使用时books可以代指另外的模型类Book
    # 在Book模型中使用时Author可以代指本模型
    books = db.relationship('Book', backref='Author')

    # def __repr__(self):
    #     return 'Author:%s' % (self.name)
# 定义书籍类


class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(16), unique=True)
    # 设置一个与表authors中id关联的键
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'))

    # def __repr__(self):
    #     return 'Author:%s,%s' % (self.name, self.author_id)

# app = Flask(__name__)


@app.route('/index/<author_id>')
# <author_id>可以用于将前端的author_id传回到后端
def delete_author(author_id):
    # 此处需要传回参数author_id,此处author_id所指的就是前端传回的author_id，不能随意修改
    # 获取到id为author_id的这一行的数据
    text = Author.query.get(author_id)
    # text若存在则判断成立
    if text:
        try:
            # 查找到Book模型中author_id=text.id的这一行并进行删除
            Book.query.filter_by(author_id=text.id).delete()
            db.session.delete(text)
            db.session.commit()
        except Exception as e:
            print(e)
            flash('删除作者失败')
            db.session.rollback()
    else:
        flash('要删除的作者不存在')
    # url中写上路由中的视图函数名用于代指路由，此处因路由不断不断发生变化，故需要使用url_for的方式
    return redirect(url_for('index'))


@app.route('/index/<route_id>')
def delete(route_id):
    # 先查询
    # 此处的id是路由器的端口设定的route_id
    # 且由前端定义之后这里代指Book中的id
    # 此处获取的是数据库中一整行的数据
    text = Book.query.get(route_id)
    # 后判断
    if text:
        # 此处try是尝试进行操作
        try:
            db.session.delete(text)
            db.session.commit()
        # except Exception as (返回值)   当try尝试不通过时运行此命令
        # e代指传回的错误
        except Exception as e:
            print(e)
            flash('删除出现错误')
            # 进行数据库的录入操作如果不成功则需要进行回滚
            db.session.rollback()
    else:
        flash('要删除的书籍不存在')
    return redirect(url_for('index'))


@app.route('/', methods=['POST', 'GET'])
def index():
    # print(authors)
    # 引用自己定义的模型BookForm
    book_form = BookForm()
    # 设置验证逻辑
    if book_form.validate_on_submit():
        # 通过验证获取表单book_form中用户输入的信息
        authors_name = book_form.author_name.data
        books_name = book_form.book_name.data
        # 查找到Author模型中name=authors_name的数据，并获取其中的第一个值(即id,具体输出为<Author id>,获取不到则为None)
        # 逻辑：用户输入的值在数据库中已存在，则author_exist有值
        author_exist = Author.query.filter_by(name=authors_name).first()
        print('获取到的值为：%s' % author_exist)
        # 判断作者是否存在，如果表中存在于authors_name相同的名字，则将此名字赋值给author_exist
        # 若不存在则author_exist为空，据此进行下列判断
        if author_exist:
            # 不为空
            # 查找到Book模型中name=books_name的数据，并获取其中的第一个值(即id,具体输出为<Author id>,获取不到则为None)
            book_exist = Book.query.filter_by(name=books_name).first()
            if book_exist:
                # 不为空
                flash('同名书籍已存在')
            else:
                try:
                    new_book = Book(name=books_name, author_id=author_exist.id)
                    db.session.add(new_book)
                    db.session.commit()
                except Exception as e:
                    print(e)
                    flash('添加书籍失败1')
                    # 提交出现问题则进行回滚
                    db.session.rollback()

        else:
            # 为空
            try:
                new_author = Author(name=authors_name)
                db.session.add(new_author)
                db.session.commit()
                new_book = Book(name=books_name, author_id=new_author.id)
                db.session.add(new_book)
                db.session.commit()

            except Exception as e:
                print(e)
                flash('添加书籍失败2')
                db.session.rollback()
    else:
        if request.method == 'POST':
            flash('参数错误')
    # 查询模板Author中的全部作者信息传回给authors
    # query用于进行查询数据库中的值
    authors = Author.query.all()
    # 需要在插入数据之后获取，才能够在刷新时获得插入的值

    return render_template('books.html', users=authors, book_form=book_form)


if __name__ == '__main__':
    # 删表
    db.drop_all()
    # 建表
    db.create_all()
    au1 = Author(name='老王')
    au2 = Author(name='老张')
    au3 = Author(name='老刘')
    db.session.add_all([au1, au2, au3])
    db.session.commit()
    bk1 = Book(name='随便打的介绍1', author_id=au1.id)
    bk2 = Book(name='随便打的介绍2', author_id=au2.id)
    bk3 = Book(name='随便打的介绍3', author_id=au3.id)
    bk4 = Book(name='随便打的介绍4', author_id=au3.id)
    bk5 = Book(name='随便打的介绍5', author_id=au3.id)
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    db.session.commit()
    app.run(debug=TRUE, host='127.0.0.1', port=5000)
