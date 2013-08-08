#!/usr/bin/env python
### Imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from flask import Response, jsonify, flash
from contextlib import closing
from datetime import datetime
import sys, os
import base64, hashlib, hmac, time, struct
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask.ext.sqlalchemy import SQLAlchemy

appName = "PrivatePaste"

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)




@app.route('/', methods=['GET', 'POST'])
def home():
    title = "PrivatePaste v0.1"
    header = "PrivatePaste v0.1"
    defaulttext = ""
    return render_template('home.html', title=title, header=header, defaulttext=defaulttext)




if __name__ == '__main__':
    app.run(host='69.164.203.152')
    
