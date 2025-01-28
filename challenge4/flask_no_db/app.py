from flask import Flask, render_template, request
import socket

from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    data = {
        "name": "Aziz Boussarsar",
        "project_name": "Flask App without DB",
        "version": "V1",
        "hostname": request.host_url,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return render_template("index.html", data=data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
