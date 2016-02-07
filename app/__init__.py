# -*- coding: utf-8 -*-

from flask import Flask
import os

from models import db

# start Flask app
#
app = Flask(__name__)

# configure database
#
#DATABASE_URL = 'mysql://root@127.0.0.1:3307/db?charset=utf8&init_command=set%%20character%%20set%%20utf8' # for local testing
DATABASE_URL = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
db.init_app(app)

from app import views
