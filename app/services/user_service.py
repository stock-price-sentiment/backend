from app import db
from app.models import User

class UserService():
  def get_all_users(self):
    return User.query.all()
  
  def get_user_by_id(self, user_id):
    return User.query.get_or_404(user_id, description=f'No User Found By ID {user_id}')
  
  def save_user(self, user):
    db.session.add(user)
    db.session.commit()
  
  def delete_user_by_id(self, id):
    user = User.query.get_or_404(id, description=f'No User Found By ID {id}')
    db.session.delete(user)
    db.session.commit()
  
  def update_user_by_id(self, id, update):
    db.session.query.filter(User.id == id).update(update)
    db.session.commit()

    

