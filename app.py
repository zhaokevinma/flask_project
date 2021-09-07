from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/result")
def result():
    resp = requests.get("http://api.open-notify.org/astros.json")
    resp_json = resp.json()
    people = resp_json['people']
    res = []
    for p in people:
        name = p['name']
        res.append(name)
    return render_template('result.html', res = res)

if __name__ == '__main__':
    app.run()