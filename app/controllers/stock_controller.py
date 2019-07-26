from app import db
from app.models import Stock, StockSchema
from flask import jsonify, request

stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)

def save_stock():
  stock = Stock(title=request.json['title'], ticker=request.json['ticker'])
  db.session.add(stock)
  db.session.commit()
  serialized = stock_schema.dump(stock).data
  return jsonify({'stock': serialized}), 201

def get_all_stocks():
  stocks = Stock.query.all()
  serialized = stocks_schema.dump(stocks).data
  return jsonify({'stocks': serialized}), 200

def get_stock(stock_id):
  stock = Stock.query.get_or_404(stock_id, description=f'No Stock Found by ID - {stock_id}')
  serialized = stock_schema.dump(stock).data
  return jsonify({'stock': serialized}), 200

def delete_stock(stock_id):
  stock = Stock.query.get_or_404(stock_id, description=f'No Stock Found By ID - {stock_id}')
  db.session.delete(stock)
  db.session.commit()
  return jsonify({}), 204 