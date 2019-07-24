import unittest, nose2
from app.models import User, Stock

class TestUser(unittest.TestCase):
  user = None

  def setUp(self):
    self.user = User()
  
  def tearDown(self):
    self.user = None

  def test_id(self):
    ID = 1

    self.user.id = ID
    
    self.assertEqual(self.user.id, ID)
    self.assertIs(type(self.user.id), int)

  def test_email(self):
    EMAIL = 'test@email.com'

    self.user.email = EMAIL

    self.assertEqual(self.user.email, EMAIL)
    self.assertIs(type(self.user.email), str)

  def test_user_stock(self):
    ID = 1
    TITLE = 'Title'
    USER_STOCK = [Stock(id=ID, title=TITLE),]

    self.user.user_stock = USER_STOCK

    self.assertEqual(len(self.user.user_stock), 1)
