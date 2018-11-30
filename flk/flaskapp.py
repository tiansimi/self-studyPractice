__author__ = 'lenovo'
from flask import Flask, request, render_template, flash

app = Flask(__name__)
app.secret_key = "1234567"


@app.route('/hello')
def hello_world():
    return "Hello World!！！"


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')

    if request.method == "POST":
        form = request.form  # form不是一个函数
        username = form.get("username")
        password = form.get("password")
        if not username:
            flash("用户名为空！")
            return render_template("login.html")
        if not password:
            flash("密码为空！")
            return render_template("login.html")

        if username == "zhangsan" and password == "123456":
            flash("登录成功!")
        else:
            flash("登录失败！")

        return render_template("login.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)


