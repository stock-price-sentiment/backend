from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def sanitationCheck():
    return jsonify({'message': 'Hello World.'})
