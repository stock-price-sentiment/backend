from app import db, mm
from datetime import datetime
import simplejson

user_stock = db.Table('user_stock', 
  db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
  db.Column('stock_id', db.Integer, db.ForeignKey('stock.id'), primary_key=True)
)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  created = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
  user_stock = db.relationship(
    'Stock', 
    secondary=user_stock, 
    lazy='subquery', 
    backref=db.backref('user', lazy=True))

class Value(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  price = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
  stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)

class Stock(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(20), nullable=False)
  ticker = db.Column(db.String(5), nullable=False)
  values = db.relationship('Value', backref='stock', lazy=True)

  def __repr__(self):
    return f'<Stock id={self.id} title={self.title} ticker={self.ticker}>'

class StockSchema(mm.ModelSchema):
  class Meta:
    model = Stock

class UserSchema(mm.ModelSchema):
  class Meta:
    model = User

class ValueSchema(mm.ModelSchema):
  class Meta:
    model = Value
    json_module = simplejson

try:
  db.create_all()
  print("Connected to database!")
except:
  print("Unable to connect to database!")