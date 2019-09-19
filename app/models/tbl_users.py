from app import db, mm
from datetime import datetime
import simplejson

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(), nullable=False)
  created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
  user_stock = db.relationship('UserStock', backref='user', lazy=True)

  
class UserSchema(mm.ModelSchema):
  class Meta:
    model = User