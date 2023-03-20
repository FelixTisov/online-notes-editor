from app import app
from flask import json, make_response, jsonify
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from ..database import Database
from ..auth_token import AuthToken
import shortuuid
import time
import requests

db = Database()


def note_generator():
    """Генерация случайного текста для заметки-примера"""
    url = 'https://hipsum.co/api/?type=hipster-centric&sentences=10'
    response = requests.get(url)
    data = response.json()
    lorem = ''
    for sentence in data:
        lorem += sentence + ' '
    return lorem


@app.route('/users/signup', methods=['POST'])
def signup_user():
    """Регистрация нового пользователя"""
    msg = None
    stat = None

    try:
        data = request.json
        email, password, username, date = data['email'], data['password'], data['userName'], data['date']
        userid = shortuuid.ShortUUID().random(length=12)
        noteid = shortuuid.ShortUUID().random(length=16)  # для дефолтной заметки-примера

        if email == '':
            raise Exception("Email can not be empty!")
        if password == '':
            raise Exception("Password can not be empty!")
        if username == '':
            raise Exception("Username can not be empty!")

        password = generate_password_hash(password, method='sha256')

        query = "INSERT INTO Users (UserID, Email, Password, UserName) VALUES ('{}', '{}', " \
                "'{}', '{}')".format(userid, email, password, username)
        db.run_query(query=query)
        db.close_connection()

        # Создание дефолтной заметки примера для нового пользователя
        default_note = note_generator()

        query = "INSERT INTO Notes (NoteID, UserID, Body, Title, Date, Edited) " \
                "VALUES ('{}', '{}', '{}', 'Default note', '{}', '{}')".format(noteid, userid, default_note, date, date)
        db.run_query(query=query)
        db.close_connection()

        msg = json.dumps("User created")
        stat = 201
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


@app.route('/users/login', methods=['POST'])
def login_user():
    """Авторизация пользователя"""
    userid = None
    msg = None
    token = None
    stat = None

    try:
        data = request.json
        email, password = data['email'], data['password']

        query = "SELECT UserID, Password FROM Users WHERE Email = '{}'".format(email)
        results = db.run_query(query=query)
        db.close_connection()

        if len(results) == 0:
            raise Exception("This user does not exist")
        elif not check_password_hash(results[0][1], password):
            raise Exception("Password is incorrect")
        else:
            userid = results[0][0]
            login_time = int(time.time())
            token = AuthToken.encode(userid, login_time)
            msg = 'Logged in!'
            stat = 303
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg, 'token': token, 'userid': userid}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response
