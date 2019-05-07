__author__ = '努力学习 不要让自己失望'
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/index")
def index():
    data = {
        "name": "python1",
        "age": "18",
        "list": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
    return render_template("index.html", **data)


@app.route("/xss", methods=["GET", "POST"])
def xss():
    text = ""
    if request.method == "POST":
        text = request.form.get("text")

    return render_template("xss.html", a=text)


def list_step_2(li):
    # 自定义过滤器
    return li[::2]

# 注册故过滤器
app.add_template_filter(list_step_2, "li2")

if __name__ == "__main__":
    app.run(debug=True)
