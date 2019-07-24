import unittest, nose2
from app.models import Stock

class TestStock(unittest.TestCase):
  stock = None

  def setUp(self):
    self.stock = Stock()
  
  def tearDown(self):
    self.stock = None

  def test_id(self):
    ID = 1

    self.stock.id = ID
    
    self.assertEqual(self.stock.id, ID)
    self.assertIs(type(self.stock.id), int)

  def test_title(self):
    TITLE = 'stock title'

    self.stock.title = TITLE

    self.assertEqual(self.stock.title, TITLE)
    self.assertIs(type(self.stock.title), str)

  def test_ticker(self):
    TICKER = 'ttl'

    self.stock.ticker = TICKER

    self.assertEqual(self.stock.ticker, TICKER)
    self.assertEqual(type(self.stock.ticker), str)