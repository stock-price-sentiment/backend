from app import db
from app.models import User
from flask import abort

class UserService():
  def get_all_users(self):
    return User.query.all()
  
  def get_user_by_id(self, id):
    return User.query.get_or_404(id, description=f'No User Found By ID {id}')
  
  def save_user(self, user):
    try:
      db.session.add(user)
      db.session.commit()
    except:
      abort(400)
  
  def delete_user_by_id(self, id):
    user = User.query.get_or_404(id, description=f'No User Found By ID {id}')
    db.session.delete(user)
    db.session.commit()
  
  def update_user_by_id(self, id, update):
    db.session.query(User).filter(User.id == id).update(update)
    db.session.commit()

    return db.session.query(User).get(id)

    

