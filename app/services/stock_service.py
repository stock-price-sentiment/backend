from app import db
from app.models import Stock

class StockService():
  def save_stock(self, stock):
    db.session.add(stock)
    db.session.commit()
  
  def get_all_stocks(self):
    return Stock.query.all()
  
  def get_stock_by_id(self, id):
    return Stock.query.get_or_404(id, description=f'No Stock Found By ID {id}')
  
  def delete_stock_by_id(self, id):
    stock = Stock.query.get_or_404(id, description=f'No Stock Found By ID - {id}')
    db.session.delete(stock)
    db.session.commit()
