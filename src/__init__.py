from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

api = Api(app)

app.config.from_object('src.config.DevelopmentConfig')

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'

class Ping(Resource):
    def get(self):
        return {
            'status': 'success',
            'message': 'pong!'
        }

api.add_resource(Ping, '/ping')

