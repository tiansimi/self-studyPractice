__author__ = '努力学习 不要让自己失望'
from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm  # 导入wtf扩展的表单类
from wtforms import StringField, SubmitField  # 导入自定义表单需要的字段
from wtforms.validators import DataRequired, EqualTo

app = Flask(__name__)

app.config["SECRET_KEY"] = "66666"

class RegisterForm(FlaskForm):
    '''自定义注册表单模型类'''
    # datarequire保障数据必须填写并且不能为空
    #                               name          验证器
    user_name = StringField(label="用户名：", validators=[DataRequired("用户名不能为空！")])
    password = StringField(label="密码：", validators=[DataRequired("密码不能为空！")])
    password2 = StringField(label="确认密码：", validators=[DataRequired("密码不能为空！"), EqualTo("password",
                                                                    "两次密码不一致！")])
    submit = SubmitField(label="提交")


@app.route("/register", methods=["GET", "POST"])
def register():
    #创建表单对象
    form = RegisterForm()
    if form.validate_on_submit():
        uname = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(uname, pwd, pwd2)
        session["user_name"] = uname
        return redirect(url_for("index"))
    return render_template("register.html", form=form)

@app.route("/index")
def index():
    user_name = session.get("user_name", "")
    return "hello %s" % user_name



if __name__ == "__main__":
    app.run(debug=True)
