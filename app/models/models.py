from app import db, mm
from datetime import datetime
import simplejson








  def __repr__(self):
    return f'<Stock id={self.id} title={self.title} ticker={self.ticker}>'







try:
  db.create_all()
  print("Connected to database!")
except:
  print("Unable to connect to database!")