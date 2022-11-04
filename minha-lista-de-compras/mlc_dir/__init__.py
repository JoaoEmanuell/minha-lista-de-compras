from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# app

app = Flask(__name__)
app.config.from_object('config')

# sqlalchemy

sql_db = SQLAlchemy(app)
migrate = Migrate(app, sql_db)

login_manager = LoginManager()
login_manager.init_app(app)