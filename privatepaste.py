#!/usr/bin/env python
### Imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from flask import Response, jsonify, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask.ext.login import LoginManager # Not sure if keeping
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import current_user
from flask.ext.login import login_required
from contextlib import closing
from datetime import datetime
import sys, os
import base64, hashlib, hmac, time, struct
import urlparse
from wtforms import Form, BooleanField, TextField, PasswordField, validators # unsure if keeping
from flask.ext.sqlalchemy import SQLAlchemy
from database import db_session
from models import User
from gauth import newSecret, getQRLink, auth

appName = "PrivatePaste"

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

#login_manager = LoginManager()
#login_manager.setup_app(app)
#@login_manager.user_loader
#def load_user(user_id):
#    return Users(user_id)

#class Users:
#    def __init__(self, user_id):
#        self.id = user_id.lower()
#        self.db = 

class LoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=50)])
    password = PasswordField('Password', [validators.Required()])
    authcode = TextField('AuthCode', [validators.Required()])


@app.before_request
def check_user_status():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/auth-qr-code.png')
def auth_qr_code():
    domain = urlparse.urlparse(request.url).netloc

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        users_db = db_session.execute('SELECT id, name, gauth, password FROM users')
        for user in users_db:
            if not request.form['username'] in user[1]:
                error = "User not found"
            elif not check_password_hash(user[3], request.form['password']):
                error = "Password incorrect"
            elif not auth(user[3], request.form['authcode']):
                error = "Google Auth incorrect"

        
        #return redirect(url_for('home'))
    else:
        error = form.validate()
    return render_template('login.html', form=form, error=error)

@app.route('/logout', methods=['GET', 'POST'])
#@login_required
def logout():
    session.pop('logged_in', None)
    flash("You have been logged out")
    return redirect(url_for('home'))

@app.route('/', methods=['GET', 'POST'])
def home():
    title = "PrivatePaste v0.1"
    header = "PrivatePaste v0.1"
    defaulttext = ""
    return render_template('home.html', title=title, header=header, defaulttext=defaulttext)




if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    if port == 5000:
        app.debug = True
    else:
        app.debug = False
    #app.run(host='69.164.203.152')
    app.run(host='0.0.0.0', port=port)
    
