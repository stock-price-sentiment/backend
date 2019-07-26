from app import app
from flask import request
from app.controllers.stock_controller import save_stock, get_all_stocks, get_stock, delete_stock

GET = 'GET'
PUT = 'PUT'
POST = 'POST'
DELETE = 'DELETE'
PREFIX = '/api/stock'

@app.route(PREFIX, methods=[GET, POST])
def stocks_route():
  return save_stock() if request.method == POST else get_all_stocks()

@app.route(PREFIX + '/<stock_id>', methods=[GET, DELETE])
def stock_route(stock_id):
  return get_stock(stock_id) if request.method == GET else delete_stock(stock_id)

    