from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime

hello = Flask(__name__)
bootstrap = Bootstrap(hello)
moment = Moment(hello)

@hello.route('/')
def index():
    return render_template('index.html',
                           current_time=datetime.utcnow())


@hello.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)