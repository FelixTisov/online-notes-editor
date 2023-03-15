from flask import Flask
import os
from flask_cors import CORS


# создание экземпляра приложения
app = Flask(__name__)
CORS(app)
app.config.from_object(os.environ.get('FLASK_ENV') or 'config.DevelopementConfig')

# инициализирует расширения
# db = SQLAlchemy(app)

# import views
from . import views
