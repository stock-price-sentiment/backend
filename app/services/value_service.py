from app import db
from app.models import Value

class ValueService():
  def get_values_by_stock_id(self, stock_id):
    return db.session.query(Value).filter(Value.stock_id == stock_id)
  
  def get_value_by_id(self, id):
    return db.session.query(Value).get(id);
  
  def save_value(self, value):
    db.session.add(value)
    db.session.commit()
  
  def delete_value_by_id(self, id):
    db.session.query(Value).get(id).delete()
    db.session.commit()
