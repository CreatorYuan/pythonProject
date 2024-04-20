from flask import Flask, request, render_template
from datetime import datetime


app = Flask(__name__)


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

# url: http[80]/https[443]://www.qq.com:443/path
# url与视图： path与视图
# 渲染模板 render_template("index.html")


@app.route('/')
def hello_world():
    user = User(username="CreatorYuan", email="724991661@qq.com")
    person = {
        "username": "CY",
        "email": "cy@qq.com"
    }
    return render_template("index.html", user=user, person=person)


# 使用自定义过滤器
def datetime_format(value, format="%Y-%d-%m %H:%M"):
    return value.strftime(format)


app.add_template_filter(datetime_format, "dformat")


# Jinja2 内置过滤器, 使用加| , user.username|length
# length abs default
@app.route('/filter')
def filter_demo():
    user = User(username="CreatorYuan", email="724991661@qq.com")
    mytime = datetime.now()
    return render_template("filter.html", user=user, mytime=mytime)


@app.route('/profile')
def profile():
    return '我是个人中心'


@app.route('/blog/list')
def blog_list():
    return '我是博客列表'


# 带参数的url: 将参数固定在path中 <blog_id>
# <int:blog_id>: 指定参数类型
# 参数可传可不传
@app.route('/blog/<blog_id>')
def blog_detail(blog_id):
    return render_template("blog_detail.html", blog_id=blog_id, username="CreatorYuan")


# /blog/list : 会给我返回第一页的数据
# /blog/list?page=2 : 获取第二页的数据
@app.route('/book/list')
def book_list():
    # arguments : 参数
    # request.args : 类字典类型
    page = request.args.get("page", default=1, type=int)
    return f"你获取的是第{page}页的图书列表"


@app.route('/control')
def control_statement():
    age = 32
    books = [{
        "name": "三国演义",
        "author": "罗贯中"
    }, {
        "name": "水浒传",
        "author": "施耐庵"
    }, ]
    return render_template("control.html", age=age, books=books)


@app.route("/child1")
def child1():
    return render_template("child1.html")


@app.route("/child2")
def child2():
    return render_template("child2.html")


@app.route("/static")
def static_demo():
    return render_template("static.html")


# 1. debug模式  app.run(debug=True)
    # 1.1 修改代码后保存,就会自动加载重启
    # 1.2 浏览器就可以实时更新,不用每次都手动重启

# 2. 修改host  --host=0.0.0.0
    # 2.1 让其他电脑也能访问

# 3. 修改port端口号  --port=8000


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
