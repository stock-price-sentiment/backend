import unittest, nose2
from nose2.tools import params
from app.models import User

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
    self.assertEqual(type(self.user.id), int)

  def test_email(self):
    EMAIL = 'test@email.com'

    self.user.email = EMAIL

    self.assertEqual(self.user.email, EMAIL)
    self.assertEqual(type(self.user.email), str)

