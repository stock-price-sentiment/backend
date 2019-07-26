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