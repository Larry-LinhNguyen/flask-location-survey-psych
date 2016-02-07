from flask import render_template, request
from sqlalchemy import desc
import json

from app import app
from models import db, create_db, User, Data

@app.route('/')
def index():
    create_db() # TODO REMOVE ME once model is set in stone
    users = User.query.all()
    return render_template('index.html', users=users)

@app.route('/add_user')
def add_user():
    name = request.values.get('name')
    email = request.values.get('email')
    user = User(name, email)
    db.session.add(user)
    db.session.commit()
    return 'User added'

@app.route('/add_data', methods=['POST'])
def add_data():
    print 'WOOOOT'
    print request.data
    data = json.loads(request.data)
    print data
    return "FTW"

@app.route('/add_data_get', methods=['GET'])
def add_data_get():
    data = request.values.get('data')
    print 'data = ' + str(data)
    shit = Data()
    shit.data = data
    db.session.add(shit)
    db.session.commit()
    return 'WTF BRO'

@app.route('/datas')
def datas():
    datas = Data.query.order_by(desc(Data.created)).all()
    return '<br>'.join([str(d.created) + ' ' + str(d.data) for d in datas])
