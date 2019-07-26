from app import app, db
from flask import jsonify, request
from app.models import Stock, StockSchema

PREFIX = '/api/stock'
stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)

@app.route(PREFIX, methods=['POST'])
def save_stock():
  stock = Stock(title=request.json['title'], ticker=request.json['ticker'])
  db.session.add(stock)
  db.session.commit()
  serialized = stock_schema.dump(stock).data
  return jsonify({'stock': serialized}), 201

@app.route(PREFIX, methods=['GET'])
def get_stocks():
  stocks = Stock.query.all()
  serialized = stocks_schema.dump(stocks).data
  return jsonify({'stocks': serialized}), 200

@app.route(PREFIX + '/<stock_id>', methods=['GET', 'DELETE'])
def get_stock(stock_id):
  if (request.method == 'GET'):
    stock = Stock.query.get_or_404(stock_id, description=f'No Stock Found by ID - {stock_id}')
    serialized = stock_schema.dump(stock).data
    return jsonify({'stock': serialized}), 200
  else:
    stock = Stock.query.get_or_404(stock_id, description=f'No Stock Found By ID - {stock_id}')
    db.session.delete(stock)
    db.session.commit()
    return jsonify({}), 204 