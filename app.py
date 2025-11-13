from flask import Flask, request, jsonify, render_template

import os
import re
from datetime import datetime
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

CONTAINER_NAME="video_catalog"

bsc = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
cc  = bsc.get_container_client(CONTAINER_NAME)

@app.get("/")
def homepage():
    return render_template("index.html")

@app.post("/api/upload")
def upload():
    if "file" not in request.files:
        return jsonify(ok=False, error="No file part in request"), 400
    
    f = request.files["file"]
    if f.filename == "":
        return jsonify(ok=False, error="No selected file"), 40
    #Continue Code here
    try:
        #Continue Code here
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 500

@app.get("/api/catalog")
def catalog():
    try:
        blobs = cc.list_blobs()    
    #Continue Code here
    except Exception as e:
        return jsonify({
            "ok": False,
            "error": str(e)
        }), 500

@app.get("/api/health")
def health():
    return jsonify(status="ok"), 200

"""
@app.get("/api/watch")
def catalog():    
    #Continue Code here
"""

#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=8080)
