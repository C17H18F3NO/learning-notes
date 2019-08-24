# 从 flask 包导入 Flask 类
from flask import Flask

# 通过实例化这个类，创建一个程序对象 app
app = Flask(__name__)


# 使用 app.route() 装饰器将函数绑定对应的 URL，
# 当用户在浏览器访问这个URL 的时候就去会触发这个函数，获取返回值，并把返回值显示到浏览器窗口
# 填入 app.route() 装饰器的第一个参数是 URL 规则字符串，这里的 / 指的是根地址
@app.route('/')
# 装饰器注册的处理函数，该函数是处理某个请求的处理函数，Flask 官方把它叫做视图函数（view function) ,
# 可理解为处理函数
def hello_world():
    # 返回响应内容
    return 'Hello World!'


if __name__ == '__main__':
    # Flask 应用程序实例的 run 方法启动 web 服务器
    app.run()


# 在终端上运行  flask run
