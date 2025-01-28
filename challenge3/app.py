from flask import Flask, render_template, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)

# MongoDB Configuration
MONGO_URI = "mongodb://mongo:27017/"  # MongoDB container hostname
client = MongoClient(MONGO_URI)
db = client["my_database"]
collection = db["requests"]

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
        "name": "Your Name",
        "project_name": "Your Project Name",
        "version": "V2",
        "hostname": request.host_url,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_records": last_records,
    }

    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
