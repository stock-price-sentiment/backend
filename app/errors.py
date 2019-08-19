from flask import jsonify
from app import app

@app.errorhandler(400)
def client_error(error):
  return jsonify({'error': error.description}), 400

@app.errorhandler(404)
def not_found(error):
  return jsonify({'error': error.description}), 404

@app.errorhandler(500)
def internal_error(error):
  return jsonify({'error': 'Uh oh. Thats not supposed to happen... try again later.'}), 500

@app.errorhandler(401)
def unauthorized(error):
  return jsonify({'error': 'Client does not contain the necessary authorization to access this resource.'}), 401