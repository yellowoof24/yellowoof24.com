from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
  return '<h1>님 바보임 ㅅㄱ</h1>'
@app.route('/<name>')
def babaoname(name):
  return '<h1>' + name + '님 바보임 ㅅㄱ</h1>'

app.run(host="0.0.0.0", port="8080")
