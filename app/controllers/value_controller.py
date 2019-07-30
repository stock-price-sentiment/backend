from app import app
from flask import jsonify, request
from flask.views import MethodView
from app.services import ValueService
from app.models import ValueSchema

class ValueController(MethodView):
  
  def __init__(self):
    self.service = ValueService()
    self.schema = ValueSchema()

  def get(self, value_id):
    res = None
    if value_id is not None:
      self.schema.many = True
      values = self.service.get_values()
      res = {'values': self.schema.dump(values).data}
    else:
      self.schema.many = False
      value = self.service.get_value_by_id(value_id)
      res = {'value': self.schema.dump(value).data}
    return jsonify(res), 200
  
  def post(self):
    pass
  
  def delete(self, value_id):
    pass

VIEW = ValueController.as_view('value_controller')

app.add_url_rule(
  '/api/user', 
  defaults={'value_id': None},
  view_func=VIEW, 
  methods=['GET'])

app.add_url_rule(
  '/api/user', 
  view_func=VIEW, 
  methods=['POST',])

app.add_url_rule(
  '/api/user/<int:user_id>', 
  view_func=VIEW, 
  methods=['GET', 'DELETE'])