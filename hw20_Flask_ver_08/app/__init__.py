from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = '026dcb1fbc52810fb87cdf40cd832e07361e9f8b'
app.static_folder = 'static'
login_manager = LoginManager(app)

from app import routes
from app import database






