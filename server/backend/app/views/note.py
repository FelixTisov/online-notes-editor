from app import app
from flask import json, make_response, jsonify
from flask import request
from ..database import Database
from ..auth_token import AuthToken
import shortuuid

db = Database()


@app.route('/notes', methods=['POST'])
def get_notes():
    """Получение всех заметок пользователя"""
    res = None
    msg = None
    stat = None

    try:
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            payload = AuthToken.decode(token)

            if not isinstance(payload, str):
                data = request.json
                userid = data['userid']

                query = "SELECT NoteID, Title, Body, Date, Edited FROM Notes WHERE UserID = '{}'".format(userid)
                results = db.run_query(query=query)
                db.close_connection()

                if len(results) == 0:
                    raise Exception("There are no notes yet")

                res = json.dumps(results)
                msg = "Loaded"
                stat = 200
            else:
                msg = payload
                stat = 403
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg, 'body': res}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


@app.route('/notes/update', methods=['POST'])
def update_note():
    """Обновление заметки"""
    msg = None
    stat = None

    try:
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            payload = AuthToken.decode(token)

            if not isinstance(payload, str):
                data = request.json
                field = data['field']
                value = data['value']
                edited = data['edited']
                noteid = data['noteid']

                query = "UPDATE Notes SET {} = '{}', Edited = '{}' WHERE Notes.NoteID = '{}'".\
                    format(field, value, edited, noteid)
                db.run_query(query=query)
                db.close_connection()

                msg = "Note updated"
                stat = 200
            else:
                msg = payload
                stat = 403
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


@app.route('/notes/create', methods=['POST'])
def create_note():
    """Создание новой заметки"""
    noteid = None
    msg = None
    stat = None

    try:
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            payload = AuthToken.decode(token)

            if not isinstance(payload, str):
                data = request.json
                title = data['title']
                value = data['value']
                date = data['date']
                userid = data['userid']
                noteid = shortuuid.ShortUUID().random(length=16)

                query = "INSERT INTO Notes (NoteID, UserID, Body, Title, Date, Edited) " \
                        "VALUES ('{}', '{}', '{}', '{}', '{}', '{}')".format(noteid, userid, value, title, date, date)
                db.run_query(query=query)
                db.close_connection()

                msg = "Note created"
                stat = 201
            else:
                msg = payload
                stat = 403
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg, 'noteid': noteid}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response


@app.route('/notes/delete', methods=['POST'])
def delete_note():
    """Удаление заметки"""
    msg = None
    stat = None

    try:
        if 'Authorization' in request.headers:
            token = request.headers['Authorization']
            payload = AuthToken.decode(token)

            if not isinstance(payload, str):
                data = request.json
                noteids = tuple(data['noteids'])

                if len(noteids) > 1:
                    query = "DELETE FROM Notes WHERE NoteID IN {}".format(noteids)
                elif len(noteids) == 1:
                    query = "DELETE FROM Notes WHERE NoteID = '{}'".format(noteids[0])
                else:
                    raise Exception("At least one note should be selected")

                db.run_query(query=query)
                db.close_connection()

                msg = "Note deleted"
                stat = 200
            else:
                msg = payload
                stat = 403
    except Exception as error:
        msg = str(error)
        stat = 500
    finally:
        response = make_response(jsonify({'msg': msg}))
        response.status_code = stat
        response.mimetype = 'application/json'
    return response
