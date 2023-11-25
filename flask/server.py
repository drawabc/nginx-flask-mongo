#!/usr/bin/env python
import os
import json

from flask import Flask, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongo:27017")
db = client.flask_db
payload = db.payload

@app.route('/')
def todo():
    try:
        client.admin.command('ismaster')
    except:
        return "Server not available"
    return "Hello from the MongoDB client!\n"


@app.route('/ganteng', methods=['GET','POST'])
def ganteng():
    print(request, flush=True)
    return "request"

@app.route('/viewganteng')
def viewganteng():
    return "OK"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=True)

