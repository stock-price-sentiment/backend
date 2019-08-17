from app import db
from app.models import Stock
from flask import abort

class StockService():
  def save_stock(self, stock):
    try:
      db.session.add(stock)
      db.session.commit()
    except:
      abort(400, 'Could not save stock to database, please make sure attributes are correct and try again.')
  
  def get_all_stocks(self):
    try:
      return Stock.query.all()
    except:
      abort(500, 'Could not retrieve stock data set from database. Try again later.')
  
  def get_stock_by_id(self, id):
    return Stock.query.get_or_404(id, description=f'No Stock Found By ID {id}')
  
  def delete_stock_by_id(self, id):
    stock = Stock.query.get_or_404(id, description=f'No Stock Found By ID - {id}')
    db.session.delete(stock)
    db.session.commit()
