from flask import Flask, request, jsonify
from pymongo import MongoClient
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_heroku import Heroku

app = Flask(__name__)
heroku = Heroku(app)

client = MongoClient('mongodb+srv://ethonwilles:password34521@cluster0-t779q.mongodb.net/conv?retryWrites=true&w=majority')

# 
CORS(app)

db = client['conv']
collection = db['user_messages']
ma = Marshmallow(app)


@app.route("/get-conv", methods=["GET"])
def get_conv():
    all_convs = collection.find({},{"messages":1})

    return jsonify(all_convs)

if __name__ == "__main__":
    app.run(debug=True)