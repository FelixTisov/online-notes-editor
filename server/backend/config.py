import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    DB_HOST = os.environ.get('DB_HOST') or 'a0849712.xsph.ru'
    DB_USER = os.environ.get('DB_USER') or 'a0849712_online-notes-editor'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'ruf2002@215'
    DB_NAME = os.environ.get('DB_NAME') or 'a0849712_online-notes-editor'


class DevelopementConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
