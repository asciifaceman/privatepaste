#!/usr/bin/env python
### Imports
from flask import Flask, request, session, g, redirect, url_for, abort, render_template
from flask import Response, jsonify, flash
from contextlib import closing
from datetime import datetime
import sys, os
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
db = SQLAlchemy(app)

