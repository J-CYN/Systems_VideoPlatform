from flask import Flask, request, jsonify, render_template

import os
import re
from datetime import datetime
from azure.storage.blob import BlobServiceClient

app = Flask(__name__)

@app.get("/")
def homepage():
    return render_template("index.html")
