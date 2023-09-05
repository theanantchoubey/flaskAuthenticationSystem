from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
import os
from functools import wraps
from forms import LoginForm, RegistrationForm

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = os.path.join('static', 'uploads')
app.config['SECRET_KEY'] = os.urandom(24).hex()  
limiter = Limiter(get_remote_address, app=app, default_limits=["200 per day", "50 per hour"])

# Temporary Database to use as of now
users = {
    'admin': {'password': 'adminPassword'},
    'user': {'password': 'userPassword'}
}

def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if not is_authenticated():
            flash('Authentication required. Please log in.', 'danger')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
@login_required
@limiter.limit("5/minute") # maximum of 5 requests per minute
def upload_form():
    return render_template('upload.html')

def is_authenticated():
    return 'user' in session

@app.route('/upload', methods=['POST'])
@login_required
def upload_image():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        return redirect(url_for('show_image', filename=filename))


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if authenticate_user(username, password):
            session['user'] = username
            flash('Login successful', 'success')
            return redirect(url_for('upload_form'))
        else:
            flash('Login failed. Please check your credentials.', 'danger')
    return render_template('login.html', form=form)
def authenticate_user(username, password):
    if username in users and users[username]['password'] == password:
        return True
    return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Registration successful. You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/uploads/<filename>')
@login_required
def show_image(filename):   
    return render_template('result.html', filename=filename)

@app.route('/logout')
@login_required
def logout():
    session.pop('user', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))

@app.route('/protected')
@login_required
def protected():
    return 'This is a protected route. Only authenticated users can access this page.'

if __name__ == '__main__':
    app.run(debug=True)
