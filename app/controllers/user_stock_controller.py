from app import app
from flask import jsonify, request
from flask.views import MethodView

class UserStockController(MethodView):
  def __init__(self):
    pass

  def get(self):
    pass
  
  def post(self):
    pass
  
  def delete(self):
    pass

VIEW = UserStockController.as_view('user_stock_controller')

app.add_url_rule(
  '/api/user/<int:user_id>/stock',
  view_func=VIEW, 
  methods=['GET', 'POST'])

app.add_url_rule(
  '/api/user/<int:user_id>/stock/<int:stock_id>', 
  view_func=VIEW, 
  methods=['DELETE'])