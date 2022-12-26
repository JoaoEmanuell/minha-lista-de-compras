from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# app

app = Flask(__name__)
app.config.from_object("config")

# Login manager

login_manager = LoginManager()
login_manager.init_app(app)

# Sqlalchemy

sql_db = SQLAlchemy(app)
migrate = Migrate(app, sql_db)

# Models

from .source import (
    UserModel,
    ListModel,
    MongoDatabaseInterface,
    Factory,
    DatabaseInterface,
    SQLiteDatabaseInterface,
)
from .routes import user

with app.app_context():
    sql_db.create_all()

# Blueprints
app.register_blueprint(user, url_prefix="/user")
