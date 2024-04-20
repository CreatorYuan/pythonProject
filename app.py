from flask import Flask

app = Flask(__name__)

# url: http[80]/https[443]://www.qq.com:443/path
# url与视图： path与视图


@app.route('/')
def hello_world():
    return 'Hello CreatorYuan'


@app.route('/profile')
def profile():
    return '我是个人中心'


@app.route('/blog/list')
def blog_list():
    return '我是博客列表'


# 1. debug模式  app.run(debug=True)
    # 1.1 修改代码后保存,就会自动加载重启
    # 1.2 浏览器就可以实时更新,不用每次都手动重启

# 2. 修改host  --host=0.0.0.0
    # 2.1 让其他电脑也能访问

# 3. 修改port端口号  --port=8000


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)
