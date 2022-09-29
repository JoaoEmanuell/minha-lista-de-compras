from flask import Blueprint, render_template, request

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/')
def index():
    return 'User Route'

@user.route('/list')
def list_route():
    return render_template('list/index.html')

@user.route('/login')
def login_route():
    return render_template('login/index.html')

@user.route('/login_post', methods=['POST'])
def login_post_route():
    data = {
        'name': request.form['name'],
        'password': request.form['password']
    }
    return data
