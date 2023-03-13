from app import app
from flask import json, make_response, jsonify
from flask import request
import pymysql
import shortuuid
from werkzeug.security import generate_password_hash, check_password_hash


db = pymysql.connect(host='f0762448.xsph.ru',
 user='f0762448_test_database',
 password='testpassword',
 database='f0762448_test_database',
 charset='utf8mb4',
 autocommit=True)


# выполнение sql запроса
def call_query(query):
    cursor = db.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    return results


# регистрация пользователя
@app.route('/users/signup', methods=['POST'])
def signup_user():
    msg = None
    stat = None
    try:
        data = request.json
        email, password, username = data['email'], data['password'], data['userName']

        if email == '':
            raise Exception("Email can not be empty!")
        if password == '':
            raise Exception("Password can not be empty!")
        if username == '':
            raise Exception("Username can not be empty!")

        password = generate_password_hash(password, method='sha256')

        query = "INSERT INTO Users (UserID, Email, Password, UserName) VALUES (UUID(), '{}', " \
                "'{}', '{}')".format(email, password, username)
        call_query(query)

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


# авторизация пользователя
@app.route('/users/login', methods=['POST'])
def login_user():
    userid = None
    msg = None
    stat = None
    try:
        data = request.json
        email, password = data['email'], data['password']

        query = "SELECT UserID, Password FROM Users WHERE Email = '{}'".format(email)
        results = call_query(query)

        if len(results) == 0:
            raise Exception("This user does not exist")
        elif not check_password_hash(results[0][1], password):
            raise Exception("Password is incorrect")
        else:
            userid = results[0][0]
            msg = "Logged in!"
            stat = 303
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg, 'userid': userid}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


# получение всех заметок пользователя
@app.route('/notes', methods=['POST'])
def get_notes():
    res = None
    msg = None
    stat = None
    try:
        data = request.json
        userid = data['userid']

        query = "SELECT NoteID, Title, Body, Date, Edited FROM Notes WHERE UserID = '{}'".format(userid)
        results = call_query(query)

        if len(results) == 0:
            raise Exception("There are no notes yet")

        res = json.dumps(results)
        msg = "Loaded"
        stat = 200
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg, 'body': res}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


# обновление заметки
@app.route('/notes/update', methods=['POST'])
def update_note():
    # res = None
    msg = None
    stat = None
    try:
        data = request.json
        field = data['field']
        value = data['value']
        edited = data['edited']
        noteid = data['noteid']

        print(field)

        query = "UPDATE Notes SET {} = '{}', Edited = '{}' WHERE Notes.NoteID = '{}'".\
            format(field, value, edited, noteid)
        call_query(query)

        # if len(results) == 0:
        #     raise Exception("There are no notes yet")

        msg = "Note updated"
        stat = 200
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


# создание новой заметки
@app.route('/notes/create', methods=['POST'])
def create_note():
    # res = None
    noteid = None
    msg = None
    stat = None
    try:
        data = request.json
        title = data['title']
        value = data['value']
        date = data['date']
        userid = data['userid']
        noteid = shortuuid.ShortUUID().random(length=16)

        query = "INSERT INTO Notes (NoteID, UserID, Body, Title, Date, Edited) " \
                "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(noteid, userid, value, title, date, date)
        call_query(query)

        msg = "Note created"
        stat = 201
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg, 'noteid': noteid}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


# удаление заметки
@app.route('/notes/delete', methods=['POST'])
def delete_note():
    msg = None
    stat = None
    query = ''
    try:
        data = request.json
        noteids = tuple(data['noteids'])

        if len(noteids) > 1:
            query = "DELETE FROM Notes WHERE NoteID IN {}".format(noteids)
        elif len(noteids) == 1:
            query = "DELETE FROM Notes WHERE NoteID = '{}'".format(noteids[0])
        else:
            raise Exception("At least one note should be selected")

        call_query(query)

        msg = "Note deleted"
        stat = 200
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response