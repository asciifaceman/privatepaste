#!/usr/bin/env python
### Imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from flask import Response, jsonify, flash
from flask.ext.login import LoginManager
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
from gauth import newSecret, getQRLink, auth

appName = "PrivatePaste"

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.setup_app(app)

@login_manager.user_loader
def load_user(user_id):
    return Users(user_id)

class Users:
    def __init__(self, user_id):
        self.id = 

class LoginForm(Form):
    username = TextField('Username')
    password = PasswordField('Password')
    authcode = TextField('AuthCode')
    

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()

@app.route('/auth-qr-code.png')
def auth_qr_code():
    domain = urlparse.urlparse(request.url).netloc

@app.route('/login', methods=['GET', 'POST'])
def login():


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
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
    
