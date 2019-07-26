from app import db
from app.models import Stock, StockSchema
from app.services.stock_service import StockService
from flask import jsonify, request

stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)
stock_service = StockService()

def save_stock():
  stock = Stock(title=request.json['title'], ticker=request.json['ticker'])
  stock_service.save_stock(stock)
  serialized = stock_schema.dump(stock).data
  return jsonify({'stock': serialized}), 201

def get_all_stocks():
  stocks = stock_service.get_all_stocks()
  serialized = stocks_schema.dump(stocks).data
  return jsonify({'stocks': serialized}), 200

def get_stock(stock_id):
  stock = stock_service.get_stock_by_id(stock_id)
  serialized = stock_schema.dump(stock).data
  return jsonify({'stock': serialized}), 200

def delete_stock(stock_id):
  stock_service.delete_stock_by_id(stock_id)
  return jsonify({}), 204 