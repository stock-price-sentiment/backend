from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database

USER = config('DB_USER')
PWD = config('DB_PWD')
URL = config('DB_URL')
DB = config('DB_NAME')
DATABASE_URI = f"postgresql+psycopg2://{USER}:{PWD}@{URL}/{DB}"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

if not database_exists(DATABASE_URI):
    create_database(DATABASE_URI, template='template1')

db = SQLAlchemy(app)

from app import routes, models

db.create_all()