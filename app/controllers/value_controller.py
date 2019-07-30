from flask import jsonify, request
from flask.views import MethodView

class ValueController(MethodView):
  def get(self, value_id):
    pass
  
  def post(self):
    pass
  
  def delete(self, value_id):
    pass