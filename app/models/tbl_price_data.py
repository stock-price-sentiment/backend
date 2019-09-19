from app import db, mm
from datetime import datetime
import simplejson

class Value(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  price = db.Column(db.Numeric(precision=8, scale=2), nullable=False)
  stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), nullable=False)

  
class ValueSchema(mm.ModelSchema):
  class Meta:
    model = Value
    json_module = simplejson