from app.models import User

class UserService():
  def get_all_users(self):
    return User.query.all()
  def get_user_by_id(self, user_id):
    return User.query.get_or_404(user_id, description=f'No User Found By ID {user_id}')
