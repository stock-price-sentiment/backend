from app import app
from flask import jsonify


@app.route('/', methods=['GET'])
def index():
    return jsonify({'message': 'Hello From Flask'})

