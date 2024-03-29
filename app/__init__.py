from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

ENV = os.environ.get('FLASK_ENV' or None)
DB_USER = config('DB_USER', default='postgres')
DB_PWD = config('DB_PWD', default='password')
DB_URL = config('DB_URL', default='postgres')
DB_NAME = config('DB_NAME', default='postgres')
DATABASE_URL = os.environ.get('DATABASE_URL' or None)
DATABASE_URI = DATABASE_URL if DATABASE_URL else f"postgres://{DB_USER}:{DB_PWD}@{DB_URL}/{DB_NAME}"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
mm = Marshmallow(app)

from app import router, models, errors
from app.controllers import user_controller, value_controller, stock_controller
from app.schedule import Scheduler
from app.tasks import print_hello_world


scheduler = Scheduler()
tasks = scheduler.tasks
tasks.append(print_hello_world.task)

if (ENV == 'production'):
  scheduler.run_continuously()