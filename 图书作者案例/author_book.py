__author__ = '努力学习 不要让自己失望'
from flask import Flask, render_template, request, redirect, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)


class Config(object):
    # sqlalchemy的配置参数
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://dev:fjrUWqUp4WVi8PE@116.196.103.195:3306/test"
    # sqlachemy自动跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = "66666666"


app.config.from_object(Config)
db = SQLAlchemy(app)


class Author(db.Model):
    '''作者'''
    __tablename__ = "tbl_authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    # 关联book模型类
    books = db.relationship("Book", backref="author")


class Book(db.Model):
    '''书籍'''
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey("tbl_authors.id"))

class AuthorBookForm(FlaskForm):
    '''作者表单数据模型类'''
    author_name = StringField(label="作者", validators=[DataRequired("必填项")])
    book_name = StringField(label="书名", validators=[DataRequired("必填项")])
    submit = SubmitField(label="保存")


@app.route("/", methods=["GET", "POST"])
def index():
    # 创建表单对象
    form = AuthorBookForm()
    if form.validate_on_submit(): # 验证表单成功
        # 提取表单数据
        author_name = form.author_name.data
        book_name = form.book_name.data
        # 保存数据库
        author = Author(name=author_name)
        db.session.add(author)
        db.session.commit()

        book = Book(name=book_name, author_id=author.id)
        db.session.add(book)
        db.session.commit()

    # 查询数据库
    author_li = Author.query.all()
    return render_template("author_book.html", authors=author_li,form=form)
@app.route("/delete_book", methods=["POST"])
def delete_book():
    # 提取参数
    # 直接提取前端发送的json数据，并转化成字典格式
    req_dict = request.get_json()
    book_id = req_dict.get("book_id")
    # 删除数据
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()

    return jsonify(code=0, message="OK")


if __name__ == "__main__":
    '''db.create_all()
    au_1 = Author(name='胖胖爱吃西红柿')
    au_6 = Author(name='米宝宝')
    au_2 = Author(name='TQ')
    au_3 = Author(name='录宝宝')
    au_4 = Author(name='青梧公主')
    # db.session.add_all([au_1, au_2, au_3, au_4, au_6])
    # db.session.commit()

    bk_mi = Book(name="小企鹅乐园 ", author_id=au_6.id)
    bk_lu = Book(name="围城", author_id=au_3.id)
    bk_tq = Book(name='吞噬星空', author_id=au_2.id)
    # db.session.add_all([bk_lu, bk_mi, bk_tq])
    # db.session.commit()
    bk_mi = Book(author_id=au_6.id)
    db.session.add(bk_mi)
    db.session.commit()
'''

    app.run(debug=True)

