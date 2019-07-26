from app import app, db
from flask import jsonify, request
from app.models import Stock

PREFIX = '/api/stock'

@app.route(PREFIX, methods=['POST'])
def save_stock():
  stock = Stock(title=request.json['title'], ticker=request.json['ticker'])
  db.session.add(stock)
  db.session.commit()
  return jsonify({"stock": stock}), 201