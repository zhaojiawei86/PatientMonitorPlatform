'''home page'''
from flask import Blueprint

home = Blueprint("example_blueprint", __name__)


@home.route('/')
def index():
    '''home page'''
    return "Home Page"
