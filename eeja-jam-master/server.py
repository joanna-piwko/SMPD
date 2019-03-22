from flask import Flask
from flask import jsonify
from firebase import firebase

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate("eeia-jam-firebase-adminsdk-ngx8t-46893418d2.json")
firebase_admin.initialize_app(cred)

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify({"hello": 12})

if __name__ == "__main__":
    app.run()


