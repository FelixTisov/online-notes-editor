import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    SECRET_KEY = os.environ.get('SECRET_KEY') or '123456'
    DB_HOST = os.environ.get('DB_HOST') or 'f0762448.xsph.ru'
    DB_USER = os.environ.get('DB_USER') or 'f0762448_test_database'
    DB_PASSWORD = os.environ.get('DB_PASSWORD') or 'testpassword'
    DB_NAME = os.environ.get('DB_NAME') or 'f0762448_test_database'


class DevelopementConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False
