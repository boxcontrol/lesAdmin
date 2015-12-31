from flask import Flask, url_for
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
from config import basedir
from .solusvm import myServer



app = Flask(__name__, static_url_path='', static_folder='static')
app.config.from_object('config')  # load configuration from config.py file
db = SQLAlchemy(app)



lm = LoginManager()
lm.init_app(app)
lm.login_view = 'login'



from app import views
"""
# setup buttons for reboot, shutdown and boot
def clever_function(argument):
    return argument
"""