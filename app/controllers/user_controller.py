from app import app
from app.models import User, UserSchema
from app.services.user_service import UserService
from flask import jsonify, request
from flask.views import MethodView

class UserController(MethodView):

  def __init__(self):
    self.service = UserService()
    self.schema = UserSchema()
    self.many_schema = UserSchema(many=True)
  
  def get(self, user_id):
    res = None
    serialized = None
    if user_id is None:
      res = self.service.get_all_users()
      serialized = self.many_schema.dump(res)
    else:
      res = self.service.get_user_by_id(user_id)
      serialized = self.schema.dump(res)
    return jsonify({'user': serialized}), 200
  
  def post(self):
    user = User(
      email=request.json['email'], 
      password=request.json['password'])
    self.service.save_user(user)
    serialized = self.schema.dump(user).data
    return jsonify({'user': serialized}), 201
  
  def put(self, user_id):
    user = self.service.update_user_by_id(user_id, request.json['user'])
    serialized = self.schema.dump(user).data
    return jsonify({'user': serialized}), 200
  
  def delete(self, user_id):
    self.service.delete_user_by_id(user_id)
    return jsonify({}), 204

VIEW = UserController.as_view('user_controller')

app.add_url_rule(
  '/api/user', 
  defaults={'user_id': None},
  view_func=VIEW, 
  methods=['GET'])

app.add_url_rule(
  '/api/user', 
  view_func=VIEW, 
  methods=['POST',])

app.add_url_rule(
  '/api/user/<int:user_id>', 
  view_func=VIEW, 
  methods=['GET', 'PUT', 'DELETE'])