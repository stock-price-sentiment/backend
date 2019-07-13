from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config

USER = 'postgres'
PW = 'password'
URL = '172.26.0.3:5432'
DB = 'stock'

DATABASE_URI = f"postgresql+psycopg2://{USER}:{PW}@{URL}/{DB}"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
db = SQLAlchemy(app)


class Count(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer)

    def __repr__(self):
        return f"<Count id={self.id} value={self.count}>"


db.create_all()

count = Count(count=0)
db.session.add(count)
db.session.commit()


@app.route('/', defaults={'name': 'John Doe'})
@app.route('/<name>')
def sanitationCheck(name):
    return jsonify({'message': f"Hello, {name}"})


@app.route('/hello')
def hello():
    global count
    count.count += 1
    db.session.commit()
    return jsonify({'count': count.count})
