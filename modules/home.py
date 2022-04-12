'''home page'''
from flask import Blueprint, render_template


home = Blueprint("home", __name__)

PROJ_ADDRESS = "/Users/jiaweizhao/Desktop/PatientMonitorPlatform"
DB_ADDRESS = PROJ_ADDRESS + "/database/db.sqlite3"


@home.route('/')
def index():
    '''home'''
    return render_template('homepage.html')
