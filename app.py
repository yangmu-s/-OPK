from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    url = (url_for('new'))
    return "url反转%s" % url


@app.route('/new/')
def new():
    return "hello"


if __name__ == '__main__':
    app.run(host='192.168.1.124', port=8888)
