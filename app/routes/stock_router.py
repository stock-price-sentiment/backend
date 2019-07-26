from app import app, db
from flask import jsonify, request
from app.models import Stock, StockSchema

PREFIX = '/api/stock'

@app.route(PREFIX, methods=['POST'])
def save_stock():
  stock_schema = StockSchema()
  stock = Stock(title=request.json['title'], ticker=request.json['ticker'])
  db.session.add(stock)
  db.session.commit()
  serialized = stock_schema.dump(stock).data
  return jsonify({'stock': serialized}), 201

@app.route(PREFIX, methods=['GET'])
def get_stock():
  stocks_schema = StockSchema(many=True)
  stocks = Stock.query.all()
  serialized = stocks_schema.dump(stocks).data
  return jsonify({'stocks': serialized}), 200