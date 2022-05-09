from flask import render_template,redirect,request,urll_for,abort
from ..models import User
from . import main

# Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    return render_template('index.html')

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)