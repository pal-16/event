from flask import Flask, render_template, url_for
from init import app, db
import os
from sqlalchemy.orm import Session
from forms import RegistrationForm
from models import User

'''posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]

'''
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

'''
@app.route("/about")
def about():
    return render_template('about.html', title='About')

'''

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():

        user = User(username = form.username.data,email=form.email.data,password=form.password.data)
        db.session.add(user)
        db.session.commit()
        print("validated")

        '''flash(f'Account created!', 'success')'''
    return render_template('temp.html', title='Register', form=form)
