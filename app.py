from flask import Flask,json,jsonify
from flask_restplus import Api,reqparse
from flask import request
from pymongo import MongoClient

app = Flask(__name__)
api = app(app)

client = MongoClient('mongodb://localhost:27017')
db = client ['big_client']
col = ['jet']


if __name__ == '__main__':
    app.run(debug= True)