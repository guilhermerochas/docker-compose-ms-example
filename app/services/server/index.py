from flask import Flask, jsonify, render_template
import requests
import json
import os

app = Flask(__name__, template_folder=os.getcwd())


@app.route('/')
def server():
    res = requests.get('http://docker_api-service_1:3000')
    jsondata = res.json()
    lista = []
    for item in jsondata:
        lista.append(item["product"])
    return render_template("index.html", lista=lista, len=len(lista))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
