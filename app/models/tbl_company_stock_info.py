class Stock(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(20), nullable=False)
  ticker = db.Column(db.String(5), nullable=False)
  values = db.relationship('Value', backref='stock', lazy=True)
  user_stock = db.relationship('UserStock', backref='stock  ', lazy=True)

class StockSchema(mm.ModelSchema):
  class Meta:
    model = Stock