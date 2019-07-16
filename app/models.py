from app import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True, nullable=False)
  password = db.Column(db.String(100), nullable=False)
  created = db.Column(db.DateTime(), nullable=False)

class Stock(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(20), nullable=False)
  ticker = db.Column(db.String(5), nullable=False)
  values = db.relationship('Value', backref='stock', lazy=True)

class Value(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created = db.Column(db.DateTime, nullable=False)
  price = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
  stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)

user_stock = db.Table('user_stock', 
  db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
  db.Column('stock_id', db.Integer, db.ForeignKey('stock.id'), primary_key=True)
)