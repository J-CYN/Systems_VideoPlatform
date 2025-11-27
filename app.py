from flask import Flask, request, jsonify, render_template

import os
import re
from datetime import datetime
from azure.storage.blob import BlobServiceClient
from flask_cors import CORS

app = Flask(__name__)

CORS(app,
     resources={r"/*": {"origins": [
         "http://localhost:8080",
         "https://BlahBlah.onrender.com"#I will change this later when I host on Render
     ]}},
     supports_credentials=True)

CONTAINER_NAME="videocatalog"

bsc = BlobServiceClient.from_connection_string(os.getenv("AZURE_STORAGE_CONNECTION_STRING"))
cc  = bsc.get_container_client(CONTAINER_NAME)

@app.get("/")
def homepage():
    return render_template("index.html")

@app.get("/dashboard")
def dashboard():
    return render_template("dashboard.html")

@app.post("/api/upload")
def upload():
    if "file" not in request.files:
        return jsonify(ok=False, error="No file part in request"), 400
    
    f = request.files["file"]
    if f.filename == "":
        return jsonify(ok=False, error="No selected file"), 400
    timestamp = datetime.utcnow().strftime("%Y%m%dT%H%M%S")
    safe_filename = sanitize_filename(f.filename)
    blob_name = f"{timestamp}-{safe_filename}"
    try:
        cc.upload_blob(name=blob_name, data=f, overwrite=True)
        file_url = f"{cc.url}/{blob_name}"
        return jsonify(ok=True, url=file_url), 200
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 500

@app.get("/api/catalog")
def catalog():
    try:
        blobs = cc.list_blobs()
        gallery_urls = [
            f"https://{bsc.account_name}.blob.core.windows.net/{CONTAINER_NAME}/{blob.name}"
            for blob in blobs
        ]

        return jsonify({
            "ok": True,
            "gallery": gallery_urls
        }), 200    
    except Exception as e:
        return jsonify({
            "ok": False,
            "error": str(e)
        }), 500

@app.get("/api/health")
def health():
    return jsonify(status="ok"), 200


def sanitize_filename(filename):
    filename = os.path.basename(filename)
    filename = re.sub(r'[^A-Za-z0-9._-]', '_', filename)
    return filename

