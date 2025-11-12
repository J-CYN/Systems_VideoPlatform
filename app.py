from flask import Flask, request, jsonify, render_template

import os
import re
from datetime import datetime
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

CONTAINER_NAME=

bsc = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
cc  = bsc.get_container_client(CONTAINER_NAME)

@app.get("/")
def homepage():
    return render_template("index.html")

@app.post("/api/v1/upload")
def upload():
    if "file" not in request.files:
        return jsonify(ok=False, error="No file part in request"), 400
    #Continue Code here

@app.get("/api/v1/catalog")
def catalog():    
    #Continue Code here

@app.get("/api/v1/health")
def health():
    return jsonify(status="ok"), 200

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=8080)
