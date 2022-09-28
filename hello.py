from flask import Flask

hello = Flask(__name__)

@hello.route('/')
def index():
    return "<h1>Hello World!</h1>"

@hello.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)