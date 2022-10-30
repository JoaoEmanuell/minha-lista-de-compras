from flask import Flask, redirect

# Routes

from routes import user, api

app = Flask(__name__)

# Blueprints

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(api, url_prefix='/api')

@app.route('/')
def index():
    return redirect('/user')