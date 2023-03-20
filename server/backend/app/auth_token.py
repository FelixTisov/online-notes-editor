from app import app
import jwt
import datetime


class AuthToken:
    @staticmethod
    def encode(user_id, login_time):
        """Генерация токена аутентификации"""
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=30, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'iss': 'ken',
                'data': {
                    'id': user_id,
                    'login_time': login_time
                }
            }
            return jwt.encode(
                payload,
                app.config['SECRET_KEY'],
                algorithm='HS256'
            )
        except Exception as error:
            return error

    @staticmethod
    def decode(auth_token):
        """Проверка токена аутентификации"""
        try:
            payload = jwt.decode(auth_token, app.config['SECRET_KEY'], algorithms=['HS256'], options={'verify_exp': False})
            if 'data' in payload and 'id' in payload['data']:
                return payload
            else:
                raise jwt.InvalidTokenError
        except jwt.ExpiredSignatureError:
            return 'Token expired!'
        except jwt.InvalidTokenError:
            return 'Invalid token!'
