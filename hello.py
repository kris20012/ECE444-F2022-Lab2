import email
from pickle import FALSE, TRUE
from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Email

hello = Flask(__name__)
hello.config['SECRET_KEY'] = 'hard to guess string'
bootstrap = Bootstrap(hello)
moment = Moment(hello)

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField('What is your U of T Email address?', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')


@hello.route('/', methods=['GET', 'POST'])
def index():
    
    substring = "utoronto"
    form = NameForm()
    
    if form.validate_on_submit():
        old_name = session.get('name')
        if old_name is not None and old_name != form.name.data:
            flash('Looks like you have changed your name!')
        session['name'] = form.name.data
        session['is_email'] = 0

        if (form.email.data).find(substring) != -1:
            session['is_email'] = 1
            print(session['is_email'])    
        flash('Looks like you have changed your email!')
        session['email'] = form.email.data
        return redirect(url_for('index'))
    return render_template('index.html',
        form = form, name = session.get('name'), 
        is_email = session.get('is_email'), 
        email = session.get('email'))