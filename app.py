from flask import Flask, redirect, url_for, request, json
from flask_pymongo import PyMongo
from bson.json_util import dumps
import jwt,time



app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://amal:amal1234@ds131743.mlab.com:31743/final_whistle"
mongo = PyMongo(app)


@app.route('/login', methods=['POST', 'GET'])
def login():
      x = mongo.db.users.find()
      #return dumps(x)
      encoded = jwt.encode({'some': 'payload', 'exp': int(time.time())}, 'secret', algorithm='HS256')
      return encoded


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(host='127.0.0.1', port=5000, debug=True)
