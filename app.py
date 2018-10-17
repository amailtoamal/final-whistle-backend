from flask import Flask, redirect, url_for, request, json
from flask_pymongo import PyMongo
from bson.json_util import dumps


application = Flask(__name__)

application.config["MONGO_URI"] = "mongodb://amal:amal1234@ds131743.mlab.com:31743/final_whistle"
mongo = PyMongo(application)


@application.route('/login', methods=['POST','GET'])
def login():
      x = mongo.db.users.find()
      return dumps(x)


if __name__ == "__main__":
    application.run(host='0.0.0.0', port=8080)
