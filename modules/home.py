'''home page'''
from flask import Blueprint, render_template


home = Blueprint("example_blueprint", __name__)


@home.route('/')
def index():
    '''home'''
    return render_template('homepage.html')
