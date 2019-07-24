import unittest, nose2
from app.models import Value

class TestStock(unittest.TestCase):
  value = None

  def setUp(self):
    self.value = Value()
  
  def tearDown(self):
    self.value = None

  def test_id(self):
    ID = 1

    self.value.id = ID
    
    self.assertEqual(self.value.id, ID)
    self.assertIs(type(self.value.id), int)

  def test_price(self):
    PRICE = 299.9999

    self.value.price = PRICE

    self.assertEqual(self.value.price, PRICE)
    self.assertIs(type(self.value.price), float)

  def test_stock_id(self):
    STOCK_ID = 1

    self.value.stock_id = STOCK_ID

    self.assertEqual(self.value.stock_id, STOCK_ID)
    self.assertEqual(type(self.value.stock_id), int)