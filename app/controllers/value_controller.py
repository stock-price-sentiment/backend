from app import app
from flask import jsonify, request
from flask.views import MethodView
from app.services.value_service import ValueService
from app.models import Value, ValueSchema

class ValueController(MethodView):
  def __init__(self):
    self.service = ValueService()
    self.schema = ValueSchema()
  
  def get(self, stock_id, value_id):
    res = None
    if value_id is None:
      self.schema.many = True
      values = self.service.get_values_by_stock_id(stock_id)
      data = self.schema.dump(values).data
      res = {'values': data}
    else:
      self.schema.many = False
      value = self.service.get_value_by_id(value_id)
      data = self.schema.dump(value).data
      res = {'value': data}
    return jsonify(res), 200
  
  def post(self, stock_id):
    self.schema.many = False
    value = Value(price=request.json['price'], stock_id=stock_id)
    self.service.save_value(value)
    data = self.schema.dump(value).data
    return jsonify({'value': data}), 201
  
  def delete(self, stock_id, value_id):
    self.service.delete_value_by_id(value_id)
    return jsonify({}), 204

VIEW = ValueController.as_view('value_controller')

app.add_url_rule(
  '/api/stock/<int:stock_id>/value', 
  defaults={'value_id': None},
  view_func=VIEW, 
  methods=['GET'])

app.add_url_rule(
  '/api/stock/<int:stock_id>/value', 
  view_func=VIEW, 
  methods=['POST',])

app.add_url_rule(
  '/api/stock/<int:stock_id>/value/<int:value_id>', 
  view_func=VIEW, 
  methods=['GET', 'DELETE'])