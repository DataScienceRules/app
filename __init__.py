from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_socketio import SocketIO, send
#import socketio
import eventlet

app = Flask(__name__)
app.config['SECRET_KEY'] = '9e23234101efa0a821a7ac47ad593788'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
socketio = SocketIO(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

user_session_ids = dict()

#sio = socketio.Server()

from app import routes
