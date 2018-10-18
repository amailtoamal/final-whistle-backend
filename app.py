from flask import Flask, redirect, url_for, request, json
from flask_pymongo import PyMongo
from bson.json_util import dumps
import jwt,time

app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://amal:amal1234@ds131743.mlab.com:31743/final_whistle"
mongo = PyMongo(app)

encoded = jwt.encode({'some': 'payload', 'exp': int(time.time())+10}, 'secret', algorithm='HS256')

@app.route('/login', methods=['POST', 'GET'])
def login():
      x = mongo.db.users.find()
      #return dumps(x)

      try:
            decoded=jwt.decode(encoded, 'secret', algorithms=['HS256'])
      except jwt.ExpiredSignatureError:
            return "Token expired"
      except:
            return "Token invalid"
      # decoded = jwt.decode(encoded, 'secret', algorithm='HS256')
      return str(decoded)


if __name__ == "__main__":
    #app.run(host='0.0.0.0', port=8080)
    app.run(host='127.0.0.1', port=5000, debug=True)
