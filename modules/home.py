'''home page'''
import os
from flask import Blueprint, render_template
from modules import PROJ_ADDRESS, AWS_ADDRESS

home = Blueprint("home", __name__)


if not os.path.exists(PROJ_ADDRESS):
    PROJ_ADDRESS = AWS_ADDRESS
DB_ADDRESS = PROJ_ADDRESS + "/database/db.sqlite3"


@home.route('/')
def index():
    '''home'''
    return render_template('homepage.html')
