from app import db, mm
from datetime import datetime
import simplejson


class UserStock(db.Model):
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True, nullable=False)
  stock_id = db.Column(db.Integer, db.ForeignKey('stock.id'), primary_key=True, nullable=False)
  created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  target_price = db.Column(db.Numeric(precision=8, scale=2), nullable=False)

class UserStockSchema(mm.ModelSchema):
  class Meta:
    model = UserStock
    json_module = simplejson