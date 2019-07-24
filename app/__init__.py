from flask import Flask
from decouple import config
from flask_sqlalchemy import SQLAlchemy
import os, time, sys

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

from app import routes, models

while True:
  try:
    db.create_all()
    print("Connected to database!")
    break;
  except:
    print('Unable to connect to database.', file=sys.stderr)
    time.sleep(1)