from app import db
from app.models import Value
from flask import abort

class ValueService():
  def get_values_by_stock_id(self, stock_id):
    values = db.session.query(Value).filter(Value.stock_id == stock_id)
    if values:
      return values
    else:
      abort(500, 'Could\'nt retrieve value data set from database. Please try again later.')
  
  def get_value_by_id(self, id):
      value = db.session.query(Value).get(id);
      if value:
        return value
      else:
        abort(404, f'No Value Found By ID - {id}')
  
  def save_value(self, value):
    try:
      db.session.add(value)
      db.session.commit()
    except:
      abort(404, 'Could\'nt save value to database, check proper attributes and try again.')
  
  def delete_value_by_id(self, id):
    value = db.session.query(Value).get(id)
    if value:
      db.session.delete(value)
      db.session.commit()
    else:
      abort(404, f'No value found by ID {id}')
