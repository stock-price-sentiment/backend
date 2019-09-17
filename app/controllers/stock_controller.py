from app import app
from app.models import Stock, StockSchema
from app.services.stock_service import StockService
from flask import jsonify, request
from flask.views import MethodView


class StockController(MethodView):
  def __init__(self):
    self.stock_schema = StockSchema()
    self.stocks_schema = StockSchema(many=True)
    self.service = StockService()
  
  def get(self, stock_id):
    if stock_id is None:
      stocks = self.service.get_all_stocks()
      serialized = self.stocks_schema.dump(stocks).data
      return jsonify({'stocks': serialized}), 200
    else:
      stock = self.service.get_stock_by_id(stock_id)
      serialized = self.stock_schema.dump(stock).data
      return jsonify({'stock': serialized}), 200
    

  def post(self):
    stock = Stock(title=request.json['title'], ticker=request.json['ticker'])
    self.service.save_stock(stock)
    serialized = self.stock_schema.dump(stock).data
    return jsonify({'stock': serialized}), 201
  
  def delete(self):
    self.service.delete_stock_by_id(stock_id)
    return jsonify({}), 204 


VIEW = StockController.as_view('stock_controller')

app.add_url_rule(
  '/api/stock', 
  defaults={'stock_id': None},
  view_func=VIEW, 
  methods=['GET'])

app.add_url_rule(
  '/api/stock', 
  view_func=VIEW, 
  methods=['POST',])

app.add_url_rule(
  '/api/stock/<int:stock_id>', 
  view_func=VIEW, 
  methods=['GET', 'DELETE'])