import os
from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB Configuration
# MONGO_URI = "mongodb://mongo:27017/"  # MongoDB container hostname
# client = MongoClient(MONGO_URI)
# db = client["my_database"]
# collection = db["requests"]

# MongoDB configuration using environment variables
mongo_url = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')  # Default to localhost for local testing
client = MongoClient(mongo_url)
db = client[os.getenv('MONGO_DB_NAME', 'flask_with_db')]  # Default to 'flask_app_db'
collection = db[os.getenv('MONGO_COLLECTION_NAME', 'requests')]  # Default to 'requests'

# Configuration
#MONGO_URI = os.getenv("MONGO_URI")
#client = MongoClient(MONGO_URI)
#db = client["flask_app_db"]
#collection = db["requests"]


@app.route("/")
def home():
    # Log the client's IP and current date
    client_ip = request.remote_addr
    record = {"ip_address": client_ip, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    collection.insert_one(record)

    # Fetch the last 10 records from the database
    last_records = list(collection.find().sort("_id", -1).limit(10))
    for record in last_records:
        record["_id"] = str(record["_id"])  # Convert ObjectId to string for display

    # Metadata
    data = {
        "name": "Aziz Boussarsar",
        "project_name": "Flask App with DB",
        "version": "V3",
        "hostname": request.host_url,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_records": last_records,
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
